from fastapi import APIRouter, Request, Depends

from models import ServiceCreate, ServiceInputCreate
from crud import ServiceCrud
from services import AuthService, ServiceService


router = APIRouter(prefix="/service")


@router.post("/")
async def create_service(request: Request, service: ServiceCreate):
    """
    Create a new service.
    """
    return await ServiceCrud.create_service(service)

@router.get("/all")
async def read_all_services(request: Request):
    """
    Retrieve all services.
    """
    return await ServiceCrud.read_all_services()

@router.get("/base/all")
async def read_all_services_base(request: Request):
    """
    Retrieve all services in base format.
    """
    return await ServiceCrud.read_all_services_base()

@router.get("/{_id}")
async def read_service(request : Request, _id: int):
    """
    Retrieve a service by ID.
    """
    return await ServiceCrud.read_service(_id)

@router.get("/")
async def read_service_2(request: Request, id: int):
    """
    Retrieve a service by ID.
    """
    return await ServiceCrud.read_service(id)

@router.get("/base/{_id}")
async def read_service_base(request: Request, _id: int):
    """
    Get a service base by ID.
    """
    return await ServiceCrud.read_service_base(_id)

@router.get("/base/")
async def read_service_base_2(request: Request, id: int):
    """
    Get a service base by ID.
    """
    return await ServiceCrud.read_service_base(id)

@router.put("/{_id}")
async def update_service(request: Request, _id: int, fields: dict):
    """
    Update an existing service by ID.
    """
    return await ServiceCrud.update_service(_id, fields)

@router.put("/")
async def update_service_2(request: Request, id: int, fields: dict):
    """
    Update an existing service by ID.
    """
    return await ServiceCrud.update_service(id, fields)


@router.delete("/{_id}")
async def delete_service(request: Request, _id: int):
    """
    Delete a service by ID.
    """
    return await ServiceCrud.delete_service(_id)

@router.delete("/")
async def delete_service_2(request: Request, id: int):
    """
    Delete a service by ID.
    """
    return await ServiceCrud.delete_service(id)

@router.post("/input_service/")
async def create_input_service(request: Request, input_service: ServiceInputCreate):
    """
    Create a new input service for a specific service ID.
    """
    return await ServiceCrud.create_service_input(input_service)

@router.get("/input_service/product/{product_id}")
async def read_input_services_by_product(request: Request, product_id: int):
    """
    Retrieve input services by product ID.
    """
    return await ServiceCrud.read_services_inputs_by_product(product_id)

@router.get("/input_service/product/")
async def read_input_services_by_product_2(request: Request, product_id: int):
    """
    Retrieve input services by product ID.
    """
    return await ServiceCrud.read_services_inputs_by_product(product_id)


@router.get("/input_service/service/{service_id}")
async def read_input_services_by_service(request: Request, service_id: int):
    """
    Retrieve input services by service ID.
    """
    return await ServiceCrud.read_services_inputs_by_service(service_id)

@router.get("/input_service/service/")
async def read_input_services_by_service_2(request: Request, service_id: int):
    """
    Retrieve input services by service ID.
    """
    return await ServiceCrud.read_services_inputs_by_service(service_id)

@router.get("/input_service/{service_id}/{product_id}")
async def read_input_services_by_service_and_product(request: Request, service_id: int, product_id: int):
    """
    Retrieve input services by service ID and product ID.
    """
    return await ServiceCrud.read_service_input_by_service_id_and_product_id(service_id, product_id)

@router.get("/input_service/{_id}")
async def read_input_service(request: Request, _id: int):
    """
    Retrieve an input service by ID.
    """
    return await ServiceCrud.read_service_input(_id)

@router.get("/input_service/")
async def read_input_service_2(request: Request, id: int):
    """
    Retrieve an input service by ID.
    """
    return await ServiceCrud.read_service_input(id)

@router.put("/input_service/{_id}")
async def update_input_service(request: Request, _id: int, fields: dict):
    """
    Update an existing input service.
    """
    return await ServiceCrud.update_service_input(_id, fields)

@router.put("/input_service/")
async def update_input_service_2(request: Request, _id : int, fields: dict):
    """
    Update an existing input service.
    """
    return await ServiceCrud.update_service_input(_id, fields)

@router.put("/input_service/{service_id}/{product_id}")
async def update_input_service_by_service_and_product(request: Request, service_id: int, product_id: int, fields: dict):
    """ Update an existing input service by service ID and product ID.
    """
    return await ServiceCrud.update_service_input_by_service_id_and_product_id(service_id, product_id, fields)

@router.delete("/input_service/{_id}")
async def delete_input_service(request: Request, _id: int):
    """
    Delete an existing input service.
    """
    return await ServiceCrud.delete_service_input(_id)

@router.delete("/input_service/")
async def delete_input_service_2(request: Request, _id : int):
    """
    Delete an existing input service.
    """
    return await ServiceCrud.delete_service_input(_id)

@router.delete("/input_service/{service_id}/{product_id}")
async def delete_input_service_by_service_and_product(request: Request, service_id: int, product_id: int):
    """
    Delete an existing input service by service ID and product ID.
    """
    return await ServiceCrud.delete_service_input_by_service_id_and_product_id(service_id, product_id)

@router.get("/search/name/{name}")
async def search_services_by_name(request: Request, name: str):
    """
    Search for services by name.
    """
    return await ServiceService.search_services_by_name(name)

@router.get("/search/name/")
async def search_services_by_name_2(request: Request, name: str):
    """
    Search for services by name.
    """
    return await ServiceService.search_services_by_name(name)


@router.get("/search/price_range/{min_price}/{max_price}")
async def search_services_by_price_range(request: Request, min_price: float, max_price: float):
    """
    Search for services by price range.
    """
    return await ServiceService.search_services_by_price_range(min_price, max_price)

@router.get("/search/price_range/")
async def search_services_by_price_range_2(request: Request, min_price: float, max_price: float):
    """
    Search for services by price range.
    """
    return await ServiceService.search_services_by_price_range(min_price, max_price)

@router.get("/search/cost_range/{min_cost}/{max_cost}")
async def search_services_by_cost_range(request: Request, min_cost: float, max_cost: float):
    """
    Search for services by cost range.
    """
    return await ServiceService.search_services_by_cost_range(min_cost, max_cost)

@router.get("/search/cost_range/")
async def search_services_by_cost_range_2(request: Request, min_cost: float, max_cost: float):
    """
    Search for services by cost range.
    """
    return await ServiceService.search_services_by_cost_range(min_cost, max_cost)
