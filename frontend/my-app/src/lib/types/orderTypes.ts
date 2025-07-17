export interface order {
	id: number;
	client_id: number;
	employee_id: number;
	status: 'Pendiente' | 'Completada' | 'Cancelada'; // Puedes ajustar los estados según tu lógica
	total_price: number;
}

export interface OrderWithInvoice {
	id: number;
	client_id: number;
	total_price: number;
	status: 'Completada' | 'Pendiente' | 'Cancelada' | string;
	employee_id: number;
	created_at: string;
	updated_at: string;
	invoice_link: string;
}
