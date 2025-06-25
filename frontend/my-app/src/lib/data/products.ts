import type { ProductInterface } from '$lib/types';

export let products: ProductInterface[] = [
	{
		id: 1,
		name: 'Producto A',
		description: 'Descripción del Producto A',
		price: 10000,
		cost: 500,
		category: 'Categoría 1',
		stock: 50,
		img: '/1.jpg'
	},
	{
		id: 2,
		name: 'Producto B',
		description: 'Descripción del Producto B',
		price: 20000,
		cost: 1000,
		category: 'Categoría 2',
		stock: 30,
		img: '/2.jpeg'
	},
	{
		id: 3,
		name: 'Producto C',
		description: 'Descripción del Producto C',
		price: 15000,
		cost: 750,
		category: 'Categoría 1',
		stock: 20,
		img: '/3.jpeg'
	},
	{
		id: 4,
		name: 'Producto D',
		description: 'Descripción del Producto D',
		price: 30000,
		cost: 1500,
		category: 'Categoría 3',
		stock: 10,
		img: '/1.jpg'
	}
];

export let services = [
	{
		id: 1,
		name: 'Impresión',
		shortDescription: '',
		price: '$10.000',
		listProducts: [products[0], products[2]]
	},
	{
		id: 2,
		name: 'Fotocopia',
		shortDescription: '',
		price: '$20.000',
		listProducts: [products[1], products[3]]
	},
	{
		id: 3,
		name: 'Plastificado',
		shortDescription: '',
		price: '$30.000',
		listProducts: [products[0], products[1]]
	},
	{
		id: 4,
		name: 'Envolver Regalo',
		shortDescription: '',
		price: '$40.000',
		listProducts: [products[3], products[2], products[1]]
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
