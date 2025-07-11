<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import { Button } from '$lib/components/ui/button/index.js';
	import { ShoppingBasket } from '@lucide/svelte';
	import { cartStore } from '$lib';
	import { onMount } from 'svelte';

	import { inventory, serviceStore } from '$lib/store';
	import { productController, serviceController } from '$lib';
	import type { ProductInterface } from '$lib';
	import ProductCardSelectProducts from '$lib/components/product/ProductCardSelectProducts.svelte';
	import { toast, Toaster } from 'svelte-sonner';
	import ProductCardOrdenSummary from '../product/ProductCardOrdenSummary.svelte';
	import { goto } from '$app/navigation';

	let service = $derived(cartStore.serviceSelected);
	/* let productsService: ProductInterface[] = $derived(service!.products || []);

	onMount(async () => {
		try {
			service!.products = await serviceController.getProductsOfService(service!);
		} catch (e: any) {
			toast('Algo ha salido mal', {
				description: e.message || 'No se han podido cargar los productos',
				action: {
					label: 'Aceptar',
					onClick: () => console.info('Aceptar')
				}
			});
		}
	}); */
</script>

<div class="flex h-full flex-col items-center justify-center px-8">
	<Card.Root>
		<Card.Content>
			{#if service}
				<div class="flex items-center justify-between gap-4 space-x-4">
					<div class="flex flex-col items-start justify-between gap-4">
						<h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
							{service.name}
						</h5>
						<p class="font-normal text-gray-700 dark:text-gray-400">ID: {service.id}</p>
						<p class="font-semibold text-gray-900 dark:text-white">
							Precio Fijo: ${service.price}
						</p>
						{#await serviceController.getProductsOfService(service!)}
							<p>Estamos buscando los productos, Por favor espere</p>
						{:then value}
							{#each value as productService}
								<ProductCardOrdenSummary
									bind:product={inventory.products[inventory.products.indexOf(productService)]}
									deleteButton={false}
								/>
							{/each}
						{/await}
						<Button
							onclick={() => {
								cartStore.addService(cartStore.serviceSelected!);
								cartStore.serviceSelected = null;
								goto('/new-sale');
							}}
							class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
							>Agregar a la Lista de Venta Actual <ShoppingBasket /></Button
						>
					</div>
				</div>
			{:else}
				<p>Ha ocurrido un error, por favor vuelve a seleccionar un servicio</p>
			{/if}
		</Card.Content>
	</Card.Root>
</div>
