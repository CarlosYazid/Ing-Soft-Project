<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import DataTable from '$lib/components/DataTable.svelte';

	const columns = [
		{ label: 'ID', field: 'id' },
		{ label: 'Nombre', field: 'name' },
		{ label: 'Categoria', field: 'category' },
		{ label: 'Precio', field: 'price' },
		{ label: 'Stock', field: 'stock' }
	];

	const users = [
		{ id: 1, name: 'Producto A', category: 'Categoria 1', price: '$10.00', stock: 100 },
		{ id: 2, name: 'Producto B', category: 'Categoria 2', price: '$20.00', stock: 50 },
		{ id: 3, name: 'Producto C', category: 'Categoria 1', price: '$15.00', stock: 75 },
		{ id: 4, name: 'Producto D', category: 'Categoria 3', price: '$30.00', stock: 20 },
		{ id: 5, name: 'Producto E', category: 'Categoria 2', price: '$25.00', stock: 10 }
	];
</script>

<Button href="/gestionar-productos" size="lg" class="fixed top-4 right-4 px-4 py-2"
	>Añadir nuevo producto</Button
>
<DataTable {columns} data={users} />
