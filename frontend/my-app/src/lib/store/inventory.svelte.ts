import type { ProductInterface } from '$lib/types';

class Inventory {
	#products: ProductInterface[] = $state([]);
	#editProduct: ProductInterface | null = $state(null);
	#deleteProduct: ProductInterface | null = $state(null);

	constructor(initialData: ProductInterface[]) {
		this.#products = initialData;
	}

	addProduct(product: ProductInterface) {
		this.#products.push(product);
	}

	removeProductById(id: number) {
		this.#products = this.#products.filter((p) => p.id !== id);
	}

	findProductById(id: number): ProductInterface | null {
		return this.#products.find((p) => p.id === id) || null;
	}

	clearEditProduct() {
		this.#editProduct = null;
	}

	clearDeleteProduct() {
		this.#deleteProduct = null;
	}

	get products() {
		return this.#products;
	}

	set products(p: ProductInterface[]) {
		this.#products = p;
	}

	get editProduct(): ProductInterface | null {
		return this.#editProduct;
	}

	get deleteProduct(): ProductInterface | null {
		return this.#deleteProduct;
	}

	set editProduct(p: ProductInterface) {
		this.#editProduct = p;
	}

	set deleteProduct(p: ProductInterface) {
		this.#deleteProduct = p;
	}
}

// Llamar el DB controller dentro de inventory
export const inventory = new Inventory([
	{
		id: 1,
		name: 'Cuaderno Argollado Pasta Dura',
		description: 'Cuaderno universitario de 100 hojas, cuadros de 7mm, ideal para tomar apuntes.',
		cost: 5000.0,
		price: 8500.0,
		category: 'Cuadernos',
		stock: 200,
		img: null,
		expirationDate: Date.now().toString()
	},
	{
		id: 2,
		name: 'Caja de Esferos Negros x12',
		description: 'Docena de esferos de tinta negra, punta fina, escritura suave y duradera.',
		cost: 12000.0,
		price: 21900.0,
		category: 'Esferos y Lápices',
		stock: 150,
		img: null,
		expirationDate: Date.now().toString()
	},
	{
		id: 3,
		name: 'Resaltadores Pastel x6',
		description: 'Set de 6 resaltadores en tonos pastel, tinta de secado rápido, punta biselada.',
		cost: 9000.0,
		price: 15500.0,
		category: 'Marcadores y Resaltadores',
		stock: 90,
		img: null,
		expirationDate: Date.now().toString()
	},
	{
		id: 4,
		name: 'Block de Hojas Iris Colores',
		description: 'Block de 50 hojas de papel iris de colores surtidos, tamaño carta, 75 gramos.',
		cost: 4500.0,
		price: 7800.0,
		category: 'Papelería Creativa',
		stock: 180,
		img: null,
		expirationDate: Date.now().toString()
	},
	{
		id: 5,
		name: 'Carpeta de Archivo Plástica Oficio',
		description: 'Carpeta plástica tamaño oficio con elástico, ideal para organizar documentos.',
		cost: 3000.0,
		price: 5200.0,
		category: 'Organización',
		stock: 100,
		img: null,
		expirationDate: Date.now().toString()
	}
]);
