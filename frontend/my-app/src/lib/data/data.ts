import type { ProductInterface } from '$lib/types';
import type { service } from '$lib/types/serviceTypes.js';

export let products: ProductInterface[] = [
	{
		id: 1,
		name: 'Producto A',
		description: 'Descripción del Producto A',
		price: 10000,
		cost: 500,
		category: 'Categoría 1',
		stock: 50,
		img: '/1.jpg',
		expirationDate: '2024-12-31'
	},
	{
		id: 2,
		name: 'Producto B',
		description: 'Descripción del Producto B',
		price: 20000,
		cost: 1000,
		category: 'Categoría 2',
		stock: 30,
		img: '/2.jpeg',
		expirationDate: '2025-01-15'
	},
	{
		id: 3,
		name: 'Producto C',
		description: 'Descripción del Producto C',
		price: 15000,
		cost: 750,
		category: 'Categoría 1',
		stock: 20,
		img: '/3.jpeg',
		expirationDate: '2024-11-30'
	},
	{
		id: 4,
		name: 'Producto D',
		description: 'Descripción del Producto D',
		price: 30000,
		cost: 1500,
		category: 'Categoría 3',
		stock: 10,
		img: '/1.jpg',
		expirationDate: '2025-02-28'
	}
];

export let services: service[] = [
	{
		id: 1,
		name: 'Impresión',
		price: 100,
		products: [products[0], products[2]]
	},
	{
		id: 2,
		name: 'Fotocopia',
		price: 200,
		products: [products[1], products[3]]
	},
	{
		id: 3,
		name: 'Plastificado',
		price: 300,
		products: [products[0], products[1]]
	},
	{
		id: 4,
		name: 'Envolver Regalo',
		price: 400,
		products: [products[3], products[2], products[1]]
	}
];

export let orderProducts = [
	{ product: products[0], quantity: 2 },
	{ product: products[1], quantity: 1 },
	{ product: products[2], quantity: 3 },
	{ product: products[3], quantity: 1 }
];

export let orderServices = [
	{ service: services[0], quantity: 1 },
	{ service: services[1], quantity: 2 },
	{ service: services[2], quantity: 1 }
];

export let clients = [
	{
		id: 1,
		name: 'Cliente A',
		number: '123456789'
	},
	{
		id: 2,
		name: 'Cliente B',
		number: '987654321'
	},
	{
		id: 3,
		name: 'Cliente C',
		number: '456789123'
	}
];
