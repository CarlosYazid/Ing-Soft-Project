// src/lib/utils/service/validateServiceForm.ts
import type { serviceFormInput } from '$lib/types';

export function validateServiceForm(formData: serviceFormInput): Record<string, string> {
	const errors: Record<string, string> = {};

	// 1. Validar Name (letras, espacios, tildes, ñ), entre 3 y 100 caracteres
	const nameRegex = /^[\p{L}\s]{3,100}$/u;
	if (!formData.name?.trim()) {
		errors.name = 'El nombre es obligatorio.';
	} else if (!nameRegex.test(formData.name.trim())) {
		errors.name = 'El nombre debe tener entre 3 y 100 letras (puede incluir tildes y ñ).';
	}

	// 2. Validar Price (número positivo, opcionalmente con decimales)
	//    Acepta enteros o decimales con hasta 2 dígitos tras la coma/punto
	const priceRegex = /^\d+(\.\d{1,2})?$/;
	if (!formData.price?.trim()) {
		errors.price = 'El precio es obligatorio.';
	} else if (!priceRegex.test(formData.price.trim())) {
		errors.price = 'El precio debe ser un número válido (p.ej. 100 o 49.99).';
	} else if (parseFloat(formData.price) < 0) {
		errors.price = 'El precio no puede ser negativo.';
	}

	return errors;
}
