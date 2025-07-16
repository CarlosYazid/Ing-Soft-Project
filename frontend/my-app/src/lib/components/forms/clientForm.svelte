<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
	import { toast, Toaster } from 'svelte-sonner';
	import { goto } from '$app/navigation';

	import type { client } from '$lib/types';
	import { clientStore, cartStore } from '$lib/store';
	import { clientController } from '$lib/controllers';
	import { validateClientForm } from '$lib/utils/';

	// — Estados locales —
	let current = false; /*clientStore.editClient; Implementar en un futuro*/
	let documentid = $state(/* current?.documentid?.toString() ?? */ '');
	let name = $state(/* current?.name ?? */ '');
	let email = $state(/* current?.email ?? */ '');
	let phone = $state(/* current?.phone ?? */ '');

	let formErrors = $state<{ documentid?: string; name?: string; email?: string; phone?: string }>(
		{}
	);

	async function handleSubmit(e: Event) {
		e.preventDefault();

		const formData = {
			id: 0,
			documentid: parseInt(documentid),
			name: name.trim(),
			email: email.trim(),
			phone: phone.trim()
		};

		console.log(formData);

		// Validación de campos
		formErrors = {};
		if (!validateClientForm(formData, formErrors)) {
			toast.error('Por favor corrige los errores en el formulario.');
			return;
		}

		try {
			let saved: client;
			if (false) {
				/* saved = await clientController.updateClient(current.documentid, formData);
				clientStore.clearEditClient();
				toast.success('Cliente actualizado correctamente'); */
			} else {
				console.log('Hola');
				saved = await clientController.createClient(formData);
				/* clientStore.addClient(saved); // Esto pa que hptas si igual estoy sobreescribiendo esto con la info del server */
				toast.success('Cliente registrado correctamente');
			}
			clientStore.clients = await clientController.getAllClients();
			cartStore.client = saved;
		} catch (err) {
			console.error(err);
			toast.error('Error al guardar el cliente. Intenta de nuevo.');
		}

		handleCancel() //Ejecutamos esa misma lógica para regresar a la page correspondiente
	}

	function handleCancel() {
		goto(
			clientStore.addingClient || clientStore.editClient
				? '/gestionar-clientes'
				: '/new-sale/confirm-sale'
		);
		clientStore.clearEditClient();
		clientStore.addingClient = false;
	}

	$inspect(clientStore.clients);
</script>

<Toaster />

<form onsubmit={handleSubmit} class="mx-auto grid max-w-md grid-cols-1 gap-4 space-y-4 p-4">
	<h3 class="text-2xl font-bold">
		{#if current}Editar Cliente{:else}Registrar Nuevo Cliente{/if}
	</h3>

	<!-- Documento de Identificación -->
	<div class="space-y-1">
		<Label for="documentid">Documento de Identificación</Label>
		<Input id="documentid" type="text" bind:value={documentid} placeholder="C.C." required />
		{#if formErrors.documentid}
			<p class="text-sm text-red-600">{formErrors.documentid}</p>
		{/if}
	</div>

	<!-- Nombre Completo -->
	<div class="space-y-1">
		<Label for="name">Nombre Completo</Label>
		<Input id="name" type="text" bind:value={name} placeholder="Nombre completo" required />
		{#if formErrors.name}
			<p class="text-sm text-red-600">{formErrors.name}</p>
		{/if}
	</div>

	<!-- Número Telefónico -->
	<div class="space-y-1">
		<Label for="phone">Número Telefónico</Label>
		<Input id="phone" type="text" bind:value={phone} placeholder="Ej. 3001234567" required />
		{#if formErrors.phone}
			<p class="text-sm text-red-600">{formErrors.phone}</p>
		{/if}
	</div>

	<!-- Email -->
	<div class="space-y-1">
		<Label for="email">Correo Electrónico</Label>
		<Input id="email" type="email" bind:value={email} placeholder="cliente@ejemplo.com" required />
		{#if formErrors.email}
			<p class="text-sm text-red-600">{formErrors.email}</p>
		{/if}
	</div>

	<!-- Botones -->
	<div class="mt-4 flex justify-between">
		<Button type="submit" class="bg-blue-600 hover:bg-blue-700">
			{#if current}Actualizar{:else}Registrar{/if}
		</Button>
		<Button type="button" class="bg-gray-500 hover:bg-gray-600" onclick={handleCancel}>
			Cancelar
		</Button>
	</div>
</form>
