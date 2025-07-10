<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import type { ProductInterface, service } from '$lib/types';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Trash2 } from '@lucide/svelte';
	import Input from '../ui/input/input.svelte';
	import SuccessOrFailDialog from '../common/SuccessOrFailDialog.svelte';

	import { cartStore } from '$lib';

	let { Service = $bindable() } = $props<{
		Service: service;
	}>();
</script>

<!-- <Card.Root>
	<Card.Content>
		<div class="flex items-center justify-between gap-4">
			<img src={product.img as string} alt={product.name} class="h-auto w-30" />
			<div class="grid grid-cols-1 gap-2">
				<h3 class="text-2xl font-bold">{product.name}</h3>
				<p class="text-sm text-gray-500">{product.short_description}</p>
			</div>
			<div class="grid grid-cols-1 gap-2">
				<h3 class="text-base font-semibold">Precio Unitario</h3>
				<p class="text-sm text-gray-500">${product.price}</p>
			</div>
			<div class="grid grid-cols-1 gap-2">
				<h3 class="text-base font-semibold">Precio Total</h3>
				<p class="text-sm font-semibold">${(product.price * product.quantity!).toFixed(2)}</p>
			</div>
			<Input type="number" bind:value={product.quantity} class="w-18" min="1" max={product.stock} />

			<Button
				onclick={() => cartStore.removeProductById(product.id)}
				class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
			>
		</div>
		<p class="flex justify-end text-sm text-gray-500">Stock: {product.stock - product.quantity!}</p>
	</Card.Content>
</Card.Root>

{#if product?.quantity! > product?.stock! || product?.quantity! < 0}
	<SuccessOrFailDialog
		infoDialog={false}
		contentDialog={'La cantidad ingresada no puede ser procesada'}
		callback={() => (product!.quantity = product?.stock)}
	/>
{/if}
 -->
