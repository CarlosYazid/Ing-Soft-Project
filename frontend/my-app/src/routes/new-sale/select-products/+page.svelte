<script lang="ts">
	/* import { products } from '$lib/data/products.js'; */
	import ProductCardSelectProducts from '$lib/components/product/ProductCardSelectProducts.svelte';

	import { inventory } from '$lib';

	let products = $derived(inventory.products);

	let searchTerm = $state('');
	let filteredProducts = $derived(
		searchTerm.trim()
			? [...products].filter((p) => p.name.toLowerCase().startsWith(searchTerm.toLowerCase()))
			: products
	);
</script>

<div class="flex w-full flex-col items-center gap-6 p-8">
	<div class="flex gap-4">
		<input
			type="text"
			placeholder="Buscar producto..."
			bind:value={searchTerm}
			class="rounded border px-3 py-2"
		/>
		<button class="rounded bg-blue-600 px-4 py-2 text-white hover:bg-blue-500"> Buscar </button>
	</div>
	<div
		class="grid w-full grid-cols-[repeat(auto-fit,minmax(300px,375px))] justify-center gap-4 px-10"
	>
		{#key searchTerm}
			{#each filteredProducts as product (product.id)}
				<ProductCardSelectProducts {product} />
			{:else}
				<p class="col-span-full text-center text-gray-500">No se encontraron productos.</p>
			{/each}
		{/key}
	</div>
</div>
