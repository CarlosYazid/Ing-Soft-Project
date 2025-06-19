<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';

	//Cuando tengamos la base de datos chao
	import { onMount } from 'svelte';

	onMount(() => {
		localStorage.setItem(
			'productos',
			JSON.stringify([
				{
					id: 1,
					productName: 'Cuaderno Argollado Pasta Dura',
					description:
						'Cuaderno universitario de 100 hojas, cuadros de 7mm, ideal para tomar apuntes.',
					cost: 5000.0,
					price: 8500.0,
					category: 'Cuadernos',
					stock: 200,
					picture: null
				},
				{
					id: 2,
					productName: 'Caja de Esferos Negros x12',
					description: 'Docena de esferos de tinta negra, punta fina, escritura suave y duradera.',
					cost: 12000.0,
					price: 21900.0,
					category: 'Esferos y Lápices',
					stock: 150,
					picture: null
				},
				{
					id: 3,
					productName: 'Resaltadores Pastel x6',
					description:
						'Set de 6 resaltadores en tonos pastel, tinta de secado rápido, punta biselada.',
					cost: 9000.0,
					price: 15500.0,
					category: 'Marcadores y Resaltadores',
					stock: 90,
					picture: null
				},
				{
					id: 4,
					productName: 'Block de Hojas Iris Colores',
					description:
						'Block de 50 hojas de papel iris de colores surtidos, tamaño carta, 75 gramos.',
					cost: 4500.0,
					price: 7800.0,
					category: 'Papelería Creativa',
					stock: 180,
					picture: null
				},
				{
					id: 5,
					productName: 'Carpeta de Archivo Plástica Oficio',
					description:
						'Carpeta plástica tamaño oficio con elástico, ideal para organizar documentos.',
					cost: 3000.0,
					price: 5200.0,
					category: 'Organización',
					stock: 100,
					picture: null
				}
			])
		);
	});
</script>

<div class="flex h-full flex-col items-center justify-center">
	<h1 class="text-center text-3xl font-medium">Telecomunicaciones San Antonio</h1>
	<div class="mt-4 flex justify-center">
		<Button href="#" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Registrar Nueva Venta</Button
		>
	</div>
	<div class="mt-4 flex justify-center">
		<Button href="/mi-negocio" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Gestionar Mi Negocio</Button
		>
	</div>
</div>
