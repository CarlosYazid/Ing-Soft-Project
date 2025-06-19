import { BaseProductInterface } from './BaseProductInterface';
import { ConsumibleProduct } from './ConsumibleProductInterface';

export interface ProductInterface extends BaseProductInterface, ConsumibleProduct {
	cost: int;
	img: HTMLImageElement;
}
