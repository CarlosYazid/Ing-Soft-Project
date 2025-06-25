// src/lib/http/api.ts

// Importa las variables de entorno de SvelteKit.
// Usamos 'public' si la URL base es pública y conocida por el cliente.
// Si es una API privada que solo se accede desde el servidor (en hooks de SvelteKit, por ejemplo),
// podrías usar '$env/dynamic/private'. Para la mayoría de los casos de frontend, public es suficiente.
import { PUBLIC_BACKEND_BASE_URL } from '$env/static/public';

// Define la URL base de tu backend.
// Se recomienda usar una variable de entorno para esto.
// Asegúrate de que PUBLIC_BACKEND_BASE_URL esté definida en tu archivo .env, por ejemplo:
// PUBLIC_BACKEND_BASE_URL="https://api.tudominio.com"
export const BASE_URL = PUBLIC_BACKEND_BASE_URL;

/**
 * Realiza una petición GET.
 * @param path El path relativo al endpoint (ej. '/users', '/products/1').
 * @param options Opciones adicionales para la petición fetch.
 * @returns La respuesta parseada como JSON.
 * @throws Error si la respuesta no es OK.
 */
async function get(path: string, options?: RequestInit): Promise<any> {
	const response = await fetch(`${BASE_URL}${path}`, { ...options, method: 'GET', mode: 'cors' });
	if (!response.ok) {
		// Podrías añadir más lógica de manejo de errores aquí, como parsear un cuerpo de error JSON
		// si tu backend envía errores detallados en el body.
		const errorData = await response.json().catch(() => ({ message: response.statusText }));
		throw new Error(
			`HTTP error! Status: ${response.status}, Details: ${JSON.stringify(errorData)}`
		);
	}
	return response.json();
}

/**
 * Realiza una petición POST.
 * @param path El path relativo al endpoint.
 * @param data Los datos a enviar en el cuerpo de la petición (se serializan a JSON).
 * @returns La respuesta parseada como JSON.
 * @throws Error si la respuesta no es OK.
 */
async function post(path: string, data: any): Promise<any> {
	const response = await fetch(`${BASE_URL}${path}`, {
		method: 'POST',
		mode: 'cors',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	});
	if (!response.ok) {
		const errorData = await response.json().catch(() => ({ message: response.statusText }));
		throw new Error(
			`HTTP error! Status: ${response.status}, Details: ${JSON.stringify(errorData)}`
		);
	}
	return response.json();
}

/**
 * Realiza una petición PUT.
 * @param path El path relativo al endpoint.
 * @param data Los datos a enviar en el cuerpo de la petición (se serializan a JSON).
 * @param options Opciones adicionales para la petición fetch.
 * @returns La respuesta parseada como JSON.
 * @throws Error si la respuesta no es OK.
 */
async function put(path: string, data: any, options?: RequestInit): Promise<any> {
	const response = await fetch(`${BASE_URL}${path}`, {
		...options,
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json',
			...(options?.headers || {})
		},
		body: JSON.stringify(data)
	});
	if (!response.ok) {
		const errorData = await response.json().catch(() => ({ message: response.statusText }));
		throw new Error(
			`HTTP error! Status: ${response.status}, Details: ${JSON.stringify(errorData)}`
		);
	}
	return response.json();
}

/**
 * Realiza una petición DELETE.
 * @param path El path relativo al endpoint.
 * @param options Opciones adicionales para la petición fetch.
 * @returns La respuesta parseada como JSON (puede ser un objeto vacío o un mensaje de éxito).
 * @throws Error si la respuesta no es OK.
 */
async function del(path: string, options?: RequestInit): Promise<any> {
	const response = await fetch(`${BASE_URL}${path}`, { ...options, method: 'DELETE' });
	if (!response.ok) {
		const errorData = await response.json().catch(() => ({ message: response.statusText }));
		throw new Error(
			`HTTP error! Status: ${response.status}, Details: ${JSON.stringify(errorData)}`
		);
	}
	// Una petición DELETE exitosa a menudo no devuelve contenido,
	// o devuelve un estado 204 No Content.
	// Intentamos parsear como JSON pero no es un error si falla.
	return response.json().catch(() => ({ message: 'Delete successful, no content returned.' }));
}

// Exporta un objeto `api` que contiene todos los métodos de petición,
// y también la BASE_URL directamente.
export const api = {
	get,
	post,
	put,
	delete: del // 'delete' es una palabra reservada en JS, por eso usamos 'del' como nombre de función y lo mapeamos.
};

// Si necesitas un lugar para configurar headers globales como tokens de autorización:
/*
export const setAuthToken = (token: string) => {
    // Esto es un ejemplo, necesitarías pasar headers en cada llamada o usar un patrón de factoría
    // o interceptores si usas una librería como axios.
    // Con fetch nativo, lo más común es pasar el header en las opciones de cada llamada.
};
*/
