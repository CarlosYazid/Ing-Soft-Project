<script lang="ts">
	import type { ProductInterface } from '$lib/types';
	import * as Card from '$lib/components/ui/card/index.js';
	import Input from '$lib/components/ui/input/input.svelte';
	import { Button } from '$lib/components/ui/button/index.js';
	import { ShoppingBasket } from '@lucide/svelte';
	import SuccessOrFailDialog from '../common/SuccessOrFailDialog.svelte';

	import { cartStore } from '$lib';

	let product = $state(cartStore.productSelected);
	if (product) {
		product.quantity = product?.quantity! | 0;
	}
</script>

<div class="flex h-full flex-col items-center justify-center px-8">
	<Card.Root>
		<Card.Content>
			{#if product}
				<div class="flex items-center justify-between gap-4 space-x-4">
					<div>
						<img class="max-w-base rounded-lg" src={product.img as string} alt={product.name} />
					</div>
					<div class="flex flex-col items-start justify-between gap-4">
						<h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
							{product.name}
						</h5>
						<p class="font-normal text-gray-700 dark:text-gray-400">ID: {product.id}</p>
						<p class="font-normal text-gray-700 dark:text-gray-400">
							{product.description}
						</p>
						<p class="font-semibold text-gray-900 dark:text-white">
							Precio Unitario: ${product.price}
						</p>
						<p class="font-semibold text-gray-900 dark:text-white">
							Precio Total: ${(product.price * product.quantity!).toLocaleString()}
						</p>
						<Input
							type="number"
							bind:value={product.quantity}
							class="w-18"
							min="1"
							max={product.stock}
						/>
						<Button
							onclick={() => {
								cartStore.addProduct(product);
							}}
							class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
							>Agregar a la Lista de Venta Actual <ShoppingBasket /></Button
						>
						<p class="font-normal text-gray-700 dark:text-gray-400">
							Stock: {product.stock - product.quantity!}
						</p>
					</div>
				</div>
			{:else}
				<p>Ha ocurrido un error, por favor vuelve a seleccionar un producto</p>
			{/if}
		</Card.Content>
	</Card.Root>
</div>

{#if product?.quantity! > product?.stock! || product?.quantity! < 0}
	<SuccessOrFailDialog
		infoDialog={false}
		contentDialog={'La cantidad ingresada no puede ser procesada'}
		callback={() => (product!.quantity = product?.stock)}
	/>
{/if}
