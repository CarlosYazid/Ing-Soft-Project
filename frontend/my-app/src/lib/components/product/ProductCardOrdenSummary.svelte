<script lang="ts">
	import * as Card from '$lib/components/ui/card/index.js';
	import type { BaseProductInterface } from '$lib/types';
	export let product: BaseProductInterface;
	export let quantity: number;
</script>

<Card.Root>
	<Card.Header>
		<Card.Title>{product.name}</Card.Title>
		<Card.Description>{quantity}</Card.Description>
	</Card.Header>
	<Card.Content>
		<p>Card Content</p>
	</Card.Content>
	<Card.Footer>
		<p>Card Footer</p>
	</Card.Footer>
</Card.Root>
