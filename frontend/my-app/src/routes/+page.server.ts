import type { PageServerLoad } from './$types';
import { productController, serviceController } from '$lib/controllers';

export const load: PageServerLoad = async () => {
	return {
		products: await productController.getAll(),
		services: await serviceController.getAllServices()
	};
};
