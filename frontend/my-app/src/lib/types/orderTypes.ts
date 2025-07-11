export interface order {
	id: number;
	client_id: number;
	employee_id: number;
	status: 'Pendiente' | 'Completada' | 'Cancelada'; // Puedes ajustar los estados según tu lógica
	total_price: number;
}
