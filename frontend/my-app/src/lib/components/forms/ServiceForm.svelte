<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button';
	import { toast, Toaster } from 'svelte-sonner';
	import { goto } from '$app/navigation';

	import type { service, serviceFormInput } from '$lib/types';
	import { serviceStore } from '$lib/store';
	import * as serviceController from '$lib/controllers';
	import { validateServiceForm } from '$lib/utils/servicios';

	// --- Estados locales ---
	let current = serviceStore.editService;
	let name = $state(current?.name || '');
	let price = $state(current?.price?.toString() || '');

	let formErrors = $state<{ name?: string; price?: string }>({});

	async function handleSubmit(e: Event) {
		e.preventDefault();

		const serviceFormData: serviceFormInput = {
			name: name,
			price: price
		};

		if (!validateServiceForm(serviceFormData)) {
			toast.error('Corrige los errores en el formulario.');
			return;
		}

		const payload: service = {
			id: current?.id || 0,
			name: serviceFormData.name.trim(),
			price: parseFloat(serviceFormData.price)
		};

		try {
			let saved: service;
			if (current) {
				saved = await serviceController.updateService(current.id, payload);
				serviceStore.services = await serviceController.getAllServices();
				serviceStore.clearEditService();
				toast.success('Servicio actualizado correctamente');
			} else {
				saved = await serviceController.createService(payload);
				serviceStore.addService(saved);
				toast.success('Servicio creado correctamente');
			}
			goto('/gestionar-servicios');
		} catch (err) {
			console.error(err);
			toast.error('Error al guardar el servicio. Intenta de nuevo.');
		}
	}

	function handleCancel() {
		serviceStore.clearEditService();
		goto('/gestionar-servicios');
	}
</script>

<Toaster />

<form onsubmit={handleSubmit} class="mx-auto max-w-md space-y-4 p-4">
	<!-- Nombre -->
	<div class="space-y-1">
		<Label for="name">Nombre del servicio</Label>
		<Input id="name" type="text" bind:value={name} placeholder="Ej. Consultoría" required />
		{#if formErrors.name}
			<p class="text-sm text-red-600">{formErrors.name}</p>
		{/if}
	</div>

	<!-- Precio -->
	<div class="space-y-1">
		<Label for="price">Precio</Label>
		<div class="flex items-center gap-2">
			<span class="text-gray-500 select-none">$</span>
			<Input
				id="price"
				type="text"
				bind:value={price}
				placeholder="0.00"
				inputmode="decimal"
				required
			/>
			<span class="text-gray-500 select-none">COP</span>
		</div>
		{#if formErrors.price}
			<p class="text-sm text-red-600">{formErrors.price}</p>
		{/if}
	</div>

	<!-- Botones -->
	<div class="mt-4 flex justify-between">
		<Button type="submit" class="bg-blue-600 hover:bg-blue-700">
			{current ? 'Actualizar' : 'Crear'}
		</Button>
		<Button type="button" class="bg-gray-500 hover:bg-gray-600" onclick={handleCancel}>
			Cancelar
		</Button>
	</div>
</form>
