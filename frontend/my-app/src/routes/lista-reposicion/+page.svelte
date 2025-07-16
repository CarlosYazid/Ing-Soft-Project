<script lang="ts">
	import ConfirmDialog from '$lib/components/common/ConfirmDialog.svelte';
	import type { ProductInterface, ProductRow } from '$lib/types';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Table from '$lib/components/ui/table/index.js';
	import { Plus } from '@lucide/svelte';
	import { inventory } from '$lib/store/index';
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { toast, Toaster } from 'svelte-sonner';
	import { productController } from '$lib/controllers';
	import * as Dialog from '$lib/components/ui/dialog/index.js';
	import { Input } from '$lib/components/ui/input/index.js';

	let productsInventory: ProductInterface[] = $derived(inventory.products);

	let products: ProductRow[] = $derived(
		productsInventory.map((p) => ({
			id: p.id,
			name: p.name,
			category: p.category,
			price: p.price,
			stock: p.stock
		}))
	);

	// Gestionar lógica sort
	const columns = [
		{ title: 'ID', key: 'id' },
		{ title: 'Nombre', key: 'name' },
		{ title: 'Precio', key: 'price' },
		{ title: 'Stock', key: 'stock' }
	];

	let sortAsc = $state(true);

	function toggleSort() {
		sortAsc = !sortAsc;

		products = [...products].sort((a, b) => {
			const valA = a.stock;
			const valB = b.stock;

			if (typeof valA === 'number' && typeof valB === 'number') {
				return sortAsc ? valA - valB : valB - valA;
			}
			return 0;
		});
	}

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

<div class="px-8">
	<h3 class="font-semiboldc mt-8 bg-zinc-500/15 p-4 text-lg">Lista de Productos con Stock Bajo</h3>
	{#key productsInventory}
		<Table.Root>
			<Table.Caption>Productos Actuales en la Base de Datos</Table.Caption>
			<Table.Header class="bg-zinc-500/10">
				<Table.Row>
					{#each columns as column (column.key)}
						{#if column.key === 'stock'}
							<Table.Head onclick={() => toggleSort()} class="p-4">
								{column.title}

								{sortAsc ? ' ↓' : ' ↑'}
							</Table.Head>
						{:else}
							<Table.Head class="p-4">
								{column.title}
							</Table.Head>
						{/if}
					{/each}
					<Table.Head class="p-4"></Table.Head>
				</Table.Row>
			</Table.Header>
			<Table.Body>
				{#each products as product (product.id)}
					<Table.Row>
						<Table.Cell class="p-4">{product.id}</Table.Cell>
						<Table.Cell class="p-4">{product.name}</Table.Cell>
						<Table.Cell class="p-4">{product.price}</Table.Cell>
						<Table.Cell class="p-4 text-red-700">{product.stock}</Table.Cell>
						<Table.Cell
							><Dialog.Root>
								<Dialog.Trigger
									><Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
										><Plus /></Button
									></Dialog.Trigger
								>
								<Dialog.Content>
									<Dialog.Header>
										<Dialog.Title
											>¿Cuántos productos se han recibido para incorporar al stock?</Dialog.Title
										>
										<Dialog.Description>
											<div class="grid grid-cols-3 gap-4">
												<Input class="col-span-2" />
												<Button class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
													>Guardar</Button
												>
											</div>
										</Dialog.Description>
									</Dialog.Header>
								</Dialog.Content>
							</Dialog.Root>
						</Table.Cell>
					</Table.Row>
				{/each}
			</Table.Body>
		</Table.Root>
	{/key}
</div>
