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
	ProductInterface,
	ApiResponse,
	ApiErrorResponse
} from '$lib/types';

const PRODUCTS_BASE_PATH = '/products';

export const productController = {
	/**
	 * Fetches all products from the backend, mapping them to the frontend's ProductInterface.
	 * @returns A promise that resolves to an array of ProductInterface.
	 * @throws An Error with a user-friendly message if the API call fails.
	 */
	async getAll(): Promise<ProductInterface[]> {
		try {
			// Assume api.get returns ApiResponse<ProductListResponse>
			const response: ApiResponse<{ products: BackendProduct[] }> = await api.get(
				`${PRODUCTS_BASE_PATH}/all`
			);

			if (!response.success) {
				// If the API indicates failure but doesn't throw an HTTP error
				throw new Error(
					response.message || 'Failed to fetch products due to an unknown API error.'
				);
			}

			// Map each backend product to the frontend ProductInterface
			return response.data.products.map(mapBackendProductToProduct);
		} catch (error: any) {
			console.error('Error fetching all products:', error);
			// Attempt to parse the detailed error from api.ts's throw
			if (error instanceof Error && error.message.includes('Details: ')) {
				try {
					const errorDetails: ApiErrorResponse = JSON.parse(error.message.split('Details: ')[1]);
					throw new Error(
						`Failed to load products: ${errorDetails.message || 'Unknown server error'}`
					);
				} catch (parseError) {
					// Fallback if parsing fails or 'Details' isn't valid JSON
					throw new Error(`Failed to load products: ${error.message}`);
				}
			}
			// Fallback for general network errors or unexpected issues
			throw new Error('An unexpected error occurred while fetching products. Please try again.');
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
			// Assume api.get returns ApiResponse<BackendProduct>
			const response: ApiResponse<BackendProduct> = await api.get(`${PRODUCTS_BASE_PATH}/${id}`);

			if (!response.success) {
				throw new Error(response.message || `Failed to fetch product with ID ${id}.`);
			}

			// Map the backend product to the frontend ProductInterface
			return mapBackendProductToProduct(response.data);
		} catch (error: any) {
			console.error(`Error fetching product ${id}:`, error);
			if (error.message.includes('Status: 404')) {
				throw new Error(`Product with ID ${id} not found.`);
			}
			if (error instanceof Error && error.message.includes('Details: ')) {
				try {
					const errorDetails: ApiErrorResponse = JSON.parse(error.message.split('Details: ')[1]);
					throw new Error(
						`Failed to get product: ${errorDetails.message || 'Unknown server error'}`
					);
				} catch {
					throw new Error(`Failed to get product: ${error.message}`);
				}
			}
			throw new Error(
				`An unexpected error occurred while fetching product ${id}. Please try again.`
			);
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
	async updateById(id: number, productData: Partial<ProductInterface>): Promise<ProductInterface> {
		// Manually bind the data to the backend's expected format (BackendBaseProduct structure).
		// Ensure that `productData.img` is the URL string here, not a File object.
		const dataToSend = {
			id: productData.id, // Backend might expect ID in body for PUT, if not, remove.
			name: productData.name,
			short_description: productData.description, // Mapping frontend 'description' to backend 'short_description'
			price: productData.price,
			category: productData.category,
			stock: productData.stock,
			image_url: typeof productData.img === 'string' ? productData.img : '', // Ensure it's a URL string
			description: productData.description, // Assuming backend needs full description in update
			cost: productData.cost,
			type: '',
			expiration_date:
				productData.expirationDate instanceof Date
					? productData.expirationDate.toISOString()
					: productData.expirationDate // Convert Date to ISO string if needed
		};

		try {
			// Assume api.put returns ApiResponse<BackendProduct>
			const response: ApiResponse<BackendProduct> = await api.put(
				`${PRODUCTS_BASE_PATH}/${id}`,
				dataToSend
			);

			if (!response.success) {
				throw new Error(response.message || `Failed to update product with ID ${id}.`);
			}

			// Map the updated backend product to the frontend ProductInterface
			return mapBackendProductToProduct(response.data);
		} catch (error: any) {
			console.error(`Error updating product ${id}:`, error);
			if (error.message.includes('Status: 404')) {
				throw new Error(`Product with ID ${id} not found for update.`);
			}
			if (error instanceof Error && error.message.includes('Details: ')) {
				try {
					const errorDetails: ApiErrorResponse = JSON.parse(error.message.split('Details: ')[1]);
					throw new Error(
						`Failed to update product: ${errorDetails.message || 'Unknown server error'}`
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
	 * Deletes a product by its ID.
	 * @param id The ID of the product to delete.
	 * @returns A promise that resolves to void on successful deletion.
	 * @throws An Error if the deletion fails (e.g., product not found).
	 */
	async deleteById(id: number): Promise<void> {
		try {
			// Assume api.delete returns ApiResponse<any> or a successful status
			const response: ApiResponse<any> = await api.delete(`${PRODUCTS_BASE_PATH}/${id}`);

			if (!response.success) {
				throw new Error(response.message || `Failed to delete product with ID ${id}.`);
			}
			// No need to return data for delete, just confirm success.
		} catch (error: any) {
			console.error(`Error deleting product ${id}:`, error);
			if (error.message.includes('Status: 404')) {
				throw new Error(`Product with ID ${id} not found for deletion.`);
			}
			if (error instanceof Error && error.message.includes('Details: ')) {
				try {
					const errorDetails: ApiErrorResponse = JSON.parse(error.message.split('Details: ')[1]);
					throw new Error(
						`Failed to delete product: ${errorDetails.message || 'Unknown server error'}`
					);
				} catch {
					throw new Error(`Failed to delete product: ${error.message}`);
				}
			}
			throw new Error(
				`An unexpected error occurred while deleting product ${id}. Please try again.`
			);
		}
	}
};
