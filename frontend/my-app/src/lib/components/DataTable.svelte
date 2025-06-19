<script lang="ts">
	export let columns: { label: string; field: string }[];
	export let data: any[];

	let sortField = '';
	let sortAsc = true;

	$: sortedData = [...data].sort((a, b) => {
		if (!sortField) return 0;
		const valA = a[sortField];
		const valB = b[sortField];

		// Comparar números
		if (typeof valA === 'number' && typeof valB === 'number') {
			return sortAsc ? valA - valB : valB - valA;
		}

		// Comparar strings
		if (typeof valA === 'string' && typeof valB === 'string') {
			return sortAsc ? valA.localeCompare(valB) : valB.localeCompare(valA);
		}

		// Comparar cualquier otro tipo (fallback)
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
</script>

<!-- Contenedor que llena toda la pantalla -->
<div class="flex h-screen w-full flex-col">
	<div class="flex-none border-b bg-gray-50 px-4 py-2 text-lg font-semibold">
		Lista de productos actuales
	</div>

	<!-- Contenedor scrollable de la tabla -->
	<div class="flex-1 overflow-y-scroll">
		<table class="min-w-full divide-y divide-gray-200 text-sm">
			<thead class="sticky top-0 z-10 bg-gray-100">
				<tr>
					{#each columns as column}
						<th
							class="cursor-pointer bg-gray-100 px-4 py-3 text-left font-semibold text-gray-700 hover:underline"
							on:click={() => toggleSort(column.field)}
						>
							{column.label}
							{#if sortField === column.field}
								{sortAsc ? ' ↑' : ' ↓'}
							{/if}
						</th>
					{/each}
				</tr>
			</thead>
			<tbody class="divide-y divide-gray-100 bg-white">
				{#each sortedData as row}
					<tr class="hover:bg-gray-50">
						{#each columns as column}
							<td class="px-4 py-2 whitespace-nowrap text-gray-800">
								{row[column.field]}
							</td>
						{/each}
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>
