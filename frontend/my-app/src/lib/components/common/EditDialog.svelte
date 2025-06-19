<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';
	import Button from '../ui/button/button.svelte';
</script>

<AlertDialog.Root open={true}>
	<AlertDialog.Content>
		<div class="flex h-full flex-col items-center justify-center">
			<AlertDialog.Header>
				<AlertDialog.Title>¿Está seguro que desea editar el producto?</AlertDialog.Title>
				<AlertDialog.Description></AlertDialog.Description>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Cancel>Cancelar</AlertDialog.Cancel>
				<Button
					href="/gestionar-productos/edit-product"
					class=" bg-blue-700 hover:bg-blue-300 hover:text-blue-700">Confirmar</Button
				>
			</AlertDialog.Footer>
		</div>
	</AlertDialog.Content>
</AlertDialog.Root>
