// src/lib/controllers/orderController.ts
import type { ProductInterface, service, order } from '$lib/types';
import { api } from '$lib/http/api';

const ORDER_BASE_PATH = '/order';
const ORDER_PRODUCTS_PATH = '/order/product';
const ORDER_SERVICES_PATH = '/order/service';

/**
 * Transforma un objeto recibido de la base de datos al tipo frontend `order`.
 */
function toOrder(data: any): order {
	return {
		id: data.id,
		client_id: data.client_id,
		status: data.status,
		employee_id: data.employee_id,
		total_price: data.total_price
	};
}

// CRUD principal de órdenes
async function createOrder(order: Partial<order>): Promise<order> {
	try {
		const payload = {
			client_id: order.client_id,
			created_at: new Date().toISOString().split('.')[0] + 'Z',
			employee_id: order.employee_id,
			status: order.status,
			total_price: order.total_price,
			updated_at: new Date().toISOString().split('.')[0] + 'Z'
		};
		const created = await api.post(`${ORDER_BASE_PATH}/`, payload);
		return toOrder(created);
	} catch (error: any) {
		console.error('Error al crear la orden:', error);
		throw new Error('No se pudo crear la orden');
	}
}

async function getOrderById(id: number): Promise<order> {
	try {
		const result = await api.get(`${ORDER_BASE_PATH}/${id}`);
		return toOrder(result);
	} catch (error: any) {
		console.error(`Error al obtener la orden ${id}:`, error);
		throw new Error('No se pudo obtener la orden');
	}
}

async function getAllOrders(): Promise<order[]> {
	try {
		const rawOrders = await api.get(`${ORDER_BASE_PATH}/all`);
		return rawOrders.map(toOrder);
	} catch (error: any) {
		console.error('Error al obtener todas las órdenes:', error);
		throw new Error('No se pudieron obtener las órdenes');
	}
}

async function updateOrder(id: number, updatedFields: Partial<order>): Promise<order> {
	try {
		const updated = await api.putJson(`${ORDER_BASE_PATH}/${id}`, updatedFields);
		return toOrder(updated);
	} catch (error: any) {
		console.error(`Error al actualizar la orden ${id}:`, error);
		throw new Error('No se pudo actualizar la orden');
	}
}

async function deleteOrderById(id: number): Promise<void> {
	try {
		await api.delete(`${ORDER_BASE_PATH}/${id}`);
	} catch (error) {
		console.error(`Error al eliminar la orden ${id}:`, error);
		throw new Error('No se pudo eliminar la orden');
	}
}

// Asociar productos a una orden
async function addProductsToOrder(orderId: number, products: ProductInterface[]) {
	const payloads = products.map((p) => ({
		order_id: orderId,
		product_id: p.id,
		quantity: p.quantity! + p.quantityService!
	}));

	try {
		if (products) await Promise.all(payloads.map((p) => api.post(`${ORDER_PRODUCTS_PATH}/`, p)));
	} catch (error) {
		console.error('Error al asociar productos a la orden:', error);
		throw new Error('No se pudieron asociar los productos a la orden');
	}
}

// Asociar servicios a una orden
async function addServicesToOrder(orderId: number, services: service[]) {
	const payloads = services.map((s) => ({
		order_id: orderId,
		service_id: s.id,
		quantity: s.products?.reduce((acc, p) => acc + p.quantityService!, 0)
	}));

	try {
		await Promise.all(payloads.map((s) => api.post(`${ORDER_SERVICES_PATH}/`, s)));
	} catch (error) {
		console.error('Error al asociar servicios a la orden:', error);
		throw new Error('No se pudieron asociar los servicios a la orden');
	}
}

// Cambiar status a completada
async function markOrderAsCompleted(orderId: number) {
	try {
		await api.putJson(`${ORDER_BASE_PATH}/${orderId}`, { status: 'Completada' });
	} catch (error) {
		console.error(`Error al marcar como completada la orden ${orderId}:`, error);
		throw new Error('No se pudo completar la orden');
	}
}

// Método combinado para crear orden con todo el flujo
async function createOrderWithItems(
	orderData: Partial<order>,
	products: ProductInterface[],
	services: service[]
): Promise<order> {
	try {
		const newOrder = await createOrder(orderData);

		// Asociar productos
		await addProductsToOrder(newOrder.id, products);

		// Asociar servicios
		await addServicesToOrder(newOrder.id, services);

		// Cambiar status a completada
		await markOrderAsCompleted(newOrder.id);

		return newOrder;
	} catch (error) {
		console.error('Error general en el proceso de creación de orden:', error);
		throw new Error('Ocurrió un error al procesar la orden');
	}
}

export const orderController = {
	createOrder,
	getOrderById,
	getAllOrders,
	updateOrder,
	deleteOrderById,
	addProductsToOrder,
	addServicesToOrder,
	markOrderAsCompleted,
	createOrderWithItems
};
