<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import ProductCardOrdenSummary from '$lib/components/product/ProductCardOrdenSummary.svelte';
	/* import { orderProducts } from '$lib/data/products.js';
	import { orderServices } from '$lib/data/products.js'; */
	import { goto } from '$app/navigation';
	import ConfirmDialog from '$lib/components/common/ConfirmDialog.svelte';

	import { onMount } from 'svelte';
	import { inventory, serviceStore, cartStore } from '$lib';
	import type { ProductInterface, service } from '$lib';
	import ServiceOverView from '$lib/components/service/ServiceOverView.svelte';
	import ServiceCardOrdenSummary from '$lib/components/service/ServiceCardOrdenSummary.svelte';

	let confirmar = $state(false);

	function confirm() {
		confirmar = true;
	}

	function confirmedSale() {
		confirmar = false;
		goto('/new-sale/confirm-sale');
	}

	function canceledSale() {
		confirmar = false;
	}

	let orderProducts: ProductInterface[] = $derived(cartStore.products);
	let orderServices: service[] = $derived(cartStore.services);
	let totalStore: string = $derived.by(() => cartStore.recalculateTotal());
	$inspect(serviceStore.services).with(console.trace);
	$inspect(inventory.products).with(console.trace);
	$inspect(orderProducts);
	$inspect(orderServices);
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
			{#each orderProducts as orderProduct, i (orderProduct.id)}
				<ProductCardOrdenSummary
					bind:product={orderProducts[i]}
					deleteButton={true}
					onServiceCard={false}
				/>
			{:else}
				<p>Aún no se ha registrado ningún producto</p>
			{/each}
		</div>
		<h3 class="font-semiboldc mt-8 bg-zinc-500/5 text-lg">Lista de Servicios Seleccionados</h3>
		<div class="mt-4 grid grid-cols-1 gap-4">
			{#each orderServices as orderService, i (orderService.id)}
				<ServiceCardOrdenSummary bind:Service={orderServices[i]} />
			{:else}
				<p>Aún no se ha registrado ningún servicio</p>
			{/each}
		</div>
	</div>
	<div class="max-w-xs px-8">
		<h3 class="font-semiboldc mt-8 mb-4 text-2xl font-bold">Resumen de Venta</h3>
		<Card.Root>
			<Card.Content>
				<div class="flex flex-col gap-4">
					<p class="text-lg font-semibold">Productos Seleccionados: {orderProducts.length}</p>
					<p class="text-lg font-semibold">Servicios Seleccionados: {orderServices.length}</p>
					<p class="text-lg font-semibold">Total Venta: ${totalStore}.00</p>
					<Button
						onclick={() => {
							confirm();
						}}
						size="lg"
						class="bg-green-700 hover:bg-green-300 hover:text-green-700">Continuar Venta</Button
					>
				</div>
			</Card.Content>
		</Card.Root>
	</div>
</div>

{#if confirmar}
	<ConfirmDialog
		callbackOnTrue={confirmedSale}
		callbackOnFalse={canceledSale}
		title={'¿Está seguro que desea continuar con la venta?'}
		description={''}
		btnClass={'bg-green-700 hover:bg-green-300 hover:text-green-700'}
		action={'Continuar'}
	/>
{/if}
