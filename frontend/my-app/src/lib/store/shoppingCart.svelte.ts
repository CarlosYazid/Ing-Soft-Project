import type { ProductInterface, service, client, order, OrderWithInvoice } from '$lib/types';

class Cart {
	products: ProductInterface[] = $state([]);
	services: service[] = $state([]);
	client: client | null = $state(null);
	/* total: number = $derived-by(...)); */ // Se podría activar para manejar como micro optimización o mejorar la reactividad, de momento estoy de afán, pailas
	productSelected: ProductInterface | null = $state(null);
	serviceSelected: service | null = $state(null);
	DEFAULT_EMPLOYEE_ID: number = 8;
	DEFAULT_CLIENT_ID: number = 5;
	currentOrder: order | null = $state(null);
	lastOrder: OrderWithInvoice | null = $state(null);
	finishedOrder: boolean = $state(false);

	addProduct(product: ProductInterface) {
		this.products.push(product);
		this.recalculateTotal();
	}

	removeProductById(id: number) {
		this.products = this.products.filter((p) => p.id !== id);
		this.recalculateTotal();
	}

	addService(service: service) {
		this.services.push(service);
		this.recalculateTotal();
	}

	removeServiceById(id: number) {
		this.services = this.services.filter((s) => s.id !== id);
		this.recalculateTotal();
	}

	clearCart() {
		this.products = [];
		this.services = [];
		this.client = null;
		this.currentOrder = null;
	}

	recalculateTotal() {
		const totalProductos = this.products.reduce((acc, p) => acc + p.price * p.quantity!, 0);
		const totalServicios = this.services.reduce(
			(acc, s) =>
				acc +
				s.products!.reduce(
					(acc, p) => acc + s.price * p.quantityService! + p.price * p.quantityService!,
					0
				),
			0
		);
		return (totalProductos + totalServicios).toFixed(2);
	}

	findProductById(id: number): ProductInterface | null {
		return this.products.find((p) => p.id === id) || null;
	}

	findServiceById(id: number): service | null {
		return this.services.find((s) => s.id === id) || null;
	}
}

export const cartStore = new Cart();
