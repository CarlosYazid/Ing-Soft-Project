// src/types/responses/productResponses.ts

/**
 * @interface BaseProduct
 * @description Representa los atributos mínimos y editables de un producto,
 * generalmente los que se envían al crear o actualizar un producto.
 */
export interface BackendBaseProduct {
	/** El identificador único del producto, asignado por el backend. */
	id: number;
	/** El nombre legible del producto (ej. "Galletas Festival"). */
	name: string;
	/** Una descripción corta del producto. */
	short_description: string;
	/** El precio de venta del producto. Se usa 'number' para manejar decimales. */
	price: number;
	/** La categoría general a la que pertenece el producto (ej. "Consumibles"). */
	category: string;
	/** La cantidad de unidades del producto en inventario. */
	stock: number;
	/** La URL de la imagen principal del producto. */
	image_url: string;
}

/**
 * @interface Product
 * @extends BaseProduct
 * @description Representa la estructura completa de un producto tal como es recibida
 * del backend, incluyendo metadatos generados por el servidor.
 */
export interface BackendProduct extends BackendBaseProduct {
	/**
	 * La fecha y hora de creación del registro del producto en el backend, en formato ISO 8601.
	 * Es un string que puedes convertir a 'Date' si necesitas operar con ella.
	 */
	created_at: string;
	/**
	 * La fecha y hora de la última actualización del registro del producto en el backend, en formato ISO 8601.
	 * También un string.
	 */
	updated_at: string;
	/** Una descripción completa y detallada del producto. */
	description: string;
	/** El costo de adquisición del producto. */
	cost: number;
	/** El tipo específico o subtipo del producto (ej. "Galletas_y_bizcochos"). */
	type: string;
	/**
	 * La fecha de vencimiento del producto, en formato ISO 8601.
	 * Se mantiene como 'string' si la usas directamente del backend,
	 * o 'Date' si la parseas. Sugiero 'string' inicialmente y parsear si es necesario en el cliente.
	 */
	expiration_date: string;
}

/**
 * @interface ProductListResponse
 * @description Define la estructura para una respuesta que contiene una lista de productos,
 * útil para endpoints de paginación o listado general.
 */
export interface ProductListResponse {
	products: Product[];
}
