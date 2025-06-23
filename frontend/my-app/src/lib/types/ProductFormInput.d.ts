export interface ProductFormInput {
	id: number; // id puede venir como string del formulario
	name: string; // Nombre del input en el HTML
	description: string;
	cost: string;
	price: string;
	category: string;
	stock: string;
	picture: File | null;
	expirationDate?: string; // Nombre del input type="file" en el HTML
	// Si tienes un input para expirationDate, agrégalo aquí
	// expirationDate: string;
}
