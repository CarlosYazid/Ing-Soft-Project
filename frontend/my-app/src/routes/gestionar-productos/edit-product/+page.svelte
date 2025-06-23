<script>
	import AddProductForm from '$lib/components/product/AddProductForm.svelte';
	import EditProductForm from '$lib/components/product/EditProductForm.svelte';
</script>

<div class="flex justify-center">
	<AddProductForm
		product={{
			id: 1,
			productName: 'Cuaderno',
			description: 'Hola',
			cost: 1000,
			price: 2000,
			category: 'Comestible',
			stock: 20,
			picture: null
		}}
	/>
</div>
