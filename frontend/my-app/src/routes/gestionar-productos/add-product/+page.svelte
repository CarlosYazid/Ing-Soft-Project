<script>
	import AddProductForm from '$lib/components/product/AddProductForm.svelte';
</script>

<div class="flex justify-center">
	<AddProductForm
		form={{
			id: 0,
			productName: '',
			description: '',
			cost: 0,
			price: 0,
			category: '',
			stock: 0,
			picture: null
		}}
	/>
</div>
