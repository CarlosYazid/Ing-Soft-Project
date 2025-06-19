<script lang="ts">
	import { Button } from '$lib/components/ui/button/index.js';
	import DataTable from '$lib/components/DataTable.svelte';
	import type { productForm } from '$lib';

	import { onMount } from 'svelte';
	let productMocks: Object[] = $state([]);
	let products = $derived(productMocks);

	const columns = [
		{ label: 'ID', field: 'id' },
		{ label: 'Nombre', field: 'name' },
		{ label: 'Categoria', field: 'category' },
		{ label: 'Precio', field: 'price' },
		{ label: 'Stock', field: 'stock' }
	];
	onMount(() => {
		let data = JSON.parse(localStorage.getItem('productos') || '[]');
		productMocks = data;

		products = productMocks.map((p: any) => ({
			id: p.id,
			name: p.productName,
			category: p.category,
			price: p.price,
			stock: p.stock
		}));
	});
</script>

<div class="mt-4 flex justify-end">
	<Button href="/gestionar-productos/add-product" size="lg" class="mr-4 mb-4"
		>Añadir nuevo producto</Button
	>
	<Button
		onclick={() => {
			productMocks = JSON.parse(localStorage.getItem('productos') || '[]');
		}}
		size="lg"
		class="mr-4 mb-4">Actualizar Estado</Button
	>
</div>
<div>
	{#key productMocks}
		<DataTable {columns} data={products} />
	{/key}
</div>
