import { BaseProductInterface } from './baseProductInterface';
import { ConsumibleProduct } from './consumibleProductInterface';

export interface ProductInterface extends BaseProductInterface, ConsumibleProduct {
	cost: int;
	img: string;
}
