<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import { inventory, serviceStore, cartStore } from '$lib/store';
	import { productController, serviceController } from '$lib/controllers';

	import { onMount } from 'svelte';

	onMount(async () => {
		inventory.products = await productController.getAll();
		serviceStore.services = await serviceController.getAllServices();
		cartStore.clearCart();
	});
</script>

<div class="flex h-full flex-col items-center justify-center">
	<h1 class="text-center text-3xl font-medium">Telecomunicaciones San Antonio</h1>
	<div class="mt-4 flex justify-center">
		<Button href="/new-sale" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Registrar Nueva Venta</Button
		>
	</div>
	<div class="mt-4 flex justify-center">
		<Button href="/mi-negocio" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Gestionar Mi Negocio</Button
		>
	</div>
</div>
