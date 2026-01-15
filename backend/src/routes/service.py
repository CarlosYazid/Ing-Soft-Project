from fastapi import APIRouter, Request, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel.ext.asyncio.session import AsyncSession

from models import ServiceInput
from dtos import ServiceCreate, ServiceUpdate, ServiceRead, ServiceFilter, ServiceInputFilter
from crud import ServiceCrud
from db import get_session
from services import AuthService, ServiceService

router = APIRouter(prefix="/service")

@router.post("/", response_model = ServiceRead)
async def create_service(request: Request,
                         service: ServiceCreate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Create a new service.
    """
    return await ServiceCrud.create_service(db_session, service)

@router.get("/{_id}", response_model = ServiceRead)
async def read_service(request : Request,
                       _id: int,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a service by ID.
    """
    return await ServiceCrud.read_service(db_session, _id)

@router.get("/", response_model = ServiceRead)
async def read_service_2(request : Request,
                         id: int,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a service by ID.
    """
    return await ServiceCrud.read_service(db_session, id)

@router.patch("/", response_model = ServiceRead)
async def update_service_2(request: Request, 
                           fields: ServiceUpdate,
                           db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing service by ID.
    """
    return await ServiceCrud.update_service(db_session, fields)

@router.delete("/{_id}")
async def delete_service(request: Request,
                         _id: int,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Delete a service by ID.
    """
    return await ServiceCrud.delete_service(db_session, _id)

@router.delete("/")
async def delete_service_2(request: Request,
                           id: int,
                           db_session: AsyncSession = Depends(get_session)):
    """
    Delete a service by ID.
    """
    return await ServiceCrud.delete_service(db_session, id)

@router.post("/service-input/", response_model = ServiceInput)
async def create_service_input(request: Request,
                               service_input: ServiceInput,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Create a new service input for a specific service.
    """
    return await ServiceCrud.create_service_input(db_session, service_input)

@router.delete("/service-input/")
async def delete_service_input(request: Request,
                               service_input: ServiceInput,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Delete an existing input service by service ID and product ID.
    """
    return await ServiceCrud.delete_service_input(db_session, service_input)

@router.delete("/service-input/{service_id}/{product_id}")
async def delete_service_input_2(request: Request,
                                  service_id: int,
                                  product_id: int,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Delete an existing input service by service ID and product ID.
    """
    return await ServiceCrud.delete_service_input(db_session, ServiceInput(service_id=service_id, product_id=product_id))

@router.post("/search", response_model = Page[ServiceRead])
async def search_services(request: Request,
                          filters: ServiceFilter,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Search services who meet the filters.
    """
    return await apaginate(db_session, ServiceService.search_services(filters))

@router.post("/service-input/search", response_model = Page[ServiceInput])
async def search_service_inputs(request: Request,
                                filters: ServiceInputFilter,
                                db_session: AsyncSession = Depends(get_session)):
    """
    Search service inputs who meet the filters.
    """
    return await apaginate(db_session, ServiceService.search_service_inputs(filters))