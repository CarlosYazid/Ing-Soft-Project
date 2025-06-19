<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';

	let open = $state(true);

	const { callback, parametro } = $props();

	function handleContinue() {
		callback(parametro);
		open = false;
	}
</script>

<AlertDialog.Root bind:open>
	<AlertDialog.Content>
		<div class="flex h-full flex-col items-center justify-center">
			<AlertDialog.Header>
				<AlertDialog.Title>¿Está seguro que desea eliminar el producto?</AlertDialog.Title>
				<AlertDialog.Description>
					Esta acción no se puede deshacer. El producto será eliminado permanentemente.
				</AlertDialog.Description>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Cancel>Cancelar</AlertDialog.Cancel>
				<AlertDialog.Action
					onclick={handleContinue}
					class="bg-red-700 hover:bg-red-300 hover:text-red-700">Eliminar</AlertDialog.Action
				>
			</AlertDialog.Footer>
		</div>
	</AlertDialog.Content>
</AlertDialog.Root>
