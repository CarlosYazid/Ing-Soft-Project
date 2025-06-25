/**
 * @interface ApiResponse
 * @description Interfaz genérica para el formato de respuesta común de tu API,
 * que envuelve los datos reales y puede incluir metadatos o mensajes.
 * Adaptar si tu backend usa un formato de envoltura para todas las respuestas.
 */
export interface ApiResponse<T> {
	data: T;
	message?: string;
	success: boolean;
	// ... otros campos comunes en tus respuestas de API
}

/**
 * @interface ApiErrorResponse
 * @description Define la estructura de una respuesta de error común de tu API.
 */
export interface ApiErrorResponse {
	statusCode: number;
	message: string;
}
