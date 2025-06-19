<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import DataTable from '$lib/components/DataTable.svelte';
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { Trash2, SquarePen } from '@lucide/svelte';

	let products = [
		{ id: 1, name: 'Producto A', category: 'Categoria 1', price: '$10.000', stock: 100 },
		{ id: 2, name: 'Producto B', category: 'Categoria 2', price: '$20.000', stock: 50 },
		{ id: 3, name: 'Producto C', category: 'Categoria 1', price: '$15.000', stock: 75 },
		{ id: 4, name: 'Producto D', category: 'Categoria 3', price: '$30.000', stock: 20 },
		{ id: 5, name: 'Producto E', category: 'Categoria 2', price: '$25.000', stock: 10 },
		{ id: 6, name: 'Producto F', category: 'Categoria 1', price: '$18.000', stock: 60 },
		{ id: 7, name: 'Producto G', category: 'Categoria 3', price: '$22.000', stock: 30 }
	];
</script>

<div class="mt-4 flex justify-end">
	<Button
		href="/gestionar-productos"
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
		>Añadir nuevo producto</Button
	>
</div>

<div class="px-8">
	<h3 class="font-semiboldc mt-8 bg-zinc-500/15 text-lg">Lista de Productos Actuales</h3>
	<Table.Root>
		<Table.Caption>Productos Actuales en la Base de Datos</Table.Caption>
		<Table.Header class="bg-zinc-500/10">
			<Table.Row>
				<Table.Head class="p-4">ID</Table.Head>
				<Table.Head class="p-4">Nombre</Table.Head>
				<Table.Head class="p-4">Categoría</Table.Head>
				<Table.Head class="p-4">Precio</Table.Head>
				<Table.Head class="p-4">Stock</Table.Head>
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
					<Table.Cell class="flex max-w-max justify-center gap-2"
						><Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"><SquarePen /></Button
						><Button class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
						></Table.Cell
					>
				</Table.Row>
			{/each}
		</Table.Body>
	</Table.Root>
</div>
