<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { ArrowRight } from '@lucide/svelte';

	import type { ProductInterface, service } from '$lib/types';
	let product = $props();
	import { serviceStore } from '$lib/store';
</script>

<div
	class="max-w-sm rounded-lg border border-gray-200 bg-white shadow-sm dark:border-gray-700 dark:bg-gray-800"
>
	<img class="w-full rounded-t-lg" src={product.product.img as string} alt="" />

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
			<!-- Usar acá truquini para selección-->
			{#if serviceStore.productsToAdd.find((p) => p.id === product.id)}
				<Button
					onclick={() => {
						serviceStore.deleteProductFromService(product);
					}}
					size="sm"
					class="bg-red-700 hover:bg-red-300 hover:text-red-700"
					>Eliminar producto<ArrowRight /></Button
				>
			{:else}
				<Button
					onclick={() => {
						serviceStore.addProductToService(product);
						console.log(serviceStore.productsToAdd);
					}}
					size="sm"
					class="bg-green-700 hover:bg-green-300 hover:text-green-700"
					>Añadir producto<ArrowRight /></Button
				>
			{/if}
		{:else}
			<Button href="#" size="sm" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
				>Ver Detalles<ArrowRight /></Button
			>
		{/if}
	</div>
</div>
