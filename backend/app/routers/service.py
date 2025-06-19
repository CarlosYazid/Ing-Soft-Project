from fastapi import APIRouter, Request, Depends

from models import Service
from crud import ServiceCrud
from services import AuthService, ServiceService


router = APIRouter(prefix="/service")

@router.get("/all")
async def get_services(request: Request):
    return await ServiceCrud.get_all_services()

@router.get("/base/all")
async def get_services_base(request: Request):
    """
    Retrieve all services in base format.
    """
    return await ServiceService.get_all_services_base()

@router.get("/{_id}")
async def get_service_by_id(request : Request, _id: int):
    """
    Retrieve a service by ID.
    """
    return await ServiceCrud.get_service_by_id(_id)

@router.get("/")
async def get_service_by_id_2(request: Request, id: int):
    """
    Retrieve a service by ID.
    """
    return await ServiceCrud.get_service_by_id(id)

@router.get("/base/{_id}")
async def get_service_base_by_id(request: Request, _id: int):
    """
    Get a service base by ID.
    """
    return await ServiceService.get_service_base_by_id(_id)

@router.get("/base/")
async def get_service_base_by_id_2(request: Request, id: int):
    """
    Get a service base by ID.
    """
    return await ServiceService.get_service_base_by_id(id)


@router.post("/")
async def create_service(request: Request, service: Service):
    """
    Create a new service.
    """
    return await ServiceCrud.create_service(service)

@router.post("/{_id}")
async def update_service_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing service by ID.
    """
    return await ServiceCrud.update_service(_id, fields)


@router.delete("/{_id}")
async def delete_service_by_id(request: Request, _id: int):
    """
    Delete a service by ID.
    """
    return await ServiceCrud.delete_service(_id)

@router.delete("/")
async def delete_service_by_id_2(request: Request, id: int):
    """
    Delete a service by ID.
    """
    return await ServiceCrud.delete_service(id)

@router.get("/exists/{_id}")
async def exist_service_by_id(request: Request, _id: int):
    """
    Check if a service exists by ID.
    """
    return await ServiceCrud.exist_service_by_id(_id)

@router.get("/exists/")
async def exist_service_by_id_2(request: Request, id: int):
    """
    Check if a service exists by ID.
    """
    return await ServiceCrud.exist_service_by_id(id)

@router.get("/input_services/{service_id}")
async def get_input_services_by_service_id(request: Request, service_id: int):
    """
    Retrieve input services by service ID.
    """
    return await ServiceCrud.get_input_services_by_service(service_id)

@router.get("/input_services/")
async def get_input_services_by_service_id_2(request: Request, service_id: int):
    """
    Retrieve input services by service ID.
    """
    return await ServiceCrud.get_input_services_by_service(service_id)


@router.get("/input_services/base/{service_id}")
async def get_input_services_base_by_service_id(request: Request, service_id: int):
    """
    Retrieve input services by service ID in base format.
    """
    return await ServiceService.get_input_services_by_service_id(service_id)

@router.get("/input_services/base/")
async def get_input_services_base_by_service_id_2(request: Request, service_id: int):
    """
    Retrieve input services by service ID in base format.
    """
    return await ServiceService.get_input_services_by_service_id(service_id)