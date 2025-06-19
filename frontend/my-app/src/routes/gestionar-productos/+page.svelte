<script lang="ts">
	import { onMount } from 'svelte';
	import { Button } from '$lib/components/ui/button/index.js';
	import DataTable from '$lib/components/DataTable.svelte';

	interface Product {
		id: number;
		productName: string;
		category: string;
		price: number;
		stock: number;
	}

	let productMocks: Product[] = $state([]);
	let products = $derived(productMocks);

	function getAll(): Product[] {
		const raw = localStorage.getItem('productos');
		return raw ? JSON.parse(raw) : [];
	}

	function saveAll(list: Product[]) {
		localStorage.setItem('productos', JSON.stringify(list));
	}

	function recargar() {
		productMocks = getAll();
	}

	onMount(() => {
		products = productMocks.map((p) => ({
			id: p.id,
			productName: p.productName,
			category: p.category,
			price: p.price,
			stock: p.stock
		}));
		recargar();
	});
</script>

<div class="mt-4 flex justify-end">
	<Button href="/gestionar-productos/add-product" size="lg" class="mr-4 mb-4">
		Añadir nuevo producto
	</Button>
	<Button onclick={recargar} size="lg" class="mr-4 mb-4">Actualizar Estado</Button>
</div>

<div>
	{#key productMocks}
		<DataTable
			columns={[
				{ label: 'ID', field: 'id' },
				{ label: 'Nombre', field: 'productName' },
				{ label: 'Categoria', field: 'category' },
				{ label: 'Precio', field: 'price' },
				{ label: 'Stock', field: 'stock' }
			]}
			data={products}
		/>
	{/key}
</div>
