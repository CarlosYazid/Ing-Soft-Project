import type { client } from '$lib/types';
import { api } from '$lib/http/api';

const CLIENT_BASE_PATH = '/user/client';

/**
 * Transforma un objeto completo de la base de datos al tipo frontend `client`.
 */
function toClient(data: any): client {
	return {
		id: data.id,
		documentid: data.documentid,
		name: data.name,
		email: data.email,
		phone: data.phone
	};
}

async function getAllClients(): Promise<client[]> {
	try {
		const rawClients = await api.get(`${CLIENT_BASE_PATH}/all`);
		return rawClients.map(toClient);
	} catch (error) {
		console.error('Error al obtener los clientes:', error);
		throw new Error('No se pudieron obtener los clientes');
	}
}

async function createClient(partialClient: client): Promise<client> {
	try {
		const payload = {
			...partialClient,
			state: true,
			created_at: new Date().toISOString(),
			updated_at: new Date().toISOString()
		};

		const created = await api.post(`${CLIENT_BASE_PATH}`, payload);
		return toClient(created);
	} catch (error) {
		console.error('Error al crear el cliente:', error);
		throw new Error('No se pudo crear el cliente');
	}
}

async function updateClient(id: number, updatedFields: client): Promise<client> {
	try {
		const payload = {
			...updatedFields,
			state: true,
			created_at: new Date().toISOString(),
			updated_at: new Date().toISOString()
		};

		const updated = await api.putJson(`${CLIENT_BASE_PATH}/${id}`, payload);
		return toClient(updated);
	} catch (error) {
		console.error(`Error al actualizar el cliente con ID ${id}:`, error);
		throw new Error('No se pudo actualizar el cliente');
	}
}

async function deleteClientById(id: number): Promise<void> {
	try {
		await api.delete(`${CLIENT_BASE_PATH}/${id}`);
	} catch (error) {
		console.error(`Error al eliminar el cliente con ID ${id}:`, error);
		throw new Error('No se pudo eliminar el cliente');
	}
}

export const clientController = {
	getAllClients,
	createClient,
	updateClient,
	deleteClientById
};
