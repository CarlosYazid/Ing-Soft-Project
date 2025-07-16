import type { client } from '$lib/types';

class ClientStore {
	// Lista de todos los clientes
	clients: client[] = $state([]);

	// Estado para controlar si se está agregando un cliente
	addingClient: boolean = $state(false);

	// Cliente seleccionado para editar
	editClient: client | null = $state(null);

	// Cliente seleccionado para eliminar
	deleteClient: client | null = $state(null);

	/**
	 * Agrega un nuevo cliente al store
	 */
	addClient(newClient: client) {
		this.clients.push(newClient);
	}

	/**
	 * Elimina un cliente del store por su ID
	 */
	removeClientById(id: number) {
		this.clients = this.clients.filter((c) => c.id !== id);
	}

	/**
	 * Busca un cliente por su ID
	 * @returns El cliente si se encuentra, o null en caso contrario
	 */
	findClientById(id: number): client | null {
		return this.clients.find((c) => c.id === id) || null;
	}

	clearEditClient() {
		this.editClient = null;
	}

	clearDeleteClient() {
		this.deleteClient = null;
	}
}

// Instancia exportable de la store
export const clientStore = new ClientStore();
