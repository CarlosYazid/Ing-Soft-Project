<script lang="ts">
	import ServiceCardSelectServices from '$lib/components/service/ServiceCardSelectServices.svelte';
	import { toast } from 'svelte-sonner';
	import { onMount } from 'svelte';
	import { serviceStore } from '$lib';
	import { serviceController } from '$lib';

	let services = $derived(serviceStore.services);
</script>

<div class="grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-4 px-10">
	{#each services as service (service.id)}
		<ServiceCardSelectServices Service={service} />
	{/each}
</div>
