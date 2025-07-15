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

		return await Promise.all(
			services.map(async (s) => {
				s.products = await getProductsOfService(s);
				return s;
			})
		);
	} catch (error: any) {
		console.error('Error al obtener servicios:', error);
		throw new Error(`No se pudieron obtener los servicios: ${error.message}`);
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
		const newService = toService(created);

		//Añadimos los productos al servicio
		partialService.products?.forEach((p) => addProductToService(p.id, newService.id));

		return newService;
	} catch (error) {
		console.error('Error al crear el servicio:', error);
		throw new Error('No se pudo crear el servicio');
	}
}

async function updateService(
	id: number,
	updatedFields: service,
	oldProducts: ProductInterface[]
): Promise<service> {
	try {
		const payload = {
			name: updatedFields.name ?? '',
			price: updatedFields.price ?? 0,
			cost: 0,
			description: '',
			short_description: ''
		};

		const updated = await api.putJson(`${SERVICE_BASE_PATH}/${id}`, payload);

		updateServiceProducts(updatedFields, oldProducts);

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

async function addProductToService(productId: number, serviceId: number) {
	const payload = {
		product_id: productId,
		service_id: serviceId
	};

	console.log('payload', payload);

	try {
		await api.post(`${SERVICE_BASE_PATH}/input_service/`, payload);
	} catch (error) {
		console.error(`Error al añadir producto con ID ${productId}:`, error);
		throw new Error('No se pudo añadir el producto');
	}
}

async function getProductsOfService(service: service) {
	try {
		const productsToGet = await api.get(`${SERVICE_BASE_PATH}/input_service/service/${service.id}`);
		const fetched = await Promise.all(
			productsToGet.map(async (input: any) => await productController.getById(input.product_id))
		);
		return fetched;
	} catch (error: any) {
		console.error(`Error al obtener los productos del servicio ${service.id}:`, error);
		throw new Error(`No se pudo obtener los productos del servicio: ${error.message}`);
	}
}

async function deleteProductFromService(productId: number, serviceId: number) {
	try {
		await api.delete(`${SERVICE_BASE_PATH}/input_service/${serviceId}/${productId}`);
	} catch (error) {
		// Parchado que si hay error es pq ese producto no estaba asociado
	}
}

/**
 * Actualiza los productos asociados a un servicio:
 *  - Elimina los que ya no están
 *  - Añade los nuevos
 *
 */
async function updateServiceProducts(service: service, oldProducts: ProductInterface[]) {
	// 1. Traer los IDs actuales
	const originalIds = oldProducts.map((p) => p.id) || [];

	// 2. Crear Sets para búsquedas O(1)
	const originalSet = new Set(originalIds);
	const newSet = new Set(service.products?.map((p) => p.id));

	// 3. Calcular qué eliminar (estaba antes, ya no)
	const toRemove = originalIds.filter((id) => !newSet.has(id));

	// 4. Calcular qué añadir (es nuevo, no estaba antes)
	const toAdd = service.products?.map((p) => p.id).filter((id) => !originalSet.has(id)) || [];

	// 5. Ejecutar eliminaciones en paralelo
	await Promise.all(toRemove.map((id) => deleteProductFromService(id, service.id)));

	// 6. Ejecutar inserciones en paralelo
	await Promise.all(toAdd.map((id) => addProductToService(id, service.id)));
}

async function getProductIdsOfService(service: service): Promise<number[]> {
	try {
		const productsToGet = await api.get(`${SERVICE_BASE_PATH}/input_service/service/${service.id}`);

		// Solo retornamos el listado de product_id
		const productIds = productsToGet.map((input: any) => input.product_id);
		return productIds;
	} catch (error: any) {
		console.error(`Error al obtener los IDs de productos del servicio ${service.id}:`, error);
		throw new Error(`No se pudieron obtener los IDs de productos del servicio: ${error.message}`);
	}
}

// Exportamos los métodos en un solo objeto
export const serviceController = {
	getAllServices,
	createService,
	updateService,
	deleteServiceById,
	getProductsOfService,
	getProductIdsOfService
};
