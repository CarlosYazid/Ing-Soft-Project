<script lang="ts">
	import ServiceCardSelectServices from '$lib/components/service/ServiceCardSelectServices.svelte';
	import { toast } from 'svelte-sonner';
	import { onMount } from 'svelte';
	import { serviceStore } from '$lib';
	import { serviceController } from '$lib';

	let services = $derived(serviceStore.services);

	onMount(async () => {
		try {
			serviceStore.services = await serviceController.getAllServices();
		} catch (e: any) {
			toast('Algo ha salido mal', {
				description: e.message || 'No se han podido cargar los servicios',
				action: {
					label: 'Aceptar',
					onClick: () => console.info('Aceptar')
				}
			});
		}
	});
</script>

<div class="grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-4 px-10">
	{#each services as service (service.id)}
		<ServiceCardSelectServices Service={service} />
	{/each}
</div>
