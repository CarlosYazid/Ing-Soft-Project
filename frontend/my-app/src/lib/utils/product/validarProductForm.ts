import type { ProductFormInput } from '$lib/types';

export function validateProduct(formData: ProductFormInput) {
	const errors: Record<string, string> = {};

	// 1. Validar Name (string) con Regex
	const nameRegex = /^(?=.*[\p{L}0-9])[\p{L}\p{N}\s\-'().,;]{3,200}$/u;
	if (!nameRegex.test(formData.name)) {
		errors.name =
			'El nombre debe tener entre 3 y 100 caracteres alfanuméricos, espacios o símbolos comunes.';
	}

	// 2. Validar Description (string) con Regex
	const descriptionRegex = /^[\p{L}\p{N}\s\p{P}]{10,1000}$/u;
	if (!descriptionRegex.test(formData.description)) {
		errors.description =
			'La descripción debe tener entre 10 y 500 caracteres, incluyendo puntuación.';
	}

	// 3. Validar Category (string) con Regex
	const categoryRegex = /^[\p{L}\s]{3,50}$/u;
	console.log(`${formData.category}`);
	if (!categoryRegex.test(formData.category)) {
		errors.category = 'La categoría debe tener entre 3 y 50 letras o espacios.';
		console.log(`${formData.category}`);
	}

	// 4. Validar Price (number/Float) - Lógica de programación
	const price = parseFloat(formData.price);
	if (isNaN(price) || price < 0) {
		errors.price = 'El precio debe ser un número positivo (puede tener decimales).';
	}

	// 5. Validar Stock (number/Int) - Lógica de programación
	const stock = parseInt(formData.stock, 10);
	if (isNaN(stock) || !Number.isInteger(stock) || stock < 0) {
		errors.stock = 'El stock debe ser un número entero no negativo.';
	}

	// 6. Validar Cost (int) - Lógica de programación
	const cost = parseInt(formData.cost, 10);
	if (isNaN(cost) || !Number.isInteger(cost) || cost < 0) {
		errors.cost = 'El costo debe ser un número entero no negativo.';
	}

	// 7. Validar Image (File) - Lógica de programación
	if (!formData.img) {
		errors.img = 'Se requiere una imagen.';
	} else {
		const allowedTypes = ['image/jpeg', 'image/png'];
		const maxSizeMB = 5;
		if (!allowedTypes.includes(formData.img.type)) {
			errors.img = 'Tipo de archivo no permitido. Solo JPG o PNG.';
		}
		if (formData.img.size > maxSizeMB * 1024 * 1024) {
			errors.img = `El tamaño de la imagen no debe exceder ${maxSizeMB} MB.`;
		}
	}

	return errors;
}
