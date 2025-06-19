import { z } from 'zod';

// Esquema del formulario
export const productSchema = z.object({
	productName: z
		.string()
		.min(1, 'Nombre requerido')
		.max(64, 'Nombre debe ser menor a 64 caracteres')
		.trim(),
	description: z
		.string()
		.min(1, 'Descripción requerida')
		.max(256, 'Descripción debe ser menor a 256 caracteres')
		.trim(),
	cost: z
		.string()
		.regex(/^\d+(\.\d{1,6})?$/, 'Costo inválido')
		.trim(),
	price: z
		.string()
		.regex(/^\d+(\.\d{1,6})?$/, 'Precio inválido')
		.trim(),
	category: z.string().min(1, 'Selecciona una categoría').trim(),
	stock: z.string().regex(/^\d+$/, 'Cantidad inválida').trim(),
	picture: z.any()
});

export type ProductSchema = typeof productSchema;
