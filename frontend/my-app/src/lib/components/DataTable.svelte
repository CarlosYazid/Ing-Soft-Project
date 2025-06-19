<script lang="ts">
	export let columns: { label: string; field: string }[] = [];
	export let data: any[] = [];

	let sortField = '';
	let sortAsc = true;

	$: sortedData = [...data].sort((a, b) => {
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

	function toggleSort(field: string) {
		if (sortField === field) {
			sortAsc = !sortAsc;
		} else {
			sortField = field;
			sortAsc = true;
		}
	}

	function onEdit(row: any) {
		console.log('Editar:', row);
	}

	function onDelete(row: any) {
		console.log('Eliminar:', row);
	}
</script>

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
							on:click={() => toggleSort(column.field)}
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
									on:click={() => (row.showMenu = !row.showMenu)}
								>
									⋮
								</button>

								{#if row.showMenu}
									<div
										class="absolute right-0 z-20 mt-1 w-32 rounded border bg-white shadow-md"
										on:mouseleave={() => (row.showMenu = false)}
									>
										<button
											class="block w-full px-4 py-2 text-left text-sm text-gray-700 hover:bg-gray-100"
											on:click={() => onEdit(row)}
										>
											Editar
										</button>
										<button
											class="block w-full px-4 py-2 text-left text-sm text-red-600 hover:bg-red-100"
											on:click={() => onDelete(row)}
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
