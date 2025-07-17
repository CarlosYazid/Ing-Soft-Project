// src/lib/controllers/orderController.ts
import type { ProductInterface, service, order, OrderWithInvoice } from '$lib/types';
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

function toOrderWithInvoice(data: any): OrderWithInvoice {
	return {
		id: data.id,
		client_id: data.client_id,
		status: data.status,
		employee_id: data.employee_id,
		total_price: data.total_price,
		created_at: data.created_at,
		updated_at: data.updated_at,
		invoice_link: data.invoice_link
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

async function getOrderById(id: number): Promise<OrderWithInvoice> {
	try {
		const result = await api.get(`${ORDER_BASE_PATH}/${id}`);
		return toOrderWithInvoice(result);
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
		if (products)
			await Promise.all(
				payloads.map((p) => {
					if (p.quantity > 0) api.post(`${ORDER_PRODUCTS_PATH}/`, p);
				})
			);
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
		await Promise.all(services.map((s) => addProductsToOrder(orderId, s.products!)));
	} catch (error) {
		console.error('Error al asociar servicios a la orden:', error);
		throw new Error('No se pudieron asociar los servicios a la orden');
	}
}

// Cambiar status a completada
async function markOrderAsCompleted(orderId: number) {
	try {
		await api.putUrl(`${ORDER_BASE_PATH}/status/${orderId}/${'Completada'}`);
	} catch (error) {
		console.error(`Error al marcar como completada la orden ${orderId}:`, error);
		throw new Error('No se pudo completar la orden');
	}
}

async function generateInvoice(orderId: number, taxRate = 0.19): Promise<string> {
	try {
		const payload = {
			order_id: orderId,
			tax_rate: taxRate
		};
		const result = await api.post('/invoice/generate', payload);
		return result as string;
	} catch (error: any) {
		console.error(`Error al generar la factura de la orden ${orderId}:`, error);
		throw new Error('No se pudo generar ni enviar la factura digital');
	}
}

function delay(ms: number) {
	return new Promise<void>((resolve) => setTimeout(resolve, ms));
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

		// Espera un momento
		await delay(3000);

		// Cambiar status a completada
		await markOrderAsCompleted(newOrder.id);

		// Generar factura
		await generateInvoice(newOrder.id);

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
