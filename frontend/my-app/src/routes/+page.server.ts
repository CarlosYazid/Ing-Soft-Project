import type { PageServerLoad } from './$types';
import { productController, serviceController } from '$lib/controllers';

export const load: PageServerLoad = async () => {
	return {
		services: await serviceController.getAllServices(),
		products: await productController.getAll()
	};
};
