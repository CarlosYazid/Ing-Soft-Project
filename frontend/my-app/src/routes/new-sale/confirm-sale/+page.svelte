<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import Input from '$lib/components/ui/input/input.svelte';
	import { Label } from '$lib/components/ui/label/index.js';
	import { Search } from '@lucide/svelte';
	import { goto } from '$app/navigation';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { onMount } from 'svelte';

	import type { client } from '$lib';
	import { cartStore, clientController } from '$lib';

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

	function confirm() {
		confirmar = true;
	}

	function confirmedSale2() {
		confirmar = false;
		cartStore.clearCart();
		goto('/gracias');
	}

	function canceledSale2() {
		confirmar = false;
	}

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

<div class="grid grid-cols-1 justify-center gap-6 p-8">
	<div class="flex justify-center">
		<h3 class="text-2xl font-bold">Cliente Seleccionado</h3>
		<div class="grid grid-cols-3 gap-3 px-8">
			<div class="">
				<Label for="id">Documento de Identificacion</Label>
				<Input disabled type="id" placeholder="C.C." bind:value={selectedDocumentid} />
			</div>
			<div>
				<Label for="name">Nombre Completo</Label>
				<Input disabled type="text" placeholder="Nombre completo" bind:value={selectedName} />
			</div>
			<div>
				<Label for="number">Numero Telefonico</Label>
				<Input disabled type="text" placeholder="3..." bind:value={selectedPhone} />
			</div>
		</div>
	</div>

	<div class="flex justify-center">
		<Button
			onclick={() => {
				confirm();
			}}
			size="lg"
			class="bg-green-700 hover:bg-green-300 hover:text-green-700">Finalizar Venta</Button
		>
	</div>

	<div class="flex w-full flex-col items-center justify-center gap-8 px-8 pt-4">
		<h3 class="text-2xl font-bold">Buscar Cliente</h3>
		<Label for="buscarNombre">Ingrese nombre de cliente</Label>
		<div class="flex gap-4">
			<Input name="buscarNombre" type="text" placeholder="ej: Andrés" bind:value={buscarNombre} />
			<Button class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Buscar<Search /></Button>
		</div>
		<div class="grid w-full grid-cols-1 gap-4">
			{#key buscarNombre}
				<Table.Root class="w-full">
					<Table.Caption>Clientes Registrados</Table.Caption>
					<Table.Header>
						<Table.Row>
							<Table.Head>Nombre</Table.Head>
							<Table.Head>Teléfono</Table.Head>
							<Table.Head>Email</Table.Head>
							<Table.Head class="text-right">Cédula de Ciudadanía</Table.Head>
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
</div>

{#if confirmar}
	<Dialog.Root bind:open={confirmar}>
		<Dialog.Content>
			<Dialog.Header>
				<Dialog.Title>¿Está seguro de finalizar la venta?</Dialog.Title>
			</Dialog.Header>
			<div>
				<p>Cliente: {selectedName}</p>
				<p>Documento de identificacion: {selectedDocumentid}</p>
				<p>Numero telefonico: {selectedPhone}</p>
			</div>
			<div>
				<p class="font-semibold">Productos Seleccionados</p>
				<Table.Root>
					<Table.Header>
						<Table.Row>
							<Table.Head>Producto</Table.Head>
							<Table.Head>Cantidad</Table.Head>
							<Table.Head>Precio</Table.Head>
						</Table.Row>
					</Table.Header>
					<Table.Body>
						{#each cartStore.products as orderProduct (orderProduct.id)}
							<Table.Row>
								<Table.Cell>{orderProduct.name}</Table.Cell>
								<Table.Cell>{orderProduct.quantity}</Table.Cell>
								<Table.Cell
									>${(orderProduct.price * orderProduct.quantity!)
										.toFixed(2)
										.toLocaleString()}</Table.Cell
								>
							</Table.Row>
						{/each}
					</Table.Body>
				</Table.Root>
			</div>
			<div>
				<p class="font-semibold">Servicios Seleccionados</p>
				<Table.Root>
					<Table.Header>
						<Table.Row>
							<Table.Head>Servicio</Table.Head>
							<Table.Head>Precio</Table.Head>
						</Table.Row>
					</Table.Header>
					<Table.Body>
						{#each cartStore.services as orderService (orderService.id)}
							<Table.Row>
								<Table.Cell>{orderService.name}</Table.Cell>
								<Table.Cell>{orderService.price.toLocaleString()}</Table.Cell>
							</Table.Row>
						{/each}
					</Table.Body>
				</Table.Root>
			</div>
			<div>
				<Button onclick={canceledSale2} class="bg-red-700 hover:bg-red-300 hover:text-red-700"
					>Cancelar</Button
				>
				<Button
					onclick={confirmedSale2}
					class="bg-green-700 hover:bg-green-300 hover:text-green-700">Finalizar</Button
				>
			</div>
		</Dialog.Content>
	</Dialog.Root>
{/if}

<div class="flex justify-center">
	<Button
		onclick={() => {
			goto('/gestionar-clientes/add-client');
		}}
		size="lg"
		class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Registrar Cliente</Button
	>
</div>
