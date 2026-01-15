from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Service, ServiceInput
from dtos import ServiceFilter, ServiceInputFilter

class ServiceService:
    
    QUERY_SERVICE_BASE = select(Service)
    QUERY_SERVICE_INPUT_BASE = select(ServiceInput)
    
    @classmethod
    def search_services(cls, filters : ServiceFilter) -> Select:
        """Query that searches for services who meet the filters."""
        return filters.apply(cls.QUERY_SERVICE_BASE)
    
    @classmethod
    def search_service_inputs(cls, filters : ServiceInputFilter) -> Select:
        """Query that searches for services who meet the filters."""
        return filters.apply(cls.QUERY_SERVICE_INPUT_BASE)