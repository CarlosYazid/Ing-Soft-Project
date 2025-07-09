// src/lib/controllers/serviceController.ts
import type { ProductInterface, service } from '$lib/types';
import { productController } from './product';
import { api } from '$lib/http/api';

const SERVICE_BASE_PATH = '/service';

/**
 * Transforma un objeto completo de la base de datos al tipo frontend `service`.
 */
function toService(data: any): service {
	return {
		id: data.id,
		name: data.name,
		price: data.price,
		products: []
	};
}

async function getAllServices(): Promise<service[]> {
	try {
		const rawServices = await api.get(`${SERVICE_BASE_PATH}/all`);
		const services: service[] = rawServices.map(toService);

		/* services.forEach(s => getProductsOfService(s)) */

		return services;
	} catch (error) {
		console.error('Error al obtener servicios:', error);
		throw new Error('No se pudieron obtener los servicios');
	}
}

async function createService(partialService: service): Promise<service> {
	try {
		const payload = {
			name: partialService.name ?? '',
			price: partialService.price ?? 0,
			cost: 0,
			description: '',
			short_description: '',
			created_at: new Date().toISOString(),
			updated_at: new Date().toISOString()
		};

		const created = await api.post(`${SERVICE_BASE_PATH}/`, payload);

		//Añadimos los productos al servicio
		/* partialService.products?.forEach((p) => addProductToService(p, partialService)); */

		return toService(created);
	} catch (error) {
		console.error('Error al crear el servicio:', error);
		throw new Error('No se pudo crear el servicio');
	}
}

async function updateService(id: number, updatedFields: service): Promise<service> {
	try {
		const payload = {
			name: updatedFields.name ?? '',
			price: updatedFields.price ?? 0,
			cost: 0,
			description: '',
			short_description: '',
			created_at: new Date().toISOString(),
			updated_at: new Date().toISOString()
		};

		const updated = await api.putJson(`${SERVICE_BASE_PATH}/${id}`, payload);
		return toService(updated);
	} catch (error) {
		console.error(`Error al actualizar el servicio con ID ${id}:`, error);
		throw new Error('No se pudo actualizar el servicio');
	}
}

async function deleteServiceById(id: number): Promise<void> {
	try {
		await api.delete(`${SERVICE_BASE_PATH}/${id}`);
	} catch (error) {
		console.error(`Error al eliminar el servicio con ID ${id}:`, error);
		throw new Error('No se pudo eliminar el servicio');
	}
}

async function addProductToService(product: ProductInterface, service: service) {
	const payload = {
		product_id: product.id,
		service_id: service.id
	};

	try {
		await api.post(`${SERVICE_BASE_PATH}/input_services/`, payload);
	} catch (error) {
		console.error(`Error al añadir producto con ID ${product.id}:`, error);
		throw new Error('No se pudo añadir el producto');
	}
}

async function getProductsOfService(service: service) {
	try {
		const productsToGet = await api.get(`${SERVICE_BASE_PATH}/input_services/`);
		productsToGet.forEach(async (product: { id: number; }) => {
			const productGet = await productController.getById(product.id)
			service.products?.push(productGet)
		});
	} catch (error) {
		console.error(`Error al al obtener los productos del servicio`, error);
		throw new Error('No se pudo obtener los productos del servicio');
	}
}

// Exportamos los métodos en un solo objeto
export const serviceController = {
	getAllServices,
	createService,
	updateService,
	deleteServiceById
};
