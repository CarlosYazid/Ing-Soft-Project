<script>
	const { infoDialog, contentDialog } = $props();
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';
</script>

<AlertDialog.Root open={true}>
	<AlertDialog.Content>
		{#if infoDialog}
			<AlertDialog.Header>
				<AlertDialog.Title>Operación Realizada Exitosamente</AlertDialog.Title>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Cancel class="bg-green-400">Aceptar</AlertDialog.Cancel>
			</AlertDialog.Footer>
		{:else}
			<AlertDialog.Header>
				<AlertDialog.Title>Ha Ocurrido un Error</AlertDialog.Title>
				<AlertDialog.Description>
					{contentDialog}
				</AlertDialog.Description>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Cancel class="bg-red-400">Aceptar</AlertDialog.Cancel>
			</AlertDialog.Footer>
		{/if}
	</AlertDialog.Content>
</AlertDialog.Root>
