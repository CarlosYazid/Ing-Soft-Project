<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import ChevronsUpDownIcon from '@lucide/svelte/icons/chevrons-up-down';
	import { cn } from '$lib/utils';

	// Tipado
	import type { productForm } from '../types';
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

	function validateProductForm(data: productForm): {
		valid: boolean;
		errors: Partial<Record<keyof productForm, string>>;
	} {
		const errors: Partial<Record<keyof productForm, string>> = {};

		if (!data.productName.trim()) errors.productName = 'El nombre es obligatorio.';
		if (!data.description.trim()) errors.description = 'La descripción es obligatoria.';
		if (data.cost < 0) errors.cost = 'El costo no puede ser negativo.';
		if (data.price <= 0) errors.price = 'El precio debe ser mayor a cero.';
		if (!data.category.trim()) errors.category = 'La categoría es obligatoria.';
		if (data.stock < 0) errors.stock = 'El stock no puede ser negativo.';
		if (!data.picture || !(data.picture instanceof File) || data.picture.size === 0) {
			errors.picture = 'Debes subir una imagen válida.';
		}

		return {
			valid: Object.keys(errors).length === 0,
			errors
		};
	}
	function obtenerIdUnicoProducto(): number {
		const productosRaw = localStorage.getItem('productos');
		const productos: { id: number }[] = productosRaw ? JSON.parse(productosRaw) : [];

		// Obtener todos los IDs existentes
		const ids = new Set(productos.map((p) => p.id));

		// Buscar el menor número posible no repetido
		let nuevoId = 1;
		while (ids.has(nuevoId)) {
			nuevoId++;
		}

		return nuevoId;
	}

	function getProductFormValues(form: HTMLFormElement): productForm {
		const formData = new FormData(form);

		const productName = (formData.get('ProductName') || '').toString().trim();
		const description = (formData.get('description') || '').toString().trim();
		const cost = Number(formData.get('cost')) || 0;
		const price = Number(formData.get('price')) || 0;
		const category = (formData.get('category') || '').toString().trim();
		const stock = Number(formData.get('stock')) || 0;
		const picture = formData.get('picture') as File;

		return {
			id: obtenerIdUnicoProducto(),
			productName,
			description,
			cost,
			price,
			category,
			stock,
			picture
		};
	}
	$inspect(infoDialog);
	function agregarProductoAlStorage(producto: any): void {
		const productosRaw = localStorage.getItem('productos');
		const productos = productosRaw ? JSON.parse(productosRaw) : [];

		productos.push(producto);
		eliminarProductoExacto(product);
		localStorage.setItem('productos', JSON.stringify(productos));
	}

	function handleSubmit(event: SubmitEvent) {
		event.preventDefault();
		const form = event.currentTarget as HTMLFormElement;
		const values = getProductFormValues(form);
		const validation = validateProductForm(values);

		infoDialog = validation.valid;
		if (validation.valid) {
			agregarProductoAlStorage(values);
			form.reset();
		}
	}

	function eliminarProductoExacto(productoAEliminar: productForm): void {
		const raw = localStorage.getItem('productos');
		if (!raw) return;

		const productos: productForm[] = JSON.parse(raw);

		// Usamos JSON.stringify para comparar todos los campos
		const filtrados = productos.filter(
			(p) => JSON.stringify(p) !== JSON.stringify(productoAEliminar)
		);

		localStorage.setItem('productos', JSON.stringify(filtrados));
	}

	/*Estado para reciclar lógica*/
	let product = $props();
	let id = $state(product.id);
	let productName = $state(product.productName);
	let description = $state(product.description);
	let cost = $state(product.cost);
	let price = $state(product.price);
	let category = $state(product.category);
	let stock = $state(product.stock);
	let picture = $state<File | null>(product.picture);
</script>

<form id="form" onsubmit={handleSubmit} class="w-sm md:w-md" enctype="multipart/form-data">
	<div class="flex flex-col gap-6">
		<div class="grid gap-2">
			<Label for="ProductName">Nombre de Producto</Label>
			<Input
				name="ProductName"
				type="text"
				placeholder="Compás"
				bind:value={productName}
				required
			/>
		</div>

		<div class="grid gap-2">
			<Label for="description">Descripción de Producto</Label>
			<Input
				name="description"
				type="text"
				placeholder="Compás metálico con rueda de precisión de marca Mapped"
				bind:value={description}
				required
			/>
		</div>

		<div class="grid gap-2">
			<Label for="cost">Costo de Compra</Label>
			<div class="flex items-center gap-1">
				<span class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</span>
				<Input type="text" name="cost" id="cost" placeholder="0.00" bind:value={cost} required />
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div class="grid gap-2">
			<Label for="price">Precio de Venta</Label>
			<div class="flex items-center gap-1">
				<span class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</span>
				<Input type="text" name="price" id="price" placeholder="0.00" bind:value={price} required />
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
								{selectedValue || category || 'Selecciona una Categoría...'}
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
			<Input name="stock" type="text" placeholder="20" bind:value={stock} required />
		</div>

		<div class="grid gap-2">
			<Label for="picture">Imagen de Producto</Label>
			<Input
				name="picture"
				type="file"
				required
				onchange={(e) => {
					const input = e.target as HTMLInputElement;
					picture = input.files?.[0] || null;
				}}
			/>
		</div>
	</div>

	<div class="mt-4 flex items-center justify-between">
		<Button type="submit" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Añadir producto</Button
		>
		<Button class="bg-red-700 hover:bg-red-500" href="/gestionar-productos">Regresar</Button>
	</div>
</form>

{#key infoDialog}
	{#if infoDialog}
		<SuccessOrFailDialog {infoDialog} contentDialog="" />
	{/if}
{/key}
