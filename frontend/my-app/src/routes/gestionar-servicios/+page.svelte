<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Carousel from '$lib/components/ui/carousel/index.js';
	import * as Card from '$lib/components/ui/card/index.js';
	import { Trash2, SquarePen } from '@lucide/svelte';

	let products = [
		{
			id: 1,
			name: 'Producto A',
			description: 'Descripción del Producto A',
			price: 10000,
			category: 'Categoría 1',
			stock: 50
		},
		{
			id: 2,
			name: 'Producto B',
			description: 'Descripción del Producto B',
			price: 20000,
			category: 'Categoría 2',
			stock: 30
		},
		{
			id: 3,
			name: 'Producto C',
			description: 'Descripción del Producto C',
			price: 30000,
			category: 'Categoría 1',
			stock: 20
		},
		{
			id: 4,
			name: 'Producto D',
			description: 'Descripción del Producto D',
			price: 40000,
			category: 'Categoría 3',
			stock: 10
		}
	];
	let services = [
		{
			id: 1,
			name: 'Impresión',
			shortDescription: '',
			price: '$10.000',
			listProducts: [products[0], products[2]]
		},
		{
			id: 2,
			name: 'Fotocopia',
			shortDescription: '',
			price: '$20.000',
			listProducts: [products[1], products[3]]
		},
		{
			id: 3,
			name: 'Plastificado',
			shortDescription: '',
			price: '$30.000',
			listProducts: [products[0], products[1]]
		},
		{
			id: 4,
			name: 'Envolver Regalo',
			shortDescription: '',
			price: '$40.000',
			listProducts: [products[3], products[2], products[1]]
		}
	];
</script>

<div class="mt-4 flex justify-end">
	<Button href="#" size="lg" class="mr-4 mb-4 bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
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
							<Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
								><SquarePen /></Button
							><Button class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button>
						</div>
					</div>
				</Card.Title>
				<Card.Description>Costo fijo: {service.price}</Card.Description>
			</Card.Header>
			<Card.Content>
				<h1>Productos Asociados:</h1>
				{#each service.listProducts as product (product.id)}
					<p class="text-sm">{product.name}</p>
				{/each}
			</Card.Content>
		</Card.Root>
	{/each}
</div>
