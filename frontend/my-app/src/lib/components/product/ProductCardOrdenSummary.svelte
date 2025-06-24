<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import type { ProductInterface } from '$lib/types';
	export let product: ProductInterface;
	export let quantity: number;
	import { Button } from '$lib/components/ui/button/index.js';
	import { Trash2, ArrowUp, ArrowDown } from '@lucide/svelte';
	import Input from '../ui/input/input.svelte';
</script>

<Card.Root>
	<Card.Content>
		<div class="flex items-center justify-between gap-4">
			<img src={product.img} alt={product.name} class="h-auto w-30" />
			<div class="grid grid-cols-1 gap-2">
				<h3 class="text-2xl font-bold">{product.name}</h3>
				<p class="text-sm text-gray-500">{product.description}</p>
			</div>
			<div class="grid grid-cols-1 gap-2">
				<h3 class="text-base font-semibold">Precio Unitario</h3>
				<p class="text-sm text-gray-500">${product.price.toLocaleString()}</p>
			</div>
			<div class="grid grid-cols-1 gap-2">
				<h3 class="text-base font-semibold">Precio Total</h3>
				<p class="text-sm font-semibold">${(product.price * quantity).toLocaleString()}</p>
			</div>
			<Input type="number" bind:value={quantity} class="w-15" />

			<Button class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button>
		</div>
		<p class="flex justify-end text-sm text-gray-500">Stock: {product.stock - quantity}</p>
	</Card.Content>
</Card.Root>
