<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import Input from '$lib/components/ui/input/input.svelte';
	import { Label } from '$lib/components/ui/label/index.js';
	import { Search } from '@lucide/svelte';
	import { goto } from '$app/navigation';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { orderProducts } from '$lib/data/products.js';
	import { orderServices } from '$lib/data/products.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { onMount } from 'svelte';

	import type { client } from '$lib';
	import { clientController } from '$lib';

	let confirmar = $state(false);
	let clients: client[] = $state([]);

	function confirm() {
		confirmar = true;
	}

	function confirmedSale2() {
		confirmar = false;
		goto('/');
	}

	function canceledSale2() {
		confirmar = false;
	}

	onMount(async () => {
		clients = await clientController.getAllClients();
	});
</script>

<div class="grid grid-cols-1 justify-center gap-6">
	<div class="flex justify-center">
		<div class="grid grid-cols-4 gap-3 px-8">
			<h3 class="text-2xl font-bold">Cliente Seleccionado</h3>
			<div>
				<Label for="id">Documento de Identificacion</Label>
				<Input disabled type="id" placeholder="C.C." />
			</div>
			<div>
				<Label for="name">Nombre Completo</Label>
				<Input disabled type="text" placeholder="Nombre completo" />
			</div>
			<div>
				<Label for="number">Numero Telefonico</Label>
				<Input disabled type="text" placeholder="3..." />
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
		<Label for="id">Documento de Identificacion</Label>
		<div class="flex gap-4">
			<Input type="id" placeholder="C.C." />
			<Button class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Buscar<Search /></Button>
		</div>
		<div class="grid w-full grid-cols-1 gap-4">
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
					{#each clients as client}
						<Table.Row>
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
				<!-- <p>Cliente: {clients[0].name}</p>
				<p>Documento de identificacion: {clients[0].id}</p>
				<p>Numero telefonico: {clients[0].number}</p> -->
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
						{#each orderProducts as orderProduct (orderProduct.product.id)}
							<Table.Row>
								<Table.Cell>{orderProduct.product.name}</Table.Cell>
								<Table.Cell>{orderProduct.quantity}</Table.Cell>
								<Table.Cell
									>${(
										orderProduct.product.price * orderProduct.quantity
									).toLocaleString()}</Table.Cell
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
						{#each orderServices as orderService (orderService.service.id)}
							<Table.Row>
								<Table.Cell>{orderService.service.name}</Table.Cell>
								<Table.Cell>{orderService.service.price.toLocaleString()}</Table.Cell>
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
