import type { ProductFormInput } from '$lib/types';

export function validateProduct(formData: ProductFormInput) {
	const errors: Record<string, string> = {};

	// 1. Validar Name (string) con Regex
	const nameRegex = /^(?=.*[a-zA-Z0-9])[\w\s\-'().]{3,100}$/;
	if (!nameRegex.test(formData.name)) {
		errors.name =
			'El nombre debe tener entre 3 y 100 caracteres alfanuméricos, espacios o símbolos comunes.';
	}

	// 2. Validar Description (string) con Regex
	const descriptionRegex = /^[\w\s\p{P}]{10,500}$/u; // `u` flag for unicode property escape
	if (!descriptionRegex.test(formData.description)) {
		errors.description =
			'La descripción debe tener entre 10 y 500 caracteres, incluyendo puntuación.';
	}

	// 3. Validar Category (string) con Regex
	const categoryRegex = /^[a-zA-Z\s]{3,50}$/;
	if (!categoryRegex.test(formData.category)) {
		errors.category = 'La categoría debe tener entre 3 y 50 letras o espacios.';
	}

	// 4. Validar ID (number/Int) - Lógica de programación
	const id = formData.id;
	if (isNaN(id) || !Number.isInteger(id) || id <= 0) {
		errors.id = 'El ID debe ser un número entero positivo.';
	}

	// 5. Validar Price (number/Float) - Lógica de programación
	const price = parseFloat(formData.price);
	if (isNaN(price) || price < 0) {
		errors.price = 'El precio debe ser un número positivo (puede tener decimales).';
	}

	// 6. Validar Stock (number/Int) - Lógica de programación
	const stock = parseInt(formData.stock, 10);
	if (isNaN(stock) || !Number.isInteger(stock) || stock < 0) {
		errors.stock = 'El stock debe ser un número entero no negativo.';
	}

	// 7. Validar Cost (int) - Lógica de programación
	const cost = parseInt(formData.cost, 10);
	if (isNaN(cost) || !Number.isInteger(cost) || cost < 0) {
		errors.cost = 'El costo debe ser un número entero no negativo.';
	}

	// 8. Validar Expiration Date (number/timestamp) - Lógica de programación
	// Asumiendo que formData.expirationDate es un string de fecha (ej. "2025-12-31")
	// y quieres convertirlo a un timestamp o validarlo como fecha válida.
	if (formData?.expirationDate) {
		const expirationTimestamp = new Date(formData.expirationDate).getTime();
		if (isNaN(expirationTimestamp) || expirationTimestamp < Date.now()) {
			errors.expirationDate = 'La fecha de expiración debe ser una fecha válida y futura.';
		}
	}
	// Si expirationDate ya viene como number (timestamp), la validación sería:
	// if (typeof formData.expirationDate !== 'number' || isNaN(formData.expirationDate) || formData.expirationDate < Date.now()) {
	//    errors.expirationDate = 'La fecha de expiración debe ser un timestamp numérico válido y futuro.';
	// }

	// 9. Validar Image (File) - Lógica de programación
	if (!formData.picture) {
		// errors.picture = 'Se requiere una imagen.'; // Si es obligatorio
	} else {
		const allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
		const maxSizeMB = 5;
		if (!allowedTypes.includes(formData.picture.type)) {
			errors.picture = 'Tipo de archivo no permitido. Solo JPG, PNG o GIF.';
		}
		if (formData.picture.size > maxSizeMB * 1024 * 1024) {
			errors.picture = `El tamaño de la imagen no debe exceder ${maxSizeMB} MB.`;
		}
	}

	return errors;
}
