import type { Actions } from './$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { productSchema } from '../../lib/components/types/ProductSchema.js';
import { zod } from 'sveltekit-superforms/adapters';

export const load = async () => {
	return {
		form: await superValidate(zod(productSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(productSchema));
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		return {
			form
		};
	}
};
