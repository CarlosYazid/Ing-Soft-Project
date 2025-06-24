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
