import { BaseProductInterface } from './BaseProductInterface';

export interface ConsumibleProduct extends BaseProductInterface {
	expirationDate: Date;
}
