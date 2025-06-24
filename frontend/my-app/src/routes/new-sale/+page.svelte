<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';

	import ProductCardOrdenSummary from '$lib/components/product/ProductCardOrdenSummary.svelte';

	import { products } from '$lib/data/products.js';

	let orderProducts = [
		{ product: products[0], quantity: 2 },
		{ product: products[1], quantity: 1 },
		{ product: products[2], quantity: 3 },
		{ product: products[3], quantity: 1 }
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
