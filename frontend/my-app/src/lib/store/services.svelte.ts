// src/lib/stores/service.ts
import type { service, ProductInterface } from '$lib/types';

class Service {
	services: service[] = $state([]);
	addingService: boolean = $state(false);
	editService: service | null = $state(null);
	deleteService: service | null = $state(null);
	productsToAdd: ProductInterface[] = $state([]);

	addService(service: service) {
		this.services.push(service);
	}

	removeServiceById(id: number) {
		this.services = this.services.filter((s) => s.id !== id);
	}

	findServiceById(id: number): service | null {
		return this.services.find((s) => s.id === id) || null;
	}

	clearEditService() {
		this.editService = null;
	}

	clearDeleteService() {
		this.deleteService = null;
	}

	clearProductsToAdd() {
		this.productsToAdd = [];
	}

	addProductToService(product: ProductInterface) {
		this.productsToAdd.push(product);
	}

	deleteProductFromService(product: ProductInterface) {
		this.productsToAdd = this.productsToAdd.filter((p) => p.id !== product.id);
	}
}

// Instancia exportable de la store
export const serviceStore = new Service();
