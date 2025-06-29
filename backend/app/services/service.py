from models import ServiceBasePlusID, ProductBasePlusID
from crud import ServiceCrud


class ServiceService:
    @classmethod
    async def get_all_services_base(cls) -> list[ServiceBasePlusID]:
        """Retrieve all services."""
        
        services = await ServiceCrud.get_all_services()
        return [ServiceBasePlusID.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }) for service in services]
        

    @classmethod
    async def get_service_base_by_id(cls, service_id: int) -> ServiceBasePlusID:
        """Retrieve a service by ID."""
        service = await ServiceCrud.get_service_by_id(service_id)
        return ServiceBasePlusID.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }
        )
    
    @classmethod
    async def get_input_services_by_service_id(cls, service_id: int) -> list[ProductBasePlusID]:
        """Retrieve input products for a service by service ID."""
        products = await ServiceCrud.get_input_services_by_service(service_id)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
        
    @classmethod
    async def search_service_by_name(cls, name: str) -> list[ServiceBasePlusID]:
        """Search for services by name."""
        services = await ServiceCrud.search_service_by_name(name)
        return [ServiceBasePlusID.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }) for service in services]
        
    @classmethod
    async def search_service_by_price_range(cls, min_price: float, max_price: float) -> list[ServiceBasePlusID]:
        """Search for services by price range."""
        services = await ServiceCrud.search_service_by_price_range(min_price, max_price)
        return [ServiceBasePlusID.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }) for service in services]
        
    @classmethod
    async def search_service_by_cost_range(cls, min_cost: float, max_cost: float) -> list[ServiceBasePlusID]:
        """Search for services by cost range."""
        services = await ServiceCrud.search_service_by_cost_range(min_cost, max_cost)
        return [ServiceBasePlusID.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }) for service in services]