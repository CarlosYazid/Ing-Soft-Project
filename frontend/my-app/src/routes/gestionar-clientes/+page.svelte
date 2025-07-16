<script lang="ts">
	import * as Table from '$lib/components/ui/table/index.js';
	import { onMount } from 'svelte';
	import { Button } from '$lib/components/ui/button/index.js';
	import Input from '$lib/components/ui/input/input.svelte';
	import { Label } from '$lib/components/ui/label/index.js';
	import { Search } from '@lucide/svelte';
	import { goto } from '$app/navigation';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import type { client } from '$lib';
	import { clientController } from '$lib';
	import { cartStore, clientStore } from '$lib/store';

	import { SquarePen, Trash2 } from '@lucide/svelte';
	import ConfirmDialog from '$lib/components/common/ConfirmDialog.svelte';

	let clients: client[] = $derived(clientStore.clients);

	onMount(async () => {
		clientStore.clients = await clientController.getAllClients();
	});

	let selectedDocumentid = $derived(cartStore.client?.documentid);
	let selectedName = $derived(cartStore.client?.name);
	let selectedPhone = $derived(cartStore.client?.phone);
	let buscarNombre = $state('');

	let filteredClients: client[] = $derived(
		buscarNombre.trim()
			? [...clients].filter((c) => c.name.toLowerCase().startsWith(buscarNombre.toLowerCase()))
			: clients
	);

	onMount(async () => {
		clients = await clientController.getAllClients();
	});

	function buildClientFromForm(
		id: number,
		documentid: number,
		nameStr: string,
		emailStr: string,
		phoneStr: string
	): client {
		return {
			id: id,
			documentid,
			name: nameStr.trim(),
			email: emailStr.trim(),
			phone: phoneStr.trim()
		};
	}

	//Lógica modal de editar cliente
	let editar = $state(false);

	function onEdit(row: any) {
		editar = true;
		clientStore.editClient = clientStore.findClientById(row.id)!;
	}

	function confirmedEdit() {
		editar = false;
		goto('/gestionar-clientes/edit-client');
	}

	function canceledEdit() {
		editar = false;
		clientStore.clearEditClient();
	}

	//Lógica modal de eliminar Cliento
	let eliminar = $state(false);
	function onDelete(row: any) {
		eliminar = true;
		clientStore.deleteClient = clientStore.findClientById(row.id)!;
	}

	function confirmedDelete() {
		eliminar = false;
		//Lógica delete
		if (clientStore.deleteClient) {
			clientController.deleteClientById(clientStore.deleteClient.id);
			clientStore.removeClientById(clientStore.deleteClient.id);
			clientStore.clearDeleteClient();
		}
	}

	function canceledDelete() {
		eliminar = false;
		clientStore.clearDeleteClient();
	}
</script>

<div class="mt-4 flex justify-end">
	<Button
		onclick={() => {
			clientStore.addingClient = true;
			goto('/gestionar-clientes/add-client');
		}}
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Añadir nuevo cliente</Button
	>
</div>
<div class="px-8">
	<h3 class="font-semiboldc mt-8 bg-zinc-500/15 p-4 text-lg">Lista de Clientes Actuales</h3>
	<div class="grid w-full grid-cols-1 gap-4">
		{#key buscarNombre}
			<Table.Root class="w-full">
				<Table.Caption>Clientes Registrados</Table.Caption>
				<Table.Header class="bg-zinc-500/10">
					<Table.Row>
						<Table.Head>Nombre</Table.Head>
						<Table.Head>Teléfono</Table.Head>
						<Table.Head>Email</Table.Head>
						<Table.Head class="text-right">Cédula de Ciudadanía</Table.Head>
						<Table.Head></Table.Head>
					</Table.Row>
				</Table.Header>
				<Table.Body>
					<!-- (client.id) -->
					{#each filteredClients as client}
						<Table.Row
							onclick={() => {
								cartStore.client = buildClientFromForm(
									client.id,
									client.documentid,
									client.name,
									client.email,
									client.phone
								);
							}}
						>
							<Table.Cell class="font-medium">{client.name}</Table.Cell>
							<Table.Cell>{client.phone}</Table.Cell>
							<Table.Cell>{client.email}</Table.Cell>
							<Table.Cell class="text-right">{client.documentid}</Table.Cell>
							<Table.Cell class="flex w-full justify-end gap-2"
								><Button
									class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
									onclick={() => onEdit(client)}><SquarePen /></Button
								><Button
									class="bg-red-700 hover:bg-red-300 hover:text-red-700"
									onclick={() => onDelete(client)}><Trash2 /></Button
								></Table.Cell
							>
						</Table.Row>
					{/each}
				</Table.Body>
				<Table.Footer>
					<Table.Row>
						<!-- <Table.Cell colspan={3}>Total</Table.Cell>
						<Table.Cell class="text-right">$2,500.00</Table.Cell> -->
					</Table.Row>
				</Table.Footer>
			</Table.Root>
		{/key}
	</div>
</div>

{#if eliminar}
	<ConfirmDialog
		callbackOnTrue={confirmedDelete}
		callbackOnFalse={canceledDelete}
		title={'¿Está seguro que desea eliminar el producto?'}
		description={'Esta acción no se puede deshacer. El cliente será eliminado permanentemente.'}
		btnClass={'bg-red-700 hover:bg-red-300 hover:text-red-700'}
		action={'Eliminar'}
	/>
{/if}

{#if editar}
	<ConfirmDialog
		callbackOnTrue={confirmedEdit}
		callbackOnFalse={canceledEdit}
		title={'¿Está seguro que desea editar el cliente?'}
		description={''}
		btnClass={'bg-blue-700 hover:bg-blue-300 hover:text-blue-700'}
		action={'Editar'}
	/>
{/if}
