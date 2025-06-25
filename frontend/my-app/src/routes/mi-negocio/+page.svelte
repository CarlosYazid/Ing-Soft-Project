<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
</script>

<div class="mt-25">
	<h1 class="text-center text-3xl font-medium">¿Qué deseas hacer hoy?</h1>
	<div class="mt-4 flex justify-center">
		<Button
			href="/gestionar-productos"
			size="lg"
			class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Gestionar Productos</Button
		>
	</div>
	<div class="mt-4 flex justify-center">
		<Button
			href="/gestionar-servicios"
			size="lg"
			class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Gestionar Servicios</Button
		>
	</div>
	<!--
	<div class="mt-4 flex justify-center">
		<Button href="#" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Registrar Reabastecimiento</Button
		>
	</div>
	<div class="mt-4 flex justify-center">
		<Button href="#" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Consultar Lista de Reposición</Button
		>
	</div>
	<div class="mt-4 flex justify-center">
		<Button href="#" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Consultar Lista de Vencimiento</Button
		>
	</div>
	<div class="mt-4 flex justify-center">
		<Button href="#" size="lg" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Consultar Reportes</Button
		>
	</div>-->
</div>
