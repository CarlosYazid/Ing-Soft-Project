<script>
	const { infoDialog, contentDialog, callback } = $props();
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';
</script>

<AlertDialog.Root open={true}>
	<AlertDialog.Content>
		{#if infoDialog}
			<AlertDialog.Header>
				<AlertDialog.Title>Operación Realizada Exitosamente</AlertDialog.Title>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Action class="bg-green-700 hover:bg-green-500" onclick={callback}
					>Aceptar</AlertDialog.Action
				>
			</AlertDialog.Footer>
		{:else}
			<AlertDialog.Header>
				<AlertDialog.Title>Ha Ocurrido un Error</AlertDialog.Title>
				<AlertDialog.Description>
					{contentDialog}
				</AlertDialog.Description>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Action class="bg-red-700 hover:bg-red-500" onclick={callback}
					>Aceptar</AlertDialog.Action
				>
			</AlertDialog.Footer>
		{/if}
	</AlertDialog.Content>
</AlertDialog.Root>
