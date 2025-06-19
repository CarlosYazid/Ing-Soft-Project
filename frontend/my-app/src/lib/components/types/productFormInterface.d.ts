export interface productForm {
	id: number;
	productName: string;
	description: string;
	cost: number;
	price: number;
	category: string;
	stock: number;
	picture: File | null;
}
