// src/lib/product/mappers.ts (or within productController.ts)

import type { BaseProductInterface, ProductInterface } from '$lib/types';
import type { BackendBaseProduct, BackendProduct } from '$lib/types/ProductResponses';

/**
 * Transforms a `BackendProductBase` object from the API into a `ProductBase` object
 * suitable for frontend consumption.
 * @param backendProductBase The product base object from the backend.
 * @returns The transformed ProductBase object.
 */
export function mapBackendProductBaseToProductBase(
	backendProductBase: BackendBaseProduct
): BaseProductInterface {
	return {
		id: backendProductBase.id,
		name: backendProductBase.name,
		description: backendProductBase.short_description,
		price: backendProductBase.price,
		category: backendProductBase.category,
		stock: backendProductBase.stock,
		img: backendProductBase.image_url
	};
}

/**
 * Transforms a `BackendProduct` object from the API into a `Product` object
 * suitable for frontend consumption, handling date conversions and name changes.
 * @param backendProduct The full product object from the backend.
 * @returns The transformed Product object.
 */
export function mapBackendProductToProduct(backendProduct: BackendProduct): ProductInterface {
	return {
		id: backendProduct.id,
		name: backendProduct.name,
		price: backendProduct.price,
		category: backendProduct.category,
		stock: backendProduct.stock,
		img: backendProduct.image_url,
		description: backendProduct.description,
		cost: backendProduct.cost,
		expirationDate: new Date(backendProduct.expiration_date),
		quantity: 0,
		quantityService: 0
	};
}
