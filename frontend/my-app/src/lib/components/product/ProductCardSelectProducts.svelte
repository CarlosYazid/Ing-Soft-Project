<script lang="ts">
	import type { ProductInterface } from '$lib/types';
	export let product: ProductInterface;
	import { Button } from '$lib/components/ui/button/index.js';
	import { ArrowRight } from '@lucide/svelte';
</script>

<div
	class="max-w-sm rounded-lg border border-gray-200 bg-white shadow-sm dark:border-gray-700 dark:bg-gray-800"
>
	<img class="w-full rounded-t-lg" src={product.img} alt="" />

	<div class="flex flex-col items-center p-5 text-center">
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
			{product.name}
		</h5>

		<p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
			{product.description}
		</p>
		<p class="mb-3 font-semibold text-gray-900 dark:text-white">
			Precio: ${product.price.toLocaleString()}
		</p>
		<Button href="#" size="sm" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Ver Detalles<ArrowRight /></Button
		>
	</div>
</div>
