// src/types/productTypes.ts o src/types/product/interfaces.ts
// (elige un nombre de archivo y ruta que te parezca más adecuado)

/**
 * @interface BaseProductInterface
 * @description Define los atributos fundamentales para cualquier tipo de producto.
 * Representa los datos principales que identifican y describen un producto.
 * 'img' se ha tipado como 'File | null' para manejo en formularios,
 * para la URL de la imagen del backend se usaría un 'string'.
 */
export interface BaseProductInterface {
	/** El identificador único del producto. */
	id: number;
	/** El nombre completo del producto. */
	name: string;
	/** Una descripción detallada del producto. */
	description: string;
	/** El precio de venta del producto. */
	price: number;
	/** La categoría a la que pertenece el producto (ej. 'Electrónica', 'Alimentos'). */
	category: string;
	/** La cantidad de unidades disponibles en stock. */
	stock: number;
	/**
	 * El archivo de imagen asociado al producto.
	 * Usado principalmente en formularios de subida.
	 * Para la URL de la imagen obtenida del backend, usa 'string'.
	 */
	img: File | string | null;
}

/**
 * @interface ConsumibleProduct
 * @extends BaseProductInterface
 * @description Extiende BaseProductInterface para incluir la fecha de expiración,
 * típica de productos consumibles o perecederos.
 */
export interface ConsumibleProduct extends BaseProductInterface {
	/** La fecha de expiración del producto en formato de cadena (ej. ISO 8601). */
	expirationDate: Date | string;
}

/**
 * @interface ProductInterface
 * @extends BaseProductInterface, ConsumibleProduct
 * @description Representa la estructura completa de un producto en el backend,
 * combinando las características base y las de un consumible, e incluyendo el costo.
 * Nota: La herencia de múltiples interfaces es útil, pero para tipar la respuesta
 * del backend, considera el Product completo que se definió antes
 * (con id, created_at, updated_at). Aquí se enfoca más en el modelo de datos.
 */
export interface ProductInterface extends ConsumibleProduct {
	/** El costo de adquisición del producto. Se tipa como number para consistencia. */
	cost: number;
	// Si esta ProductInterface es la respuesta final del backend, también podrías añadir
	// created_at: string;
	// updated_at: string;
	// u otras propiedades que el backend devuelva.
	// Esto se solapa con el Product que te di antes, considera cuál usarás como 'fuente de la verdad'
	// para los datos del backend. Generalmente, la respuesta de la API es la que manda.
}

/**
 * @interface ProductRow
 * @description Define la estructura simplificada de un producto para ser mostrada en tablas
 * o listas donde solo se requiere un subconjunto de propiedades.
 */
export interface ProductRow {
	/** El identificador único del producto. */
	id: number;
	/** El nombre del producto. */
	name: string;
	/** La categoría del producto. */
	category: string;
	/** El precio de venta del producto. */
	price: number;
	/** La cantidad de unidades en stock. */
	stock: number;
}

/**
 * @interface ProductForm
 * @description Representa la estructura de los datos tal como se recogen directamente de un formulario
 * de creación o edición de producto en el frontend.
 * Contiene los campos tal cual se usarían en un formulario HTML.
 * Nota: 'picture' es File | null para el input de tipo file.
 */
export interface ProductForm {
	/** El ID del producto (podría ser opcional para creación). */
	id: number;
	/** El nombre del producto ingresado en el formulario. */
	productName: string; // Nota: 'productName' vs 'name' en otras interfaces
	/** La descripción detallada del producto. */
	description: string;
	/** El costo del producto. */
	cost: number;
	/** El precio de venta del producto. */
	price: number;
	/** La categoría del producto. */
	category: string;
	/** La cantidad en stock. */
	stock: number;
	/** El archivo de imagen seleccionado por el usuario. */
	picture: File | null;
	/** La fecha de expiración para productos consumibles. */
	expirationDate?: string; // Opcional, ya que no todos los productos tienen fecha de expiración en BaseProductInterface
}

/**
 * @interface ProductFormInput
 * @description Representa la estructura de los datos de un formulario de producto,
 * donde todos los valores (excepto el archivo) se tratan inicialmente como cadenas de texto,
 * ideal para inputs HTML que siempre devuelven strings.
 * La conversión a 'number' o 'Date' se haría antes de enviar al backend.
 */
export interface ProductFormInput {
	/** El ID del producto, como string desde el input. */
	id: number; // Aunque el input es string, el ID suele ser number para la lógica.
	/** El nombre del producto. */
	name: string;
	/** La descripción del producto. */
	description: string;
	/** El costo del producto, como string. */
	cost: string;
	/** El precio del producto, como string. */
	price: string;
	/** La categoría del producto. */
	category: string;
	/** La cantidad en stock, como string. */
	stock: string;
	/** El archivo de imagen. */
	img: File | null;
	/** La fecha de expiración, como string. */
	expirationDate: string;
}
