<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import ChevronsUpDownIcon from '@lucide/svelte/icons/chevrons-up-down';
	import { cn } from '$lib/utils';

	import { inventory } from '$lib/store';

	// Tipado
	import type { ProductFormInput } from '$lib/types';
	import SuccessOrFailDialog from '$lib/components/common/SuccessOrFailDialog.svelte';

	// Estados
	let open = $state(false);
	let value = $state('');
	let triggerRef = $state<HTMLButtonElement>(null!);
	let infoDialog = $state();

	const categories = [
		{ value: 'papeleria', label: 'Papelería' },
		{ value: 'comestible', label: 'Comestible' }
	];

	let selectedValue = $derived(categories.find((c) => c.value === value)?.label);

	function closeAndFocusTrigger() {
		open = false;
		triggerRef?.focus();
	}
	$inspect(infoDialog);

	/*Reciclar lógica*/
	let product = inventory.editProduct;

	/*Lógica de formulario*/
	/* function getFormData(event: Event): ProductFormInput {
		const formData = new FormData(event.target as HTMLFormElement);
		const data: ProductFormInput = {
			name: (formData.get('ProductName') as string) || '',
			description: (formData.get('description') as string) || '',
			cost: (formData.get('cost') as string) || '',
			price: (formData.get('price') as string) || '',
			category: (formData.get('category') as string) || '',
			stock: (formData.get('stock') as string) || '',
			picture: (formData.get('picture') as File) || null
			// Si tu formulario tuviera un campo para id y expirationDate
			// id: (formData.get('id') as string) || undefined,
			// expirationDate: (formData.get('expirationDate') as string) || '',
		};

		// El ID es solo relevante si estás editando un producto existente
		// y tu formulario tiene un input hidden para el ID.
		// Por ejemplo: <input type="hidden" name="id" value={product?.id} />
		const productId = formData.get('id');
		if (productId) {
			data.id = productId as string;
		}

		return data;
	}

	async function handleSubmit(event: Event) {
		event.preventDefault(); // Evita la recarga de la página por defecto del formulario

		const formData = getFormData(event);
		console.log('Datos del formulario crudos:', formData);

		// 1. Validar la información obtenida
		const errors = validateProduct(formData);
		formErrors = errors; // Asigna los errores al estado reactivo

		if (Object.keys(errors).length > 0) {
			console.error('Errores de validación:', errors);
			// Aquí puedes mostrar los errores al usuario en el formulario
			return; // Detiene el envío si hay errores
		}

		console.log('¡Datos del formulario válidos!');

		// 2. Convertir a ProductInterface (con tipos correctos)
		const newProductData: ProductInterface = {
			// Si el ID existe (para edición), inclúyelo
			...(product?.id && { id: product.id }), // O si viene del formData: id: parseInt(formData.id, 10)
			name: formData.ProductName, // Mapea ProductName a name
			description: formData.description,
			cost: parseInt(formData.cost, 10),
			price: parseFloat(formData.price),
			category: formData.category,
			stock: parseInt(formData.stock, 10),
			img: formData.picture,
			expirationDate: Date.now() // Asumiendo que se genera automáticamente
			// Si tuvieras un campo de fecha de expiración en el formulario:
			// expirationDate: new Date(formData.expirationDate).getTime(),
		};

		console.log('Producto listo para procesar:', newProductData);

		// 3. Procesar el producto (añadir o editar)
		try {
			if (product?.id) {
				// Lógica para editar un producto existente
				// inventory.updateProduct(newProductData); // Asume que tienes un método updateProduct
				console.log('Producto editado:', newProductData);
				// Si la navegación es solo después de una confirmación en otro lado,
				// no redirecciones aquí, o redirecciona a una página de éxito.
				goto('/gestionar-productos'); // Redirecciona después de editar
			} else {
				// Lógica para añadir un nuevo producto
				await inventory.addProduct(newProductData); // Asume que addProduct es async y guarda en DB
				console.log('Producto añadido:', newProductData);
				goto('/gestionar-productos'); // Redirecciona después de añadir
			}
			alert(`Producto ${product?.id ? 'actualizado' : 'añadido'} con éxito!`);
		} catch (error) {
			console.error('Error al guardar el producto:', error);
			alert('Hubo un error al guardar el producto. Por favor, intenta de nuevo.');
			// Aquí podrías actualizar el estado `formErrors` con un error general
		}
	} */
</script>

<form id="form" class="w-sm md:w-md" enctype="multipart/form-data">
	<div class="flex flex-col gap-6">
		<div class="grid gap-2">
			<Label for="ProductName">Nombre de Producto</Label>
			<Input name="ProductName" type="text" placeholder="Compás" value={product?.name} required />
		</div>

		<div class="grid gap-2">
			<Label for="description">Descripción de Producto</Label>
			<Input
				name="description"
				type="text"
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

{#if infoDialog}
	<SuccessOrFailDialog {infoDialog} contentDialog="" />
{/if}
