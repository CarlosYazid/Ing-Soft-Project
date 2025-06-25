// src/lib/controllers/serviceController.ts
import type { service } from '$lib/types';
import { api } from '$lib/http/api';

const SERVICE_BASE_PATH = '/service';

/**
 * Transforma un objeto completo de la base de datos al tipo frontend `service`.
 */
function toService(data: any): service {
	return {
		id: data.id,
		name: data.name,
		price: data.price
	};
}

export async function getAllServices(): Promise<service[]> {
	try {
		const rawServices = await api.get(`${SERVICE_BASE_PATH}/all`);
		return rawServices.map(toService);
	} catch (error) {
		console.error('Error al obtener servicios:', error);
		throw new Error('No se pudieron obtener los servicios');
	}
}

export async function createService(partialService: service): Promise<service> {
	try {
		const nuevoServicio = {
			name: partialService.name ?? '',
			price: partialService.price ?? 0,
			cost: 0,
			description: '',
			short_description: '',
			created_at: new Date().toISOString(),
			updated_at: new Date().toISOString()
		};

		const created = await api.post(`${SERVICE_BASE_PATH}/`, partialService);
		return toService(created);
	} catch (error) {
		console.error('Error al crear el servicio:', error);
		throw new Error('No se pudo crear el servicio');
	}
}

export async function updateService(id: number, updatedFields: service): Promise<service> {
	try {
		const updatedServicio = {
			name: updatedFields.name ?? '',
			price: updatedFields.price ?? 0,
			cost: 0,
			description: '',
			short_description: '',
			created_at: new Date().toISOString(), // o puedes traer esto del backend si quieres más precisión
			updated_at: new Date().toISOString()
		};

		const updated = await api.putJson(`${SERVICE_BASE_PATH}/${id}`, updatedServicio);
		return toService(updated);
	} catch (error) {
		console.error(`Error al actualizar el servicio con ID ${id}:`, error);
		throw new Error('No se pudo actualizar el servicio');
	}
}

/**
 * Elimina un servicio por ID.
 */
export async function deleteServiceById(id: number): Promise<void> {
	try {
		await api.delete(`${SERVICE_BASE_PATH}/${id}`);
	} catch (error) {
		console.error(`Error al eliminar el servicio con ID ${id}:`, error);
		throw new Error('No se pudo eliminar el servicio');
	}
}
