export interface ProductFormInput {
	id: number;
	name: string;
	description: string;
	cost: string;
	price: string;
	category: string;
	stock: string;
	img: File | null;
	expirationDate: string;
}
