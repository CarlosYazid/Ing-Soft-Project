<script lang="ts">
	import ServiceForm from '$lib/components/forms/ServiceForm.svelte';
	import { inventory } from '$lib/store';
	import { productController } from '$lib';
	import type { ProductInterface } from '$lib';
	import ProductCardSelectProducts from '$lib/components/product/ProductCardSelectProducts.svelte';
	import { toast, Toaster } from 'svelte-sonner';

	import { onMount } from 'svelte';

	let productsInventory: ProductInterface[] = $derived(inventory.products);
	$inspect(productsInventory);

	onMount(async () => {
		try {
			const fetchedProducts = await productController.getAll();
			inventory.products = fetchedProducts;
		} catch (e: any) {
			toast('Algo ha salido mal', {
				description: e.message || 'No se han podido cargar los productos',
				action: {
					label: 'Aceptar',
					onClick: () => console.info('Aceptar')
				}
			});
		}
	});
</script>

<Toaster />
<ServiceForm />

<div class="grid grid-cols-[repeat(auto-fit,minmax(300px,375px))] justify-center gap-4 px-10">
	{#each productsInventory as product (product.id)}
		<ProductCardSelectProducts product={{ ...product }} />
	{/each}
</div>
