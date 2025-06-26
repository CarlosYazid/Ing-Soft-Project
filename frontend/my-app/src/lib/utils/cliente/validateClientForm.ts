// src/lib/utils/clients.ts
import type { client } from '$lib/types';

export function validateClientForm(formData: client, errors: Record<string, string>): boolean {
	// Limpiar errores previos
	Object.keys(errors).forEach((k) => delete errors[k]);

	// 1. Validar documentid: solo dígitos, entre 5 y 20 caracteres
	const idRegex = /^[0-9]{5,20}$/;
	if (!idRegex.test(formData.documentid.toString())) {
		errors.documentid =
			'El documento de identificación debe contener solo dígitos (5–20 caracteres).';
	}

	// 2. Validar name: al menos 3 caracteres alfanuméricos
	const nameRegex = /^(?=.*[\p{L}0-9])[\p{L}\p{N}\s\-'().,;]{3,200}$/u;
	if (!nameRegex.test(formData.name)) {
		errors.name =
			'El nombre debe tener entre 3 y 200 caracteres alfanuméricos, espacios o símbolos comunes.';
	}

	// 3. Validar email: formato básico
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	if (!emailRegex.test(formData.email)) {
		errors.email = 'El correo electrónico no tiene un formato válido.';
	}

	// 4. Validar phone: dígitos, guiones y espacios, entre 7 y 15 caracteres
	const phoneRegex = /^[0-9\s\-]{7,15}$/;
	if (!phoneRegex.test(formData.phone)) {
		errors.phone =
			'El número telefónico debe tener entre 7 y 15 dígitos y puede incluir espacios o guiones.';
	}

	return Object.keys(errors).length === 0;
}
