from fastapi import HTTPException

from db import get_db_client
from models import UserBase, Employee, Client, EmployeeCreate, ClientCreate
from core import SETTINGS
from utils import UserUtils

class UserCrud:
    """CRUD operations for users"""
    
    EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE = {"created_at"}
    ALLOWED_FIELDS_FOR_UPDATE_EMPLOYEE = set(EmployeeCreate.__fields__.keys()) - EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE

    EXCLUDED_FIELDS_FOR_UPDATE_CLIENT = {"created_at"}
    ALLOWED_FIELDS_FOR_UPDATE_CLIENT = set(ClientCreate.__fields__.keys()) - EXCLUDED_FIELDS_FOR_UPDATE_CLIENT

    @classmethod
    async def create_employee(cls, employee : EmployeeCreate) -> Employee:
        """Create a new employee."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).insert(employee.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee creation failed", status_code=500)
        
        return Employee.model_validate(response.data[0])

    @classmethod
    async def read_all_employees(cls) -> list[Employee]:
        """Retrieve all employees."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def read_all_employees_base(cls) -> list[UserBase]:
        """Retrieve all employees."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").execute()
        
        if not bool(response.data):
            raise HTTPException(detail="No employees found", status_code=404)
        
        return [UserBase.model_validate(employee) for employee in response.data]

    @classmethod
    async def read_employee(cls, employee_id: int) -> Employee:
        """Retrieve an employee by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("id", employee_id).execute()

        if not bool(response.data):

            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def read_employee_base(cls, employee_id: int) -> UserBase:
        """Retrieve a user by ID."""
        
        client = await get_db_client()
        
        response = await client.table(SETTINGS.employee_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").eq("id", employee_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee not found", status_code=404)

        return UserBase.model_validate(response.data[0])

    @classmethod
    async def read_employee_by_email(cls, email: str) -> Employee:
        """Retrieve an employee by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])
    
    @classmethod
    async def read_employee_base_by_email(cls, email: str) -> UserBase:
        """Retrieve a user by email."""
        
        client = await get_db_client()
        
        response = await client.table(SETTINGS.employee_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee not found", status_code=404)

        return UserBase.model_validate(response.data[0])
    
    @classmethod
    async def read_employee_by_documentid(cls, document_id: int) -> Employee:
        """Retrieve an employee by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])
    
    @classmethod
    async def read_employee_base_by_documentid(cls, documentid: str) -> UserBase:
        """Retrieve a user by document ID."""
        client = await get_db_client()
        
        response = await client.table(SETTINGS.employee_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").eq("documentid", documentid).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee not found", status_code=404)

        return UserBase.model_validate(response.data[0])

    @classmethod
    async def update_employee(cls, _id: int, fields: dict) -> Employee:
        """Update an existing employee."""
        
        if not await UserUtils.exist_employee(_id):
            raise HTTPException(detail="Employee not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE), status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE_EMPLOYEE):
            raise HTTPException(detail="Update attribute of employee", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).update(fields).eq("id", _id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee update failed", status_code=500)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def update_employee_by_email(cls, email: str, fields: dict) -> Employee:
        """Update an existing employee by email."""

        if not await UserUtils.exist_employee_by_email(email):
            raise HTTPException(detail="Employee not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE), status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE_EMPLOYEE):
            raise HTTPException(detail="Update attribute of employee", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).update(fields).eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee update failed", status_code=500)

        return Employee.model_validate(response.data[0])
    
    @classmethod
    async def update_employee_by_documentid(cls, document_id: int, fields: dict) -> Employee:
        """Update an existing employee by document ID."""

        if not await UserUtils.exist_employee_by_documentid(document_id):
            raise HTTPException(detail="Employee not found", status_code=404)

        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_EMPLOYEE), status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE_EMPLOYEE):
            raise HTTPException(detail="Update fields are invalid", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).update(fields).eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee update failed", status_code=500)

        return Employee.model_validate(response.data[0])
    
    @classmethod
    async def delete_employee(cls, employee_id: int) -> bool:
        """Delete an employee by ID."""
        
        if not await UserUtils.exist_employee(employee_id):
            raise HTTPException(detail="Employee not found", status_code=404)

        # check if the employee have any orders
        from utils import OrderUtils
        
        if await OrderUtils.exist_orders_by_employee_id(employee_id):
            raise HTTPException(detail="Cannot delete employee with active orders", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("id", employee_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee deletion failed", status_code=500)

        return bool(response.data)
    
    @classmethod
    async def delete_employee_by_email(cls, email: str) -> bool:
        """Delete an employee by email."""
        
        if not await UserUtils.exist_employee_by_email(email):
            raise HTTPException(detail="Employee not found", status_code=404)
        
        id_ = await UserUtils.translate_email_by_employee_id(email)
        
        # check if the employee have any orders
        from utils import OrderUtils
        
        if await OrderUtils.exist_orders_by_employee_id(id_):
            raise HTTPException(detail="Cannot delete employee with active orders", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee deletion failed", status_code=500)

        return bool(response.data)

    @classmethod
    async def delete_employee_by_documentid(cls, document_id: int) -> bool:
        """Delete an employee by document ID."""
        
        if not await UserUtils.exist_employee_by_documentid(document_id):
            raise HTTPException(detail="Employee not found", status_code=404)

        id_ = await UserUtils.translate_documentid_by_employee_id(document_id)

        # check if the employee have any orders
        from utils import OrderUtils
        
        if await OrderUtils.exist_orders_by_employee_id(id_):
            raise HTTPException(detail="Cannot delete employee with active orders", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Employee deletion failed", status_code=500)

        return bool(response.data)

    @classmethod
    async def create_client(cls, client_: ClientCreate) -> Client:
        """Create a new client."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).insert(client_.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client creation failed", status_code=500)
        
        return Client.model_validate(response.data[0])
    
    @classmethod
    async def read_all_clients(cls) -> list[Client]:
        """Retrieve all clients."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No clients found", status_code=404)

        return [Client.model_validate(client) for client in response.data]
    
    @classmethod
    async def read_all_clients_base(cls) -> list[UserBase]:
        """Retrieve all clients."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").execute()

        if not bool(response.data):
            raise HTTPException(detail="No clients found", status_code=404)

        return [UserBase.model_validate(client) for client in response.data]
    
    @classmethod
    async def read_client(cls, client_id: int) -> Client:
        """Retrieve a client by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("id", client_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def read_client_base(cls, client_id: int) -> UserBase:
        """Retrieve a client by ID."""
        
        client = await get_db_client()
        
        response = await client.table(SETTINGS.client_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").eq("id", client_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client not found", status_code=404)

        return UserBase.model_validate(response.data[0])
    
    @classmethod
    async def read_client_by_email(cls, email: str) -> Client:
        """Retrieve a client by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def read_client_base_by_email(cls, email: str) -> UserBase:
        """Retrieve a client by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client not found", status_code=404)

        return UserBase.model_validate(response.data[0])
    
    @classmethod
    async def read_client_by_documentid(cls, document_id: int) -> Client:   
        """Retrieve a client by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def read_client_base_by_documentid(cls, documentid: str) -> UserBase:
        """Retrieve a client by document ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email", "name", "phone", "created_at", "updated_at", "state", "documentid").eq("documentid", documentid).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client not found", status_code=404)

        return UserBase.model_validate(response.data[0])
    
    @classmethod
    async def update_client(cls, _id: int, fields: dict) -> Client:
        """Update an existing client."""

        if not await UserUtils.exist_client(_id):
            raise HTTPException(detail="Client not found", status_code=404)

        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_CLIENT):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_CLIENT), status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE_CLIENT):
            raise HTTPException(detail="Update attribute of client", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).update(fields).eq("id", _id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client update failed", status_code=500)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_email(cls, email: str, fields: dict) -> Client:
        """Update an existing client by email."""

        if not await UserUtils.exist_client_by_email(email):
            raise HTTPException(detail="Client not found", status_code=404)

        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_CLIENT):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_CLIENT), status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE_CLIENT):
            raise HTTPException(detail="Update attribute of client", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).update(fields).eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client update failed", status_code=500)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_documentid(cls, document_id: int, fields: dict) -> Client:
        """Update an existing client by document ID."""

        if not await UserUtils.exist_client_by_documentid(document_id):
            raise HTTPException(detail="Client not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_CLIENT):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_CLIENT), status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE_CLIENT):
            raise HTTPException(detail="Update fields are invalid", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).update(fields).eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Client update failed", status_code=500)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def delete_client(cls, client_id: int) -> bool:
        """Delete a client by ID."""
        
        # check if the client exists
        if not await UserUtils.exist_client(client_id):
            raise HTTPException(detail="Client not found", status_code=404)
        
        from utils import OrderUtils
        
        if await OrderUtils.exist_order_by_client_id(client_id):
            raise HTTPException(detail="Cannot delete client with active orders", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).delete().eq("id", client_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed delete client", status_code=500)

        return bool(response.data)
    
    @classmethod
    async def delete_client_by_email(cls, email: str) -> bool:
        """Delete a client by email."""
        
        # check if the client exists
        if not await UserUtils.exist_client_by_email(email):
            raise HTTPException(detail="Client not found", status_code=404)
        
        from utils import OrderUtils
        
        _id = await UserUtils.translate_email_by_client_id(email)

        if await OrderUtils.exist_order_by_client_id(_id):
            raise HTTPException(detail="Cannot delete client with active orders", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).delete().eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed delete client", status_code=500)

        return bool(response.data)
      
    @classmethod
    async def delete_client_by_documentid(cls, document_id: int) -> bool:
        """Delete a client by document ID."""

        
        # check if the client exists
        if not await UserUtils.exist_client_by_documentid(document_id):
            raise HTTPException(detail="Client not found", status_code=404)
        
        from utils import OrderUtils
        
        _id = await UserUtils.translate_documentid_by_client_id(document_id)
        
        if await OrderUtils.exist_order_by_client_id(_id):
            raise HTTPException(detail="Cannot delete client with active orders", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).delete().eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed delete client", status_code=500)

        return bool(response.data)