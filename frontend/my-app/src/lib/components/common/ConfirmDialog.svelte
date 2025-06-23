<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog/index.js';

	let open = $state(true);

	const { callbackOnTrue, callbackOnFalse, title, description, action, btnClass } = $props();

	function handleContinue() {
		callbackOnTrue();
		open = false;
	}
</script>

<AlertDialog.Root bind:open>
	<AlertDialog.Content>
		<div class="flex h-full flex-col items-center justify-center">
			<AlertDialog.Header>
				<AlertDialog.Title>{title}</AlertDialog.Title>
				<AlertDialog.Description>
					{description}
				</AlertDialog.Description>
			</AlertDialog.Header>
			<AlertDialog.Footer>
				<AlertDialog.Cancel onclick={callbackOnFalse}>Cancelar</AlertDialog.Cancel>
				<AlertDialog.Action onclick={handleContinue} class={btnClass}>{action}</AlertDialog.Action>
			</AlertDialog.Footer>
		</div>
	</AlertDialog.Content>
</AlertDialog.Root>
