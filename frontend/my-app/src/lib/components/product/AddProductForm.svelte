<script lang="ts">
	import { Input } from '$lib/components/ui/input';
	import { Label } from '$lib/components/ui/label';
	import { Button } from '$lib/components/ui/button/index.js';
	import * as Command from '$lib/components/ui/command/index.js';
	import * as Popover from '$lib/components/ui/popover/index.js';
	import CheckIcon from '@lucide/svelte/icons/check';
	import ChevronsUpDownIcon from '@lucide/svelte/icons/chevrons-up-down';
	import { cn } from '$lib/utils';

	// Tipado
	import type { productForm } from '../../types';
	import SuccessOrFailDialog from '$lib/components/common/SuccessOrFailDialog.svelte';

	// Estados
	let open = $state(false);
	let value = $state('');
	let triggerRef = $state<HTMLButtonElement>(null!);
	let infoDialog = $state();

	const categories = [
		{ value: 'papeleria', label: 'Papelería' },
		{ value: 'comestible', label: 'Comestible' }
	];

	let selectedValue = $derived(categories.find((c) => c.value === value)?.label);

	function closeAndFocusTrigger() {
		open = false;
		triggerRef?.focus();
	}
	$inspect(infoDialog);

	/*Estado para reciclar lógica*/
	let product = $props();
	$inspect(product);

	
</script>

<form id="form" class="w-sm md:w-md" enctype="multipart/form-data">
	<div class="flex flex-col gap-6">
		<div class="grid gap-2">
			<Label for="ProductName">Nombre de Producto</Label>
			<Input
				name="ProductName"
				type="text"
				placeholder="Compás"
				value={product.productName}
				required
			/>
			<input type="text" value={product.productName} />
		</div>

		<div class="grid gap-2">
			<Label for="description">Descripción de Producto</Label>
			<Input
				name="description"
				type="text"
				placeholder="Compás metálico con rueda de precisión de marca Mapped"
				value={product.description}
				required
			/>
		</div>

		<div class="grid gap-2">
			<Label for="cost">Costo de Compra</Label>
			<div class="flex items-center gap-1">
				<span class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</span>
				<Input type="text" name="cost" id="cost" placeholder="0.00" value={product.cost} required />
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div class="grid gap-2">
			<Label for="price">Precio de Venta</Label>
			<div class="flex items-center gap-1">
				<span class="shrink-0 text-base text-gray-500 select-none sm:text-sm/6">$</span>
				<Input
					type="text"
					name="price"
					id="price"
					placeholder="0.00"
					value={product.price}
					required
				/>
				<Input value="COP" class="w-16" disabled />
			</div>
		</div>

		<div class="grid gap-2">
			<Label for="category">Categoría</Label>
			<div class="mt-2">
				<Popover.Root bind:open>
					<Popover.Trigger bind:ref={triggerRef}>
						{#snippet child({ props })}
							<Button
								{...props}
								variant="outline"
								class="w-full justify-between"
								role="combobox"
								aria-expanded={open}
							>
								{selectedValue || product.category || 'Selecciona una Categoría...'}
								<ChevronsUpDownIcon class="opacity-50" />
							</Button>
						{/snippet}
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
			</div>
		</div>
		<Input class="hidden" bind:value name="category" />

		<div class="grid gap-2">
			<Label for="stock">Cantidad a ingresar</Label>
			<Input name="stock" type="text" placeholder="20" value={product.stock} required />
		</div>

		<div class="grid gap-2">
			<Label for="picture">Imagen de Producto</Label>
			<Input
				name="picture"
				type="file"
				required
				onchange={(e) => {
					const input = e.target as HTMLInputElement;
					product.picture = input.files?.[0] || null;
				}}
			/>
		</div>
	</div>

	<div class="mt-4 flex items-center justify-between">
		<Button type="submit" class="bg-blue-700 hover:bg-blue-300 hover:text-blue-700"
			>Añadir producto</Button
		>
		<Button class="bg-red-700 hover:bg-red-500" href="/gestionar-productos">Regresar</Button>
	</div>
</form>

{#key infoDialog}
	{#if infoDialog}
		<SuccessOrFailDialog {infoDialog} contentDialog="" />
	{/if}
{/key}
