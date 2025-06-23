import { BaseProductInterface } from './baseProductInterface';

export interface ConsumibleProduct extends BaseProductInterface {
	expirationDate: string;
}
