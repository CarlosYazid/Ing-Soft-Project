<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import ProductCardOrdenSummary from '$lib/components/product/ProductCardOrdenSummary.svelte';
	import { orderProducts } from '$lib/data/products.js';
	import { orderServices } from '$lib/data/products.js';
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
<div class="grid grid-cols-4">
	<div class="col-span-3 px-8">
		<h3 class="font-semiboldc mt-8 text-2xl font-bold">Lista de Venta Actual</h3>
		<h3 class="font-semiboldc mt-8 bg-zinc-500/5 text-lg">Lista de Productos Seleccionados</h3>
		<div class="mt-4 grid grid-cols-1 gap-4">
			{#each orderProducts as orderProduct (orderProduct.product.id)}
				<ProductCardOrdenSummary {...orderProduct} />
			{/each}
		</div>
		<h3 class="font-semiboldc mt-8 bg-zinc-500/5 text-lg">Lista de Servicios Seleccionados</h3>
	</div>
	<div class="max-w-xs px-8">
		<h3 class="font-semiboldc mt-8 mb-4 text-2xl font-bold">Resumen de Venta</h3>
		<Card.Root>
			<Card.Content>
				<div class="flex flex-col gap-4">
					<p class="text-lg font-semibold">Productos Seleccionados: {orderProducts.length}</p>
					<p class="text-lg font-semibold">Servicios Seleccionados: {orderServices.length}</p>
					<p class="text-lg font-semibold">Total Venta: $0.00</p>
					<Button size="lg" class="bg-green-700 hover:bg-green-300 hover:text-green-700"
						>Confirmar Venta</Button
					>
				</div>
			</Card.Content>
		</Card.Root>
	</div>
</div>
