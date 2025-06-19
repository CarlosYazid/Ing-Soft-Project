<script lang="ts">
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
</script>

<div class="mt-4 flex justify-end">
	<Button
		href="/gestionar-productos"
		size="lg"
		class="mb-4 mr-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
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
						<Table.Cell class="p-4">{product.productName}</Table.Cell>
						<Table.Cell class="p-4">{product.category}</Table.Cell>
						<Table.Cell class="p-4">{product.price}</Table.Cell>
						<Table.Cell class="p-4">{product.stock}</Table.Cell>
						<Table.Cell class="flex max-w-max justify-center gap-2"
							><Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
								><SquarePen /></Button
							><Button class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
							></Table.Cell
						>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>
	{/key}
	<Button href="/gestionar-productos/add-product" size="lg" class="mb-4 mr-4">
		Añadir nuevo producto
	</Button>
	<Button onclick={recargar} size="lg" class="mb-4 mr-4">Actualizar Estado</Button>
</div>
