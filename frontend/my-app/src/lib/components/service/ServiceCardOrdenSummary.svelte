<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import type { ProductInterface, service } from '$lib/types';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Trash2 } from '@lucide/svelte';
	import Input from '../ui/input/input.svelte';
	import SuccessOrFailDialog from '../common/SuccessOrFailDialog.svelte';
	import ProductCardOrdenSummary from '$lib/components/product/ProductCardOrdenSummary.svelte';
	import { cartStore, inventory } from '$lib';

	let { Service = $bindable() } = $props<{
		Service: service;
	}>();

	Service.products = Service.products!.map((p: ProductInterface) =>
		inventory.findProductById(p.id)
	);
</script>

<Card.Root>
	<Card.Header>
		<div class="flex items-center justify-between gap-4">
			<div class="grid grid-cols-1 gap-2">
				<p class="text-3xl font-bold">{Service.name}</p>
				<p class="text-base text-gray-500">
					Precio fijo: ${Service.price}
				</p>
			</div>
			<div class="grid grid-cols-1 gap-2">
				<p class="text-xl font-semibold">Precio Total</p>
				<p class="text-lg font-semibold">
					${Service.products?.reduce(
						(acc: number, p: ProductInterface) =>
							acc + p.quantityService! * p.price + p.quantityService! * Service.price,
						0
					)}
				</p>
			</div>
			<Button
				onclick={() => {
					cartStore.removeServiceById(Service.id);
					Service.products.forEach((p: ProductInterface) => {
						inventory.findProductById(p.id)!.quantityService = 0;
					});
				}}
				class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
			>
		</div>
	</Card.Header>
	<Card.Content>
		<div class="mt-4 grid grid-cols-1 gap-4">
			{#each Service.products as product, i (product.id)}
				<ProductCardOrdenSummary
					bind:product={Service.products[i]}
					deleteButton={false}
					onServiceCard={true}
				/>
			{/each}
		</div>
	</Card.Content>
	<Card.Footer>
		<p></p>
	</Card.Footer>
</Card.Root>
