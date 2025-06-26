<script lang="ts">
	import { goto } from '$app/navigation';
</script>

<div
	class="flex min-h-screen items-center justify-center bg-gradient-to-br from-green-100 to-green-300 p-6"
>
	<div class="max-w-md rounded-2xl bg-white p-8 text-center shadow-2xl">
		<h1 class="mb-4 text-4xl font-extrabold text-green-700">¡Felicidades por tu compra!</h1>
		<p class="mb-8 text-gray-600">
			Gracias por confiar en nosotros. Tu pedido se ha procesado correctamente.
		</p>
		<button
			on:click={() => goto('/')}
			class="rounded-xl bg-green-600 px-6 py-2 font-semibold text-white shadow-md transition hover:bg-green-700"
		>
			Continuar
		</button>
	</div>
</div>
