// src/lib/controllers/products.ts
import { api } from '$lib/http/api';
import {
	mapBackendProductBaseToProductBase,
	mapBackendProductToProduct
} from '$lib/utils/product/mappers';

import type {
	BackendBaseProduct,
	BackendProduct,
	BaseProductInterface,
	ProductInterface
} from '$lib/types';

const PRODUCTS_BASE_PATH = '/product';

export const productController = {
	/**
	 * Fetches all products from the backend, mapping them to the frontend's ProductInterface.
	 * @returns A promise that resolves to an array of ProductInterface.
	 * @throws An Error with a user-friendly message if the API call fails.
	 */
	async getAll(): Promise<ProductInterface[]> {
		try {
			const response: BackendProduct[] = await api.get(`${PRODUCTS_BASE_PATH}/all`);

			return response.map(mapBackendProductToProduct);
		} catch (error: any) {
			throw new Error('Error fetching all products:', error);
		}
	},

	/**
	 * Fetches products with low stock from the backend.
	 */
	async searchLowStock(): Promise<ProductInterface[]> {
		try {
			const response: BackendProduct[] = await api.get(`${PRODUCTS_BASE_PATH}/search/low-stock`);
			return response.map(mapBackendProductToProduct);
		} catch (error: any) {
			throw new Error('Error fetching low-stock products:', error);
		}
	},

	/**
	 * Fetches a single product by its ID, mapping it to the frontend's ProductInterface.
	 * @param id The ID of the product to fetch.
	 * @returns A promise that resolves to the ProductInterface.
	 * @throws An Error if the product is not found or the API call fails.
	 */
	async getById(id: number): Promise<ProductInterface> {
		try {
			const response: BackendProduct = await api.get(`${PRODUCTS_BASE_PATH}/${id}`);

			return mapBackendProductToProduct(response);
		} catch (error: any) {
			throw new Error(`Error fetching product ${id}:`, error);
		}
	},

	/**
	 * Updates an existing product by its ID. Data is manually bound for sending.
	 * @param id The ID of the product to update.
	 * @param productData The product data to send to the backend (Frontend BaseProductInterface type for binding).
	 * Note: 'img' should be a string (URL) here if already uploaded.
	 * @returns A promise that resolves to the updated ProductInterface from the backend.
	 * @throws An Error if the update fails (e.g., product not found, invalid data).
	 */
	async updateById(id: number, productData: ProductInterface): Promise<ProductInterface> {
		const dataToSend: Record<string, any> = {
			name: productData.name,
			price: productData.price,
			description: productData.description,
			cost: productData.cost,
			minimum_stock: productData.minimumStock
		};

		/* category: productData.category, Está pailas de momento*/

		try {
			if (
				productData.img &&
				typeof productData.img !== 'string' &&
				productData.img.size > 0 &&
				productData.img.name.trim()
			) {
				// Archivo válido, subir
				await this.uploadProductImage(productData.id, productData.img);
			}

			const response: BackendProduct = await api.putJson(`${PRODUCTS_BASE_PATH}/${id}`, dataToSend);

			await this.updateStock(productData.id, productData.stock, true);

			return mapBackendProductToProduct(response);
		} catch (error: any) {
			console.error(`Error updating product ${id}:`, error);
			if (error.message.includes('Status: 404')) {
				throw new Error(`Product with ID ${id} not found for update.`);
			}
			if (error instanceof Error && error.message.includes('Details: ')) {
				try {
					throw new Error(
						`Failed to update product: ${error.message.split('Details: ')[1] || 'Unknown server error'}`
					);
				} catch {
					throw new Error(`Failed to update product: ${error.message}`);
				}
			}
			throw new Error(
				`An unexpected error occurred while updating product ${id}. Please try again.`
			);
		}
	},

	/**
	 * Actualiza el stock de un producto.
	 * @param id      El ID del producto a actualizar.
	 * @param stock   La cantidad de stock a aplicar.
	 * @param replace Si es true, reemplaza el stock; si es false, suma al stock existente.
	 * @returns       Una promesa que resuelve el producto actualizado en la interfaz ProductInterface.
	 * @throws        Un Error con mensaje amigable si falla la petición.
	 */
	async updateStock(id: number, stock: number, replace: boolean): Promise<ProductInterface> {
		try {
			// Llamada PUT al endpoint /product/stock/{id}/{stock}/{replace}
			const response: BackendProduct = await api.putUrl(
				`${PRODUCTS_BASE_PATH}/stock/${id}/${stock}/${replace}`
			);

			// Mapeamos la respuesta al interfaz de frontend
			return mapBackendProductToProduct(response);
		} catch (error: any) {
			console.error(`Error updating stock for product ${id}:`, error);

			// 404 Not Found
			if (error.message.includes('Status: 404')) {
				throw new Error(`Product with ID ${id} not found for stock update.`);
			}

			// Errores con detalles del backend
			if (error instanceof Error && error.message.includes('Details: ')) {
				const details = error.message.split('Details: ')[1] || 'Unknown server error';
				throw new Error(`Failed to update stock: ${details}`);
			}

			// Error genérico
			throw new Error(
				`An unexpected error occurred while updating stock for product ${id}. Please try again.`
			);
		}
	},

	/**
	 * Deletes a product by its ID.
	 * @param id The ID of the product to delete.
	 * @returns A promise that resolves to void on successful deletion.
	 * @throws An Error if the deletion fails (e.g., product not found).
	 */
	async deleteById(id: number): Promise<void> {
		try {
			// Assume api.delete returns ApiResponse<any> or a successful status
			await api.delete(`${PRODUCTS_BASE_PATH}/${id}`);
		} catch (error: any) {
			console.error(`Error deleting product ${id}:`, error);
			if (error.message.includes('Status: 404')) {
				throw new Error(`Product with ID ${id} not found for deletion.`);
			}
			if (error instanceof Error && error.message.includes('Details: ')) {
				try {
					throw new Error(
						`Failed to delete product: ${error.message.split('Details: ')[1] || 'Unknown server error'}`
					);
				} catch {
					throw new Error(`Failed to delete product: ${error.message}`);
				}
			}
			throw new Error(
				`An unexpected error occurred while deleting product ${id}. Please try again.`
			);
		}
	},

	/**
	 * Sube un archivo de imagen para un producto específico al backend.
	 * Este método asume un endpoint en el backend (ej. POST /products/{id}/upload-image)
	 * que acepta FormData y actualiza la URL de la imagen del producto.
	 *
	 * @param productId El ID del producto al que se asociará la imagen.
	 * @param imageFile El objeto File que representa la imagen a subir.
	 * @returns Una Promesa que se resuelve con la URL de la imagen actualizada desde el backend.
	 * @throws Un Error si la subida falla.
	 */
	async uploadProductImage(productId: number, imageFile: File): Promise<string> {
		if (!(imageFile instanceof File)) {
			throw new Error('El archivo de imagen no es válido');
		}

		const formData = new FormData();
		formData.append('image', imageFile); // "image" debe coincidir con lo que espera el backend

		try {
			// No pasar Content-Type, el fetch lo maneja
			const response: string = await api.putFormData(
				`${PRODUCTS_BASE_PATH}/image/${productId}`,
				formData
			);
			return response;
		} catch (error: any) {
			throw new Error(`Error al subir imagen para el producto ${productId}: ${error.message}`);
		}
	},

	/**
	 * Crea un nuevo producto en el backend y luego, si se proporciona un archivo de imagen, lo sube y asocia al producto creado.
	 *
	 * @param productData Los datos del producto desde el frontend, conforme a ProductInterface.
	 * La propiedad 'id' debe considerarse opcional para la creación.
	 * La propiedad 'img' puede ser un File (para una nueva subida) o un string (si es una URL existente).
	 * @returns Una promesa que se resuelve con la ProductInterface del producto creado (con la URL de la imagen actualizada).
	 * @throws Un Error con un mensaje amigable si cualquier paso (creación o subida de imagen) falla.
	 */
	async create(productData: ProductInterface): Promise<ProductInterface> {
		let createdProductBackend: BackendProduct;

		try {
			// 1. Preparar los datos para la petición POST inicial del producto (excluyendo el archivo de imagen)
			const initialProductDataToSend = {
				category: productData.category,
				cost: productData.cost,
				created_at: '2023-01-01T00:00:00Z',
				description: productData.description,
				image_url: 'https://example.com/image.jpg',
				name: productData.name,
				price: productData.price,
				short_description: productData.description,
				stock: productData.stock,
				type: 'Papelería_general',
				updated_at: '2023-01-01T00:00:00Z',
				expiration_date: productData.expirationDate,
				minimum_stock: productData.minimumStock
			};

			// 2. Realizar la petición POST inicial para crear el producto
			const createResponse: BackendProduct = await api.post(
				`${PRODUCTS_BASE_PATH}/`,
				initialProductDataToSend
			);
			createdProductBackend = createResponse;

			function delay(ms: number) {
				return new Promise((res) => setTimeout(res, ms));
			}

			await delay(1000);

			// 3. Si se proporcionó un archivo de imagen (productData.img es un objeto File), subirlo usando el ID del nuevo producto
			if (productData.img instanceof File) {
				const updatedImageUrl = await this.uploadProductImage(
					createdProductBackend.id,
					productData.img
				);
				// Actualiza la image_url en el objeto del producto creado (en memoria)
				createdProductBackend.image_url = updatedImageUrl;
			}

			return mapBackendProductToProduct(createdProductBackend);
		} catch (error: any) {
			throw new Error(error);
		}
	}
};
