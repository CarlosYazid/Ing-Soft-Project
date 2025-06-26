<script lang="ts">
	/* import { products } from '$lib/data/products.js'; */
	import ProductCardSelectProducts from '$lib/components/product/ProductCardSelectProducts.svelte';

	import { onMount } from 'svelte';
	import { inventory } from '$lib';
	import { productController } from '$lib';

	let products = $derived(inventory.products);

	onMount(async () => {
		inventory.products = await productController.getAll();
	});
</script>

<div class="grid grid-cols-[repeat(auto-fit,minmax(300px,375px))] justify-center gap-4 px-10">
	{#each products as product (product.id)}
		<ProductCardSelectProducts {product} />
	{/each}
</div>
