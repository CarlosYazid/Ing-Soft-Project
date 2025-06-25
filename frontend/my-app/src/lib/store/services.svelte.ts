// src/lib/stores/service.ts
import type { service } from '$lib/types';

class Service {
	#services: service[] = $state([]);
	#editService: service | null = $state(null);
	#deleteService: service | null = $state(null);

	addService(service: service) {
		this.#services.push(service);
	}

	removeServiceById(id: number) {
		this.#services = this.#services.filter((s) => s.id !== id);
	}

	findServiceById(id: number): service | null {
		return this.#services.find((s) => s.id === id) || null;
	}

	clearEditService() {
		this.#editService = null;
	}

	clearDeleteService() {
		this.#deleteService = null;
	}

	get services(): service[] {
		return this.#services;
	}

	set services(services: service[]) {
		this.#services = services;
	}

	get editService(): service | null {
		return this.#editService;
	}

	set editService(service: service | null) {
		this.#editService = service;
	}

	get deleteService(): service | null {
		return this.#deleteService;
	}

	set deleteService(service: service | null) {
		this.#deleteService = service;
	}
}

// Instancia exportable de la store
export const serviceStore = new Service();
