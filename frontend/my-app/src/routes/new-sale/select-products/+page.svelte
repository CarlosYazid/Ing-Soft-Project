<script lang="ts">
	import { products } from '$lib/data/products.js';
	import ProductCardSelectProducts from '$lib/components/product/ProductCardSelectProducts.svelte';
</script>

<div class="grid grid-cols-[repeat(auto-fit,minmax(300px,375px))] justify-center gap-4 px-10">
	{#each products as product (product.id)}
		<ProductCardSelectProducts {product} />
	{/each}
</div>
