<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Carousel from '$lib/components/ui/carousel/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Trash2, SquarePen } from '@lucide/svelte';

	let services = [
		{ id: 1, name: 'Producto A', category: 'Categoria 1', price: '$10.000', stock: 100 },
		{ id: 2, name: 'Producto B', category: 'Categoria 2', price: '$20.000', stock: 50 },
		{ id: 3, name: 'Producto C', category: 'Categoria 1', price: '$15.000', stock: 75 },
		{ id: 4, name: 'Producto D', category: 'Categoria 3', price: '$30.000', stock: 20 },
		{ id: 5, name: 'Producto E', category: 'Categoria 2', price: '$25.000', stock: 10 },
		{ id: 6, name: 'Producto F', category: 'Categoria 1', price: '$18.000', stock: 60 },
		{ id: 7, name: 'Producto G', category: 'Categoria 3', price: '$22.000', stock: 30 }
	];
</script>

<div class="mt-4 flex justify-end">
	<Button
		href="/gestionar-productos"
		size="lg"
		class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
		>Añadir nuevo servicio</Button
	>
</div>

<div class="flex flex-col gap-4 px-10">
	<h3 class="font-semiboldc mt-8 text-lg font-bold">Lista de Servicios Actuales</h3>
	{#each services as service (service.id)}
		<Card.Root>
			<Card.Header>
				<Card.Title>{service.name}</Card.Title>
				<Card.Description>Card Description</Card.Description>
			</Card.Header>
			<Card.Content>
				<p>Card Content</p>
			</Card.Content>
			<Card.Footer class="flex max-w-max justify-center gap-2">
				<Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"><SquarePen /></Button
				><Button class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button>
			</Card.Footer>
		</Card.Root>
	{/each}
</div>
