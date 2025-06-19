<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import ChevronsUpDownIcon from '@lucide/svelte/icons/chevrons-up-down';
	import { cn } from '$lib/utils';

	import {
		FormField,
		FormControl,
		FormLabel,
		FormDescription,
		FormFieldErrors,
		FormButton
	} from '$lib/components/ui/form';

	let value = $state('');
	let open = $state(false);
	let triggerRef: HTMLButtonElement | null = $state(null);

	const categories = [
		{ value: 'papeleria', label: 'Papelería' },
		{ value: 'comestible', label: 'Comestible' }
	];

	const selectedValue = categories.find((c) => c.value === value)?.label ?? '';

	function closeAndFocusTrigger() {
		open = false;
		triggerRef?.focus();
	}

	/*Lógica de formulario*/
	import { enhance } from '$app/forms';
	import { type SuperValidated, type Infer, superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import { type ProductSchema, productSchema } from '$lib/components/types';

	let { data }: { data: { form: SuperValidated<Infer<ProductSchema>> } } = $props();

	const form = superForm(data.form, {
		validators: zodClient(productSchema)
	});

	const { form: formData } = form;
</script>

<form method="POST" use:enhance class="w-sm md:w-md">
	<div class="flex flex-col gap-6">
		<FormField {form} name="productName">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Nombre de Producto</FormLabel>
					<Input
						type="text"
						placeholder="Compás"
						required
						{...props}
						bind:value={$formData.productName}
					/>
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>

		<FormField {form} name="description">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Descripción de Producto</FormLabel>
					<Input
						type="text"
						placeholder="Compás metálico con rueda de precisión de marca Mapped"
						required
						{...props}
						bind:value={$formData.description}
					/>
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>

		<FormField {form} name="cost">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Costo de Compra</FormLabel>
					<div class="flex items-center gap-1">
						<div class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</div>
						<Input type="text" placeholder="0.00" required {...props} bind:value={$formData.cost} />
						<Input value="COP" class="w-16" disabled />
					</div>
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>

		<FormField {form} name="price">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Precio de Venta</FormLabel>
					<div class="flex items-center gap-1">
						<div class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</div>
						<Input
							type="text"
							placeholder="0.00"
							required
							{...props}
							bind:value={$formData.price}
						/>
						<Input value="COP" class="w-16" disabled />
					</div>
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>

		<FormField {form} name="category">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Categoría</FormLabel>
					<Popover.Root bind:open>
						<Popover.Trigger bind:ref={triggerRef}>
							<FormButton
								{...props}
								variant="outline"
								class="w-full justify-between"
								role="combobox"
								aria-expanded={open}
							>
								{selectedValue || 'Selecciona una Categoría...'}
								<ChevronsUpDownIcon class="opacity-50" />
							</FormButton>
						</Popover.Trigger>
						<Popover.Content class="w-sm p-0 md:w-md">
							<Command.Root class="w-sm md:w-md">
								<Command.Input placeholder="Buscar Categoría..." />
								<Command.List>
									<Command.Empty>Categoría no encontrada</Command.Empty>
									<Command.Group value="categories">
										{#each categories as category (category.value)}
											<Command.Item
												value={category.value}
												onSelect={() => {
													value = category.value;
													$formData.category = category.value;
													closeAndFocusTrigger();
												}}
											>
												<CheckIcon class={cn(value !== category.value && 'text-transparent')} />
												{category.label}
											</Command.Item>
										{/each}
									</Command.Group>
								</Command.List>
							</Command.Root>
						</Popover.Content>
					</Popover.Root>
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>

		<FormField {form} name="stock">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Cantidad a ingresar</FormLabel>
					<Input type="text" placeholder="20" required {...props} bind:value={$formData.stock} />
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>

		<FormField {form} name="picture">
			<FormControl>
				{#snippet children({ props })}
					<FormLabel>Imagen de Producto</FormLabel>
					<Input type="file" {...props} bind:files={$formData.picture} />
				{/snippet}
			</FormControl>
			<FormDescription />
			<FormFieldErrors />
		</FormField>
	</div>

	<div class="mt-6 flex items-center">
		<FormButton type="submit">Submit</FormButton>
	</div>
</form>
