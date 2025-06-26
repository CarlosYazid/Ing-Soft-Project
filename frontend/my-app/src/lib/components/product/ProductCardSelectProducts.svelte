<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { ArrowRight } from '@lucide/svelte';

	import { serviceStore } from '$lib/store';
	import type { ProductInterface, service } from '$lib/types';

	let product = $props();

	let isAdded = $state(
		(serviceStore.editService?.products?.find((p) => p.id === product.id) ? true : false) || false
	);

	function toggleProduct() {
		if (isAdded) {
			serviceStore.deleteProductFromService(product);
			isAdded = false;
		} else {
			serviceStore.addProductToService(product);
			isAdded = true;
		}
	}
</script>

<div
	class="max-w-sm rounded-lg border border-gray-200 bg-white shadow-sm dark:border-gray-700 dark:bg-gray-800"
>
	{#if !serviceStore.editService}
		<img class="w-full rounded-t-lg" src={product.product.img as string} alt="" />
	{/if}

	<div class="flex flex-col items-center p-5 text-center">
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
			{product.product.name}
		</h5>

		<p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
			{product.product.description}
		</p>
		<p class="mb-3 font-semibold text-gray-900 dark:text-white">
			Precio: ${product.product.price}
		</p>

		{#if serviceStore.editService}
			{#if isAdded}
				<Button
					onclick={toggleProduct}
					size="sm"
					class="bg-red-700 hover:bg-red-300 hover:text-red-700">Eliminar producto</Button
				>
			{:else}
				<Button
					onclick={toggleProduct}
					size="sm"
					class="bg-green-700 hover:bg-green-300 hover:text-green-700">Añadir producto</Button
				>
			{/if}
		{:else}
			<Button href="#" size="sm" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
				>Ver Detalles<ArrowRight /></Button
			>
		{/if}
	</div>
</div>
