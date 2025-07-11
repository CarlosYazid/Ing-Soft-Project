import type { ProductInterface } from './productTypes';

export interface service {
	id: number;
	name: string;
	price: number;
	products?: ProductInterface[];
	quantity?: number;
}

export interface serviceFormInput {
	name: string;
	price: string;
}
