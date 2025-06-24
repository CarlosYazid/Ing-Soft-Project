<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import type { ProductInterface } from '$lib/types';
	import ProductCardOrdenSummary from '$lib/components/product/ProductCardOrdenSummary.svelte';

	let products: ProductInterface[] = [
		{
			id: 1,
			name: 'Producto A',
			description: 'Descripción del Producto A',
			price: 10000,
			cost: 500,
			category: 'Categoría 1',
			stock: 50,
			img: '/1.jpg'
		},
		{
			id: 2,
			name: 'Producto B',
			description: 'Descripción del Producto B',
			price: 20000,
			cost: 1000,
			category: 'Categoría 2',
			stock: 30,
			img: '2.jpeg'
		},
		{
			id: 3,
			name: 'Producto C',
			description: 'Descripción del Producto C',
			price: 15000,
			cost: 750,
			category: 'Categoría 1',
			stock: 20,
			img: '/3.jpeg'
		},
		{
			id: 4,
			name: 'Producto D',
			description: 'Descripción del Producto D',
			price: 30000,
			cost: 1500,
			category: 'Categoría 3',
			stock: 10,
			img: '/1.jpg'
		}
	];

	let orderProducts = [
		{ product: products[0], quantity: 2 },
		{ product: products[1], quantity: 1 }
	];
</script>

<div class="mt-4 flex justify-end">
	<Button
		href="/new-sale/select-products"
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
		>Seleccionar Productos</Button
	>
	<Button
		href="/new-sale/select-services"
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
		>Seleccionar Servicios</Button
	>
</div>

<div class="px-8">
	<h3 class="font-semiboldc mt-8 text-2xl font-bold">Lista de Venta Actual</h3>
	<h3 class="font-semiboldc mt-8 bg-zinc-500/5 text-lg">Lista de Productos Seleccionados</h3>
	<div class="mt-4 grid grid-cols-1 gap-4">
		{#each orderProducts as orderProduct (orderProduct.product.id)}
			<ProductCardOrdenSummary {...orderProduct} />
		{/each}
	</div>
	<h3 class="font-semiboldc mt-8 bg-zinc-500/5 text-lg">Lista de Servicios Seleccionados</h3>
</div>
