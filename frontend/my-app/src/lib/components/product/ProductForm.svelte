<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Textarea } from '$lib/components/ui/textarea/index.js';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import ChevronsUpDownIcon from '@lucide/svelte/icons/chevrons-up-down';
	import { cn } from '$lib/utils';

	import SuccessOrFailDialog from '$lib/components/common/SuccessOrFailDialog.svelte';
	import { goto } from '$app/navigation';

	import { inventory } from '$lib/store';
	import { validateProduct } from '$lib/utils/validarProductForm';

	// Tipado
	import type { ProductFormInput, ProductInterface } from '$lib/types';
	import { formatErrorsToString } from '$lib/utils/formatterProductFormErrors';

	// Estados
	let open = $state(false);
	let triggerRef = $state<HTMLButtonElement>(null!);

	const categories = [
		{ value: 'Papelería', label: 'Papelería' },
		{ value: 'Comestible', label: 'Comestible' }
	];

	let selectedValue = $derived(categories.find((c) => c.value === value)?.label);

	function closeAndFocusTrigger() {
		open = false;
		triggerRef?.focus();
	}

	/*Reciclar lógica*/
	let product = inventory.editProduct;
	let value = $state(product?.category || '');

	/*Lógica de formulario*/
	function getFormData(event: Event): ProductFormInput {
		const formData = new FormData(event.target as HTMLFormElement);
		const data: ProductFormInput = {
			id: product?.id || 0, // Es 0 si se añade un producto
			name: (formData.get('ProductName') as string) || '',
			description: (formData.get('description') as string) || '',
			cost: (formData.get('cost') as string) || '',
			price: (formData.get('price') as string) || '',
			category: (formData.get('category') as string) || '',
			stock: (formData.get('stock') as string) || '',
			img: (formData.get('picture') as File) || null,
			expirationDate: '' // Se controla desde otro lugar
		};

		return data;
	}

	async function handleSubmit(event: Event) {
		event.preventDefault();

		const formData = getFormData(event);
		console.log('Datos del formulario crudos:', formData);

		// 1. Validar la información obtenida
		const errors = validateProduct(formData);

		if (Object.keys(errors).length > 0) {
			console.error('Errores de validación:', errors);
			// Aquí se mostrarán los errores al usuario en el formulario (Llamar a la modal usar lógica con states como en la página de gestionar-productos)
			showDialog = true;
			isFormValid = false;
			formErrors = formatErrorsToString(errors);
			return; // Detiene el envío si hay errores
		}

		console.log('¡Datos del formulario válidos!');
		isFormValid = true;

		// 2. Convertir a ProductInterface (con tipos correctos)
		const newProductData: ProductInterface = {
			id: formData.id,
			name: formData.name,
			description: formData.description,
			cost: parseInt(formData.cost, 10),
			price: parseFloat(formData.price),
			category: formData.category,
			stock: parseInt(formData.stock, 10),
			img: formData.img,
			expirationDate: formData.expirationDate
		};

		console.log('Producto listo para procesar:', newProductData);

		// 3. Procesar el producto (añadir o editar)
		try {
			if (product) {
				inventory.removeProductById(product.id);
				inventory.addProduct(newProductData);
				inventory.clearEditProduct();

				console.log('Producto editado:', newProductData);
				showDialog = true;
			} else {
				// Lógica para añadir un nuevo producto
				inventory.addProduct(newProductData);
				console.log('Producto añadido:', newProductData);
				showDialog = true;
			}
		} catch (error) {
			console.error('Error al guardar el producto:', error);
			alert('Hubo un error al guardar el producto. Por favor, intenta de nuevo.');
		}
	}

	// Lógica para controlar la modal
	let showDialog = $state();
	$inspect(showDialog);
	let isFormValid = $state(false);
	let formErrors = $state('');
</script>

<form onsubmit={handleSubmit} id="form" class="w-sm md:w-md" enctype="multipart/form-data">
	<div class="flex flex-col gap-6">
		<div class="grid gap-2">
			<Label for="ProductName">Nombre de Producto</Label>
			<Input name="ProductName" type="text" placeholder="Compás" value={product?.name} required />
		</div>

		<div class="grid gap-2">
			<Label for="description">Descripción de Producto</Label>
			<Textarea
				name="description"
				placeholder="Compás metálico con rueda de precisión de marca Mapped"
				value={product?.description}
				required
			/>
		</div>

		<div class="grid gap-2">
			<Label for="cost">Costo de Compra</Label>
			<div class="flex items-center gap-1">
				<span class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</span>
				<Input
					type="text"
					name="cost"
					id="cost"
					placeholder="0.00"
					value={product?.cost}
					required
				/>
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div class="grid gap-2">
			<Label for="price">Precio de Venta</Label>
			<div class="flex items-center gap-1">
				<span class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</span>
				<Input
					type="text"
					name="price"
					id="price"
					placeholder="0.00"
					value={product?.price}
					required
				/>
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div class="grid gap-2">
			<Label for="category">Categoría</Label>
			<div class="mt-2">
				<Popover.Root bind:open>
					<Popover.Trigger bind:ref={triggerRef}>
						{#snippet child({ props })}
							<Button
								{...props}
								variant="outline"
								class="w-full justify-between"
								role="combobox"
								aria-expanded={open}
							>
								{selectedValue || product?.category || 'Selecciona una Categoría...'}
								<ChevronsUpDownIcon class="opacity-50" />
							</Button>
						{/snippet}
					</Popover.Trigger>
					<Popover.Content class="w-sm p-0 md:w-md">
						<Command.Root class="w-sm md:w-md">
							<Command.Input placeholder="Buscar Categoría..." />
							<Command.List>
								<Command.Empty>Categoría no encontrada</Command.Empty>
								<Command.Group value="categories">
									{#each categories as category (category.value)}
										<Command.Item
											value={category.value}
											onSelect={() => {
												value = category.value;
												closeAndFocusTrigger();
											}}
										>
											<CheckIcon class={cn(value !== category.value && 'text-transparent')} />
											{category.label}
										</Command.Item>
									{/each}
								</Command.Group>
							</Command.List>
						</Command.Root>
					</Popover.Content>
				</Popover.Root>
			</div>
		</div>
		<Input class="hidden" bind:value name="category" />

		<div class="grid gap-2">
			<Label for="stock">Cantidad a ingresar</Label>
			<Input name="stock" type="text" placeholder="20" value={product?.stock} required />
		</div>

		<div class="grid gap-2">
			<Label for="picture">Imagen de Producto</Label>
			<Input
				name="picture"
				type="file"
				required
				onchange={(e) => {
					const input = e.target as HTMLInputElement;
					if (product?.img) {
						product.img = input.files?.[0] || null;
					}
				}}
			/>
		</div>
	</div>

	<div class="mt-4 flex items-center justify-between">
		<Button type="submit" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Añadir producto</Button
		>
		<Button
			class="bg-red-700 hover:bg-red-500"
			href="/gestionar-productos"
			onclick={() => inventory.clearEditProduct()}>Regresar</Button
		>
	</div>
</form>

{#if showDialog}
	<SuccessOrFailDialog
		infoDialog={isFormValid}
		callback={() => {
			showDialog = false;
			if (isFormValid) {
				goto('/gestionar-productos');
			}
		}}
		contentDialog={isFormValid ? '' : formErrors}
	/>
{/if}
