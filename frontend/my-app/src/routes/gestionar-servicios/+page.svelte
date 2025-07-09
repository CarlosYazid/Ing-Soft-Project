<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Trash2, SquarePen } from '@lucide/svelte';
	import { toast, Toaster } from 'svelte-sonner';
	import ConfirmDialog from '$lib/components/common/ConfirmDialog.svelte';

	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	import { serviceStore } from '$lib';
	import { serviceController } from '$lib';

	let services = $derived(serviceStore.services);

	onMount(async () => {
		try {
			serviceStore.services = await serviceController.getAllServices();
		} catch (e: any) {
			toast('Algo ha salido mal', {
				description: e.message || 'No se han podido cargar los productos',
				action: {
					label: 'Aceptar',
					onClick: () => console.info('Aceptar')
				}
			});
		}
	});

	//Lógica modal de editar producto
	let editar = $state(false);
	function onEdit(row: any) {
		editar = true;
		serviceStore.editService = row;
		serviceStore.addProductToService = row.products;
	}

	function confirmedEdit() {
		editar = false;
		goto('/gestionar-servicios/edit-service');
	}

	function canceledEdit() {
		editar = false;
		serviceStore.clearEditService();
	}

	//Lógica modal de eliminar producto
	let eliminar = $state(false);
	function onDelete(row: any) {
		eliminar = true;
		serviceStore.deleteService = serviceStore.findServiceById(row.id);
	}

	$inspect(serviceStore.deleteService);
	$inspect(serviceStore.services);

	function confirmedDelete() {
		eliminar = false;
		//Lógica delete
		if (serviceStore.deleteService) {
			serviceController.deleteServiceById(serviceStore.deleteService.id);
			serviceStore.removeServiceById(serviceStore.deleteService.id);
			serviceStore.clearDeleteService();
		}
	}

	function canceledDelete() {
		eliminar = false;
		serviceStore.clearDeleteService();
	}
</script>

<Toaster />

<div class="mt-4 flex justify-end">
	<Button
		href="/gestionar-servicios/add-service"
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
		>Añadir nuevo servicio</Button
	>
</div>
<h3 class="font-semiboldc mt-8 px-10 pb-5 text-lg font-bold">Lista de Servicios Actuales</h3>
<div class="grid grid-cols-[repeat(auto-fit,minmax(260px,1fr))] gap-4 px-10">
	{#each services as service (service.id)}
		<Card.Root>
			<Card.Header>
				<Card.Title>
					<div class="flex items-center justify-between">
						<h3 class="text-2xl">{service.name}</h3>
						<div class="flex gap-2">
							<Button
								class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
								onclick={() => {
									onEdit(service);
								}}><SquarePen /></Button
							><Button
								class="bg-red-700 hover:bg-red-300 hover:text-red-700"
								onclick={() => {
									onDelete(service);
								}}><Trash2 /></Button
							>
						</div>
					</div>
				</Card.Title>
				<Card.Description>Costo fijo: {service.price}</Card.Description>
			</Card.Header>
			<Card.Content>
				<!-- <h1>Productos Asociados:</h1>
				{#each service.listProducts as product (product.id)}
					<p class="text-sm">{product.name}</p>
				{/each} -->
			</Card.Content>
		</Card.Root>
	{/each}
</div>

{#if eliminar}
	<ConfirmDialog
		callbackOnTrue={confirmedDelete}
		callbackOnFalse={canceledDelete}
		title={'¿Está seguro que desea eliminar el Servicio?'}
		description={'Esta acción no se puede deshacer. El servicio será eliminado permanentemente.'}
		btnClass={'bg-red-700 hover:bg-red-300 hover:text-red-700'}
		action={'Eliminar'}
	/>
{/if}

{#if editar}
	<ConfirmDialog
		callbackOnTrue={confirmedEdit}
		callbackOnFalse={canceledEdit}
		title={'¿Está seguro que desea editar el Servicio?'}
		description={''}
		btnClass={'bg-blue-700 hover:bg-blue-300 hover:text-blue-700'}
		action={'Editar'}
	/>
{/if}
