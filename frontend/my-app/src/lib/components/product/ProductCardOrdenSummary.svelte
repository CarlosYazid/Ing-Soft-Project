<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import type { ProductInterface } from '$lib/types';
	import { Button } from '$lib/components/ui/button/index.js';
	import { Trash2 } from '@lucide/svelte';
	import Input from '../ui/input/input.svelte';
	import SuccessOrFailDialog from '../common/SuccessOrFailDialog.svelte';

	import { cartStore } from '$lib';

	let {
		product = $bindable(),
		deleteButton,
		onServiceCard
	} = $props<{
		product: ProductInterface;
		deleteButton: boolean;
		onServiceCard: boolean;
	}>();
</script>

{#if product}
	<Card.Root>
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
					<p class="text-sm font-semibold">
						${(
							product.price * (onServiceCard ? product.quantityService! : product.quantity!)
						).toFixed(2)}
					</p>
				</div>

				{#if deleteButton}
					<Input
						type="number"
						bind:value={product.quantity}
						class="w-18"
						min="1"
						max={product.stock - product.quantityService!}
					/>
					<Button
						onclick={() => cartStore.removeProductById(product.id)}
						class="bg-red-700 hover:bg-red-300 hover:text-red-700"><Trash2 /></Button
					>
				{:else}
					<Input
						type="number"
						bind:value={product.quantityService}
						class="w-18"
						min="0"
						max={product.stock - product.quantity!}
					/>
				{/if}
			</div>
			<p class="flex justify-end text-sm text-gray-500">
				Stock: {product.stock - product.quantity! - product.quantityService!}
			</p>
		</Card.Content>
	</Card.Root>

	{#if product?.quantity! > product?.stock! || product?.quantity! < 0 || product?.quantity % 1 !== 0}
		<SuccessOrFailDialog
			infoDialog={false}
			contentDialog={`La cantidad ingresada no puede ser procesada ${
				product?.quantity! > product?.stock! ? ': El stock disponible es insuficiente' : ''
			}`}
			callback={() => {
				product!.quantity = product?.stock;
			}}
		/>
	{/if}

	{#if product?.quantityService! > product?.stock! || product?.quantityService! < 0 || product.quantityService % 1 !== 0}
		<SuccessOrFailDialog
			infoDialog={false}
			contentDialog={`La cantidad ingresada no puede ser procesada ${
				product?.quantityService! > product?.stock! ? ': El stock disponible es insuficiente' : ''
			}`}
			callback={() => {
				product!.quantityService = product?.stock;
			}}
		/>
	{/if}
{/if}
