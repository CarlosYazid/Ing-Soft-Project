<script lang="ts">
	import ConfirmDialog from '$lib/components/common/ConfirmDialog.svelte';
	import type { ProductInterface, ProductRow } from '$lib/types';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { Trash2, SquarePen } from '@lucide/svelte';
	import { inventory } from '$lib/store/index';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { toast, Toaster } from 'svelte-sonner';
	import { productController } from '$lib/controllers';

	let productsInventory: ProductInterface[] = $derived(inventory.products);

	let products: ProductRow[] = $derived(
		productsInventory.map((p) => ({
			id: p.id,
			name: p.name,
			category: p.category,
			price: p.price,
			stock: p.stock
		}))
	);

	//Lógica modal de editar producto
	let editar = $state(false);

	function onEdit(row: any) {
		editar = true;
		inventory.editProduct = inventory.findProductById(row.id)!;
	}

	function confirmedEdit() {
		editar = false;
		goto('/gestionar-productos/edit-product');
	}

	function canceledEdit() {
		editar = false;
		inventory.clearEditProduct();
	}

	//Lógica modal de eliminar producto
	let eliminar = $state(false);
	function onDelete(row: any) {
		eliminar = true;
		inventory.deleteProduct = inventory.findProductById(row.id)!;
	}

	function confirmedDelete() {
		eliminar = false;
		//Lógica delete
		if (inventory.deleteProduct) {
			productController.deleteById(inventory.deleteProduct.id);
			inventory.removeProductById(inventory.deleteProduct.id);
			inventory.clearDeleteProduct();
		}
	}

	function canceledDelete() {
		eliminar = false;
		inventory.clearDeleteProduct();
	}

	// Gestionar lógica sort
	const columns = [
		{ title: 'ID', key: 'id' },
		{ title: 'Nombre', key: 'productName' },
		{ title: 'Categoría', key: 'category' },
		{ title: 'Precio', key: 'price' },
		{ title: 'Stock', key: 'stock' }
	];

	let sortField = $state('');
	let sortAsc = $state(true);

	function toggleSort(field: string) {
		if (sortField === field) {
			sortAsc = !sortAsc;
		} else {
			sortField = field;
			sortAsc = true;
		}

		products = [...products].sort((a, b) => {
			if (!sortField) return 0;
			const valA = a[sortField as keyof ProductRow];
			const valB = b[sortField as keyof ProductRow];

			if (typeof valA === 'number' && typeof valB === 'number') {
				return sortAsc ? valA - valB : valB - valA;
			}
			if (typeof valA === 'string' && typeof valB === 'string') {
				return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
			}
			return 0;
		});
	}

	onMount(async () => {
		try {
			const fetchedProducts = await productController.getAll();
			inventory.products = fetchedProducts;
		} catch (e: any) {
			toast('Algo ha salido mal', {
				description: e.message || 'No se han podido cargar los productos',
				action: {
					label: 'Aceptar',
					onClick: () => console.info('Aceptar')
				}
			});
		}
	});
</script>

<Toaster />

<div class="mt-4 flex justify-end">
	<Button
		href="/gestionar-productos/add-product"
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
		>Añadir nuevo producto</Button
	>
</div>

<div class="px-8">
	<h3 class="font-semiboldc mt-8 bg-zinc-500/15 p-4 text-lg">Lista de Productos Actuales</h3>
	{#key productsInventory}
		<Table.Root>
			<Table.Caption>Productos Actuales en la Base de Datos</Table.Caption>
			<Table.Header class="bg-zinc-500/10">
				<Table.Row>
					{#each columns as column (column.key)}
						<Table.Head onclick={() => toggleSort(column.key)} class="p-4">
							{column.title}
							{#if sortField === column.key}
								{sortAsc ? ' ↓' : ' ↑'}
							{/if}
						</Table.Head>
					{/each}
					<Table.Head class="p-4"></Table.Head>
				</Table.Row>
			</Table.Header>
			<Table.Body>
				{#each products as product (product.id)}
					<Table.Row>
						<Table.Cell class="p-4">{product.id}</Table.Cell>
						<Table.Cell class="p-4">{product.name}</Table.Cell>
						<Table.Cell class="p-4">{product.category}</Table.Cell>
						<Table.Cell class="p-4">{product.price}</Table.Cell>
						<Table.Cell class="p-4">{product.stock}</Table.Cell>
						<Table.Cell class="flex w-full justify-end gap-2"
							><Button
								onclick={() => {
									onEdit(product);
								}}
								class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"><SquarePen /></Button
							><Button
								onclick={() => {
									onDelete(product);
								}}
								class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
							></Table.Cell
						>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>
	{/key}
</div>

{#if eliminar}
	<ConfirmDialog
		callbackOnTrue={confirmedDelete}
		callbackOnFalse={canceledDelete}
		title={'¿Está seguro que desea eliminar el producto?'}
		description={'Esta acción no se puede deshacer. El producto será eliminado permanentemente.'}
		btnClass={'bg-red-700 hover:bg-red-300 hover:text-red-700'}
		action={'Eliminar'}
	/>
{/if}

{#if editar}
	<ConfirmDialog
		callbackOnTrue={confirmedEdit}
		callbackOnFalse={canceledEdit}
		title={'¿Está seguro que desea editar el producto?'}
		description={''}
		btnClass={'bg-blue-700 hover:bg-blue-300 hover:text-blue-700'}
		action={'Editar'}
	/>
{/if}
