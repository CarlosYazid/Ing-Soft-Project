export interface employee {
	id: number;
	documentid: number;
	first_name: string;
	last_name: string;
	name: string;
	email: string;
	phone: string;
	role: 'Empleado' | 'Administrador'; // Puedes ajustar según tu lógica
	state: boolean;
	birth_date: string; // Mantengo como string ISO porque es lo más común
}
