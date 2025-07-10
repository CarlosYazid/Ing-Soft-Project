<script lang="ts">
	import type { service } from '$lib/types';
	import { Button } from '$lib/components/ui/button/index.js';
	import { ArrowRight } from '@lucide/svelte';
	import { cartStore } from '$lib/store';
	import { goto } from '$app/navigation';

	let { Service } = $props<{
		Service: service;
	}>();

	async function handleClick(Service: service) {
		cartStore.serviceSelected = Service;
		goto('/new-sale/select-services/service-overview');
	}
</script>

<div
	class="max-w-sm rounded-lg border border-gray-200 bg-white shadow-sm dark:border-gray-700 dark:bg-gray-800"
>
	<img class="w-full rounded-t-lg" src="" alt="" />

	<div class="flex flex-col items-center p-5 text-center">
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
			{Service.name}
		</h5>

		<p class="mb-3 font-semibold text-gray-900 dark:text-white">
			Precio fijo: ${Service.price.toLocaleString()}
		</p>
		<Button
			onclick={() => handleClick(Service)}
			size="sm"
			class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Ver Detalles<ArrowRight /></Button
		>
	</div>
</div>
