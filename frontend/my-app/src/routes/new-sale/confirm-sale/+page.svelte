<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import Input from '$lib/components/ui/input/input.svelte';
	import { Label } from '$lib/components/ui/label/index.js';
	import { clients } from '$lib/data/products.js';
	import { Search } from '@lucide/svelte';
	import { goto } from '$app/navigation';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { orderProducts } from '$lib/data/products.js';
	import { orderServices } from '$lib/data/products.js';

	import * as Table from '$lib/components/ui/table/index.js';

	let confirmar = $state(false);

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
</script>

<div class="grid grid-cols-1 gap-4">
	<div class="flex justify-center">
		<div class="grid grid-cols-1 gap-3 px-8">
			<h3 class="text-2xl font-bold">Cliente Seleccionado</h3>
			<Label for="id-{clients[0].id}">Documento de Identificacion</Label>
			<Input disabled type="id" placeholder="C.C." />
			<Label for="name-{clients[0].name}">Nombre Completo</Label>
			<Input disabled type="text" placeholder="Nombre completo" />
			<Label for="number-{clients[0].id}">Numero Telefonico</Label>
			<Input disabled type="text" placeholder="3..." />
		</div>
	</div>
	<div class=" grid grid-cols-2 flex-col items-center justify-center gap-8 px-8 pt-4">
		<div class="grid grid-cols-1 gap-4">
			<h3 class="text-2xl font-bold">Buscar Cliente</h3>
			<Label for="id-{clients[0].id}">Documento de Identificacion</Label>
			<div class="flex">
				<Input type="id" placeholder="C.C." />
				<Button class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Buscar<Search /></Button>
			</div>
			<Label for="name-{clients[0].name}">Nombre Completo</Label>
			<Input type="text" placeholder="Nombre completo" />
			<Label for="number-{clients[0].id}">Numero Telefonico</Label>
			<Input type="text" placeholder="3..." />
			<Button class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Seleccionar Cliente</Button
			>
		</div>
		<div class="grid grid-cols-1 gap-4">
			<h3 class="text-2xl font-bold">Registrar Nuevo Cliente</h3>
			<Label for="id-{clients[0].id}">Documento de Identificacion</Label>
			<Input type="id" placeholder="C.C." />
			<Label for="name-{clients[0].name}">Nombre Completo</Label>
			<Input type="text" placeholder="Nombre completo" />
			<Label for="number-{clients[0].id}">Numero Telefonico</Label>
			<Input type="text" placeholder="3..." />
			<Button class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Registrar Cliente</Button>
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
</div>

{#if confirmar}
	<Dialog.Root bind:open={confirmar}>
		<Dialog.Content>
			<Dialog.Header>
				<Dialog.Title>¿Está seguro de finalizar la venta?</Dialog.Title>
			</Dialog.Header>
			<div>
				<p>Cliente: {clients[0].name}</p>
				<p>Documento de identificacion: {clients[0].id}</p>
				<p>Numero telefonico: {clients[0].number}</p>
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
