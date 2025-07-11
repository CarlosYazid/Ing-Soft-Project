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
	import { cartStore, clientController } from '$lib';
	import { SquarePen, Trash2 } from '@lucide/svelte';

	onMount(async () => {
		clients = await clientController.getAllClients();
	});

	let confirmar = $state(false);
	let clients: client[] = $state([]);

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
</script>

<div class="mt-4 flex justify-end">
	<Button
		href="/gestionar-clientes/add-client"
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
								><Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
									><SquarePen /></Button
								><Button class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
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
