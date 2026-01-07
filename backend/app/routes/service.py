from fastapi import APIRouter, Request, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from models import ServiceCreate, ServiceUpdate, ServiceRead, ServiceInput
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

@router.get("/all", response_model = list[ServiceRead])
async def read_all_services(request: Request,
                            db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve all services.
    """
    return await ServiceCrud.read_all_services(db_session)

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

@router.put("/", response_model = ServiceRead)
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

@router.post("/service_input/", response_model = ServiceInput)
async def create_service_input(request: Request,
                               service_input: ServiceInput,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Create a new service input for a specific service.
    """
    return await ServiceCrud.create_service_input(db_session, service_input)

@router.get("/service_input/product/{product_id}", response_model = list[ServiceInput])
async def read_service_inputs_by_product(request: Request,
                                         product_id: int,
                                         db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve input services by product ID.
    """
    return await ServiceCrud.read_service_inputs_by_product(db_session, product_id)

@router.get("/service_input/product/", response_model = list[ServiceInput])
async def read_service_inputs_by_product_2(request: Request,
                                           product_id: int,
                                           db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve input services by product ID.
    """
    return await ServiceCrud.read_service_inputs_by_product(db_session, product_id)

@router.get("/service_input/service/{service_id}", response_model = list[ServiceInput])
async def read_service_inputs_by_service(request: Request,
                                         service_id: int,
                                         db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve input services by service ID.
    """
    return await ServiceCrud.read_service_inputs_by_service(db_session, service_id)

@router.get("/service_input/service/", response_model = list[ServiceInput])
async def read_service_inputs_by_service_2(request: Request,
                                           service_id: int,
                                           db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve input services by service ID.
    """
    return await ServiceCrud.read_service_inputs_by_service(db_session, service_id)


@router.delete("/service_input/")
async def delete_service_input(request: Request,
                               service_input: ServiceInput,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Delete an existing input service by service ID and product ID.
    """
    return await ServiceCrud.delete_service_input(db_session, service_input)

@router.delete("/service_input/{service_id}/{product_id}")
async def delete_service_input_2(request: Request,
                                  service_id: int,
                                  product_id: int,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Delete an existing input service by service ID and product ID.
    """
    return await ServiceCrud.delete_service_input(db_session, ServiceInput(service_id=service_id, product_id=product_id))

@router.get("/search/name/{name}", response_model = ServiceInput)
async def search_services_by_name(request: Request,
                                  name: str,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Search for services by name.
    """
    return await ServiceService.search_services_by_name(db_session, name)

@router.get("/search/name/", response_model = ServiceInput)
async def search_services_by_name_2(request: Request,
                                    name: str,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Search for services by name.
    """
    return await ServiceService.search_services_by_name(db_session, name)

@router.get("/search/price_range/{min_price}/{max_price}", response_model = ServiceInput)
async def search_services_by_price_range(request: Request,
                                         min_price: float,
                                         max_price: float,
                                         db_session: AsyncSession = Depends(get_session)):
    """
    Search for services by price range.
    """
    return await ServiceService.search_services_by_price_range(db_session, min_price, max_price)

@router.get("/search/price_range/", response_model = ServiceInput)
async def search_services_by_price_range_2(request: Request, 
                                           min_price: float, 
                                           max_price: float,
                                           db_session: AsyncSession = Depends(get_session)):
    """
    Search for services by price range.
    """
    return await ServiceService.search_services_by_price_range(db_session, min_price, max_price)

@router.get("/search/cost_range/{min_cost}/{max_cost}", response_model = ServiceInput)
async def search_services_by_cost_range(request: Request,
                                        min_cost: float,
                                        max_cost: float,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Search for services by cost range.
    """
    return await ServiceService.search_services_by_cost_range(db_session, min_cost, max_cost)

@router.get("/search/cost_range/", response_model = ServiceInput)
async def search_services_by_cost_range_2(request: Request,
                                          min_cost: float,
                                          max_cost: float,
                                          db_session: AsyncSession = Depends(get_session)):
    """
    Search for services by cost range.
    """
    return await ServiceService.search_services_by_cost_range(db_session, min_cost, max_cost)
