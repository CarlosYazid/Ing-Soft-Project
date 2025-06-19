<script lang="ts">
	import ConfirmDialog from '$lib/components/common/ConfirmDialog.svelte';
	import EditDialog from '$lib/components/common/EditDialog.svelte';
	import type { productForm } from '$lib/components/types';
	import { onMount } from 'svelte';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { Trash2, SquarePen } from '@lucide/svelte';

	interface Product {
		id: number;
		productName: string;
		category: string;
		price: number;
		stock: number;
	}

	let productMocks: Product[] = $state([]);
	let products = $derived(productMocks);

	function getAll(): Product[] {
		const raw = localStorage.getItem('productos');
		return raw ? JSON.parse(raw) : [];
	}

	function saveAll(list: Product[]) {
		localStorage.setItem('productos', JSON.stringify(list));
	}

	function recargar() {
		productMocks = getAll();
	}

	onMount(() => {
		products = productMocks.map((p) => ({
			id: p.id,
			productName: p.productName,
			category: p.category,
			price: p.price,
			stock: p.stock
		}));
		recargar();
	});

	let fila = $state({});

	let editar = $state(false);
	function onEdit(row: any) {
		saveEditProduct(row);
		editar = true;
	}

	let eliminar = $state(false);
	function onDelete(row: any) {
		eliminar = true;
		fila = row;
	}

	//Cuando tengamos la base de datos esto chao
	function saveEditProduct(product: any): void {
		localStorage.setItem('editProduct', JSON.stringify(product));
		const raw = localStorage.getItem('products');
		if (!raw) return;
		console.log(raw);
		const products: productForm[] = JSON.parse(raw);
		const filtered = products.filter((p) => Number(p.id) !== Number(product.id));
		console.log(filtered);

		localStorage.setItem('products', JSON.stringify(filtered));
	}

	function confirmedDelete(row: any) {
		const productos = JSON.parse(localStorage.getItem('productos')!);

		const productosFiltrados = productos.filter((p: any) => p.id !== row.id);

		localStorage.setItem('productos', JSON.stringify(productosFiltrados));

		recargar();
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
			const valA = a[sortField as keyof Product];
			const valB = b[sortField as keyof Product];

			if (typeof valA === 'number' && typeof valB === 'number') {
				return sortAsc ? valA - valB : valB - valA;
			}
			if (typeof valA === 'string' && typeof valB === 'string') {
				return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
			}
			return 0;
		});
	}
</script>

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
	{#key productMocks}
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
						<Table.Cell class="p-4">{product.productName}</Table.Cell>
						<Table.Cell class="p-4">{product.category}</Table.Cell>
						<Table.Cell class="p-4">{product.price}</Table.Cell>
						<Table.Cell class="p-4">{product.stock}</Table.Cell>
						<Table.Cell class="flex max-w-max justify-center gap-2"
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

{#key eliminar}
	{#if eliminar}
		<ConfirmDialog parametro={fila} callback={confirmedDelete} />
	{/if}
{/key}

{#key editar}
	{#if editar}
		<EditDialog />
	{/if}
{/key}
