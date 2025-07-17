<script lang="ts">
	import { cartStore } from '$lib/store';
	import { orderController } from '$lib/controllers';
	import type { order } from '$lib/types';

	import { goto } from '$app/navigation';

	//Lógica barra de carga
	import { onMount } from 'svelte';
	import { Progress } from '$lib/components/ui/progress/index.js';

	let value = $state(13);

	onMount(() => {
		const timer = setTimeout(() => (value = 80), 2000);
		return () => clearTimeout(timer);
	});
</script>

{#if cartStore.currentOrder}
	{#await orderController.createOrderWithItems(cartStore.currentOrder!, cartStore.products, cartStore.services)}
		<div class="flex min-h-screen items-center justify-center">
			<div
				class="flex animate-pulse flex-col items-center space-y-4 rounded-2xl bg-gray-600 p-6 shadow-2xl"
			>
				<p class="text-lg font-medium text-gray-700">Realizando venta, por favor espera...</p>
				<Progress {value} max={100} class="w-60" />
			</div>
		</div>
	{:then value}
		<div
			class="flex min-h-screen items-center justify-center bg-gradient-to-br from-green-100 to-green-300 p-6"
		>
			<div class="max-w-md rounded-2xl bg-white p-8 text-center shadow-2xl">
				<h1 class="mb-4 text-4xl font-extrabold text-green-700">¡Felicidades por tu compra!</h1>
				<p class="mb-8 text-gray-600">
					Gracias por confiar en nosotros. Tu pedido se ha procesado correctamente.
				</p>
				<button
					onclick={() => goto('/')}
					class="rounded-xl bg-green-600 px-6 py-2 font-semibold text-white shadow-md transition hover:bg-green-700"
				>
					Continuar
				</button>
			</div>
		</div>
	{:catch error}
		<div
			class="flex min-h-screen items-center justify-center bg-gradient-to-br from-red-100 to-red-300 p-6"
		>
			<div class="max-w-sm rounded-2xl bg-white p-6 text-center shadow-2xl">
				<svg
					class="mx-auto h-12 w-12 text-red-600"
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M18.364 5.636l-1.414-1.414L12 9.172 7.05 4.222 5.636 5.636 10.586 10.586 5.636 15.536l1.414 1.414L12 12.828l4.95 4.95 1.414-1.414-4.95-4.95 4.95-4.95z"
					/>
				</svg>
				<h2 class="text-2xl font-bold text-red-700">¡Ups! Algo salió mal</h2>
				<p class="text-gray-600">Error: {error.message}</p>
				<button
					onclick={() => goto('/')}
					class="mx-auto mt-2 block rounded-xl bg-red-600 px-5 py-2 font-medium text-white shadow transition hover:bg-red-700"
				>
					Continuar
				</button>
			</div>
		</div>
	{/await}
{/if}
