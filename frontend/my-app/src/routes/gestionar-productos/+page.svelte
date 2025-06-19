<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import DataTable from '$lib/components/DataTable.svelte';
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';

	const columns = [
		{ label: 'ID', field: 'id' },
		{ label: 'Nombre', field: 'name' },
		{ label: 'Categoria', field: 'category' },
		{ label: 'Precio', field: 'price' },
		{ label: 'Stock', field: 'stock' }
	];

	let products = [
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
	<Button href="/gestionar-productos" size="lg" class="mr-4 mb-4">Añadir nuevo producto</Button>
</div>
<div>
	<DataTable {columns} data={products} />
</div>
