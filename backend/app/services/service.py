from models import ServiceBase, ProductBase
from crud import ServiceCrud


class ServiceService:
    @classmethod
    async def get_all_services_base(cls) -> list[ServiceBase]:
        """Retrieve all services."""
        
        services = await ServiceCrud.get_all_services()
        return [ServiceBase.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }) for service in services]
        

    @classmethod
    async def get_service_base_by_id(cls, service_id: int) -> ServiceBase:
        """Retrieve a service by ID."""
        service = await ServiceCrud.get_service_by_id(service_id)
        return ServiceBase.model_validate(
            {"id": service.id,
             "name": service.name,
             "short_description": service.short_description,
             "price": service.price,
            }
        )
    
    @classmethod
    async def get_input_services_by_service_id(cls, service_id: int) -> list[ProductBase]:
        """Retrieve input products for a service by service ID."""
        products = await ServiceCrud.get_input_services_by_service(service_id)
        return [ProductBase.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]