<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { ArrowRight } from '@lucide/svelte';

	import { serviceStore, cartStore } from '$lib/store';
	import type { ProductInterface, service } from '$lib/types';
	import { goto } from '$app/navigation';

	let { product, quantity = $bindable(0) } = $props<{
		product: ProductInterface;
		quantity?: number;
	}>();

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

	async function handleClick(product: ProductInterface) {
		cartStore.productSelected = product;
		goto('/new-sale/select-products/product-overview');
	}
</script>

<div
	class="flex max-w-sm flex-col items-center justify-center rounded-lg border border-gray-200 bg-white p-8 shadow-sm dark:border-gray-700 dark:bg-gray-800"
>
	{#if !serviceStore.editService}
		<img
			src={product.img as string}
			alt={product.name}
			class="h-48 w-48 rounded-t-lg object-cover md:h-64 md:w-64"
		/>
	{/if}

	<div class="flex flex-col items-center p-5 text-center">
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
			{product.name}
		</h5>

		<p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
			{product.description}
		</p>
		<p class="mb-3 font-semibold text-gray-900 dark:text-white">
			Precio: ${product.price}
		</p>
	</div>

	<div class="flex items-end justify-center">
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
			<Button
				onclick={() => handleClick(product)}
				size="sm"
				class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Ver Detalles<ArrowRight /></Button
			>
		{/if}
	</div>
</div>
