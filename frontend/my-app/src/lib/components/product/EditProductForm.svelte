<script lang="ts">
	import { onMount } from 'svelte';
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button/index.js';
	import SuccessOrFailDialog from '$lib/components/common/SuccessOrFailDialog.svelte';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import * as Command from '$lib/components/ui/command/index.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import ChevronsUpDownIcon from '@lucide/svelte/icons/chevrons-up-down';
	import { cn } from '$lib/utils';
	import { tick } from 'svelte';

	import type { productForm } from '../types';

	const categoriesComboBox = [
		{ value: 'papeleria', label: 'Papelería' },
		{ value: 'comestible', label: 'Comestible' }
	];

	let open = $state(false);
	let value = $state('');
	let triggerRef = $state<HTMLButtonElement>(null!);

	const selectedValue = $derived(categoriesComboBox.find((f) => f.value === value)?.label);

	// We want to refocus the trigger button when the user selects
	// an item from the list so users can continue navigating the
	// rest of the form with the keyboard.
	function closeAndFocusTrigger() {
		open = false;
		tick().then(() => {
			triggerRef.focus();
		});
	}

	let editProduct: productForm | null = $state(null);
	let infoDialog: boolean = $state(false);

	let productName = $state('');
	let description = $state('');
	let cost = $state(0);
	let price = $state(0);
	let category = $state('');
	let stock = $state(0);
	let picture: File | null = $state(null);

	function getAll(): productForm[] {
		const raw = localStorage.getItem('productos');
		return raw ? JSON.parse(raw) : [];
	}
	function saveAll(list: productForm[]) {
		localStorage.setItem('productos', JSON.stringify(list));
	}
	function addProducto(p: productForm) {
		const list = getAll();
		list.push(p);
		saveAll(list);
	}
	function editProducto(p: productForm) {
		const list = getAll().map((x) => (x.id === p.id ? p : x));
		saveAll(list);
	}

	function obtenerIdUnicoProducto(): number {
		const ids = new Set(getAll().map((p) => p.id));
		let nuevoId = 1;
		while (ids.has(nuevoId)) nuevoId++;
		return nuevoId;
	}

	onMount(() => {
		const raw = localStorage.getItem('editProduct');
		if (raw) {
			editProduct = JSON.parse(raw);
			localStorage.removeItem('editProduct');
		}

		if (editProduct) {
			({ productName, description, cost, price, category, stock } = editProduct);
		}
	});

	function validateProductForm(data: productForm) {
		const errors: Record<string, string> = {};
		if (!data.productName.trim()) errors.productName = 'El nombre es obligatorio.';
		if (!data.description.trim()) errors.description = 'La descripción es obligatoria.';
		if (data.cost < 0) errors.cost = 'El costo no puede ser negativo.';
		if (data.price <= 0) errors.price = 'El precio debe ser mayor a cero.';
		if (!data.category.trim()) errors.category = 'La categoría es obligatoria.';
		if (data.stock < 0) errors.stock = 'El stock no puede ser negativo.';
		if (!data.picture || data.picture.size === 0) errors.picture = 'Debes subir una imagen válida.';

		return { valid: Object.keys(errors).length === 0, errors };
	}

	async function handleSubmit(event: SubmitEvent) {
		event.preventDefault();
		const form = event.currentTarget as HTMLFormElement;
		const formData = new FormData(form);
		const newProduct: productForm = {
			id: editProduct ? editProduct.id : obtenerIdUnicoProducto(),
			productName: formData.get('ProductName')?.toString().trim() || '',
			description: formData.get('description')?.toString().trim() || '',
			cost: Number(formData.get('cost')) || 0,
			price: Number(formData.get('price')) || 0,
			category: formData.get('category')?.toString().trim() || '',
			stock: Number(formData.get('stock')) || 0,
			picture: formData.get('picture') as File
		};

		const { valid } = validateProductForm(newProduct);
		infoDialog = valid;

		if (valid) {
			if (editProduct) {
				editProducto(newProduct);
			} else {
				addProducto(newProduct);
			}
			form.reset();
		}
	}
</script>

<form onsubmit={handleSubmit} class="w-sm md:w-md" enctype="multipart/form-data">
	<div class="flex flex-col gap-6">
		<div>
			<Label for="ProductName">Nombre de Producto</Label>
			<Input name="ProductName" bind:value={productName} required />
		</div>

		<div>
			<Label for="description">Descripción</Label>
			<Input name="description" bind:value={description} required />
		</div>

		<div>
			<Label for="cost">Costo de Compra</Label>
			<div class="flex items-center gap-1">
				<span>$</span>
				<Input name="cost" type="number" bind:value={cost} min="0" required />
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div>
			<Label for="price">Precio de Venta</Label>
			<div class="flex items-center gap-1">
				<span>$</span>
				<Input name="price" type="number" bind:value={price} min="0" required />
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div>
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
							{selectedValue || 'Select a category...'}
							<ChevronsUpDownIcon class="opacity-50" />
						</Button>
					{/snippet}
				</Popover.Trigger>
				<Popover.Content class="w-full p-0">
					<Command.Root>
						<Command.Input placeholder="Search category..." />
						<Command.List>
							<Command.Empty>No category found.</Command.Empty>
							<Command.Group value="categoriesComboBox">
								{#each categoriesComboBox as category (category.value)}
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
			<Input type="hidden" name="category" {value} />
		</div>

		<div>
			<Label for="stock">Stock</Label>
			<Input name="stock" type="number" bind:value={stock} min="0" />
		</div>

		<div>
			<Label for="picture">Imagen</Label>
			<Input
				name="picture"
				type="file"
				required={!editProduct}
				onchange={(e) => {
					const files = (e.target as HTMLInputElement).files;
					if (files?.length) picture = files[0];
				}}
			/>
		</div>
	</div>

	<div class="mt-4 flex justify-between">
		<Button type="submit" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700 "
			>{editProduct ? 'Actualizar' : 'Crear'}</Button
		>
		<Button href="/gestionar-productos" variant="outline">Regresar</Button>
	</div>
</form>

{#if infoDialog}
	<SuccessOrFailDialog {infoDialog} contentDialog="" />
{/if}
