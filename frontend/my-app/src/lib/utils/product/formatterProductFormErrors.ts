export function formatErrorsToString(errors: Record<string, string>): string {
	// Si el objeto de errores está vacío, retorna una cadena vacía
	if (Object.keys(errors).length === 0) {
		return '';
	}

	// Mapea cada entrada de error a una cadena de "Campo: Mensaje de error"
	const errorMessages = Object.entries(errors).map(([field, message]) => {
		// Puedes capitalizar el nombre del campo para una mejor presentación
		const formattedField =
			field.charAt(0).toUpperCase() + field.slice(1).replace(/([A-Z])/g, ' $1');
		return `${formattedField}: ${message}`;
	});

	// Une todos los mensajes con un salto de línea
	return errorMessages.join('\n');
}
