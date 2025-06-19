<script lang="ts">
	import ConfirmDialog from './common/ConfirmDialog.svelte';
	import EditDialog from './common/EditDialog.svelte';
	import * as Table from '$lib/components/ui/table/index.js';
	import type { productForm } from './types';

	let { columns, data } = $props();	

	let sortField = $state('');
	let sortAsc = $state(true);

	let sortedData = $state.raw(data);

	function toggleSort(field: string) {
		if (sortField === field) {
			sortAsc = !sortAsc;
		} else {
			sortField = field;
			sortAsc = true;
		}

		sortedData = [...data].sort((a, b) => {
			if (!sortField) return 0;
			const valA = a[sortField];
			const valB = b[sortField];

			if (typeof valA === 'number' && typeof valB === 'number') {
				return sortAsc ? valA - valB : valB - valA;
			}
			if (typeof valA === 'string' && typeof valB === 'string') {
				return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
			}
			return 0;
		});
	}

	let fila = $state({});

	let editar = $state(false);
	function onEdit(row: any) {
		saveEditProduct(row);
		editar = true;
	}

	let eliminar = $state(false);
	function onDelete(row: any) {
		eliminar = true;
		fila = row;
	}

	function saveEditProduct(product: any): void {
		localStorage.setItem('editProduct', JSON.stringify(product));
		const raw = localStorage.getItem('products');
		if (!raw) return;
		console.log(raw);
		const products: productForm[] = JSON.parse(raw);
		const filtered = products.filter((p) => Number(p.id) !== Number(product.id));
		console.log(filtered);

		localStorage.setItem('products', JSON.stringify(filtered));
	}

	function confirmedDelete(row: any) {
		const productos = JSON.parse(localStorage.getItem('productos')!);

		const productosFiltrados = productos.filter((p: any) => p.id !== row.id);

		localStorage.setItem('productos', JSON.stringify(productosFiltrados));
	}
</script>

{#key sortedData}
	<div class="flex w-full flex-col">
		<div class="flex-none border-b bg-gray-50 px-4 py-2 text-lg font-semibold">
			Lista de productos actuales
		</div>

		<div class="flex-1 overflow-y-auto">
			<table class="min-w-full divide-y divide-gray-200 text-sm">
				<thead class="sticky top-0 z-10 bg-gray-100">
					<tr>
						{#each columns as column}
							<th
								class="cursor-pointer px-4 py-3 text-left font-semibold text-gray-700 hover:underline"
								onclick={() => toggleSort(column.field)}
							>
								{column.label}
								{#if sortField === column.field}
									{sortAsc ? ' ↑' : ' ↓'}
								{/if}
							</th>
						{/each}
						<th class="px-4 py-3 text-left text-gray-500"></th>
					</tr>
				</thead>
				<tbody class="divide-y divide-gray-100 bg-white">
					{#each sortedData as row (row.id)}
						<tr class="hover:bg-gray-50">
							{#each columns as column}
								<td class="px-4 py-2 whitespace-nowrap text-gray-800">
									{row[column.field]}
								</td>
							{/each}
							<td class="px-4 py-2 whitespace-nowrap">
								<!-- Simple Dropdown Menu por fila -->
								<div class="relative">
									<button
										class="rounded px-2 py-1 text-gray-600 hover:bg-gray-100"
										onclick={() => (row.showMenu = !row.showMenu)}
									>
										⋮
									</button>

									{#if row.showMenu}
										<div
											class="absolute right-0 z-20 mt-1 w-32 rounded border bg-white shadow-md"
											onmouseleave={() => (row.showMenu = false)}
										>
											<button
												class="block w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100"
												onclick={() => onEdit(row)}
											>
												Editar
											</button>
											<button
												class="block w-full px-4 py-2 text-left text-sm text-red-600 hover:bg-red-100"
												onclick={() => onDelete(row)}
											>
												Eliminar
											</button>
										</div>
									{/if}
								</div>
							</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>
{/key}

{#key eliminar}
	{#if eliminar}
		<ConfirmDialog parametro={fila} callback={confirmedDelete} />
	{/if}
{/key}

{#key editar}
	{#if editar}
		<EditDialog />
	{/if}
{/key}
