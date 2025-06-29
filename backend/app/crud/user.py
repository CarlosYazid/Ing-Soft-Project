from fastapi import HTTPException
from datetime import date

from db import get_db_client
from models import Employee, Client, EmployeeCreate, ClientCreate, EmployeeRole
from core import SETTINGS

class UserCrud:
    """CRUD operations for users"""

    @classmethod
    async def get_all_employees(cls) -> list[Employee]:
        """Retrieve all employees."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    
    @classmethod
    async def create_employee(cls, employee : EmployeeCreate) -> Employee:
        """Create a new employee."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).insert(employee.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee creation failed", status_code=400)
        return Employee.model_validate(response.data[0])

    @classmethod
    async def update_employee_by_id(cls, _id: int, fields: dict) -> Employee:
        """Update an existing employee."""

        client = await get_db_client()
        
        
        if not(set(fields.keys()) < set(EmployeeCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of employee", status_code=400)

        response = await client.table(SETTINGS.employee_table).update(fields).eq("id", _id).execute()

        if not(bool(response.data)):

            if not cls.exist_employee_by_id(_id):
                raise HTTPException(detail="Employee not found", status_code=404)

            raise HTTPException(detail="Employee update failed", status_code=400)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def update_employee_by_email(cls, email: str, fields: dict) -> Employee:
        """Update an existing employee by email."""

        client = await get_db_client()
        
        if not(set(fields.keys()) < set(EmployeeCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of employee", status_code=400)

        response = await client.table(SETTINGS.employee_table).update(fields).eq("email", email).execute()

        if not(bool(response.data)):

            if not cls.exist_employee_by_email(email):
                raise HTTPException(detail="Employee not found", status_code=404)

            raise HTTPException(detail="Employee update failed", status_code=400)

        return Employee.model_validate(response.data[0])
    
    @classmethod
    async def update_employee_by_documentid(cls, document_id: int, fields: dict) -> Employee:
        """Update an existing employee by document ID."""

        client = await get_db_client()

        if not(set(fields.keys()) < set(EmployeeCreate.__fields__.keys())):
            raise HTTPException(detail="Update fields are invalid", status_code=400)

        response = await client.table(SETTINGS.employee_table).update(fields).eq("documentid", document_id).execute()

        if not(bool(response.data)):

            if not cls.exist_employee_by_documentid(document_id):
                raise HTTPException(detail="Employee not found", status_code=404)

            raise HTTPException(detail="Employee update failed", status_code=400)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def read_employee_by_id(cls, employee_id: int) -> Employee:
        """Retrieve an employee by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("id", employee_id).execute()

        if not(bool(response.data)):

            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def read_employee_by_email(cls, email: str) -> Employee:
        """Retrieve an employee by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])
    
    
    @classmethod
    async def read_employee_by_documentid(cls, document_id: int) -> Employee:
        """Retrieve an employee by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("documentid", document_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def exist_employee_by_email(cls, email: str) -> bool:
        """Check if an employee exists by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("email").eq("email", email).execute()

        return bool(response.data)

    @classmethod
    async def exist_employee_by_id(cls, employee_id: int) -> bool:
        """Check if an employee exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("id").eq("id", employee_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_employee_by_documentid(cls, document_id: int) -> bool:
        """Check if an employee exists by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("documentid").eq("documentid", document_id).execute()

        return bool(response.data)

    @classmethod
    async def delete_employee_by_id(cls, employee_id: int) -> bool:
        """Delete an employee by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("id", employee_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return True
    @classmethod
    async def delete_employee_by_email(cls, email: str) -> bool:
        """Delete an employee by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return True

    @classmethod
    async def delete_employee_by_documentid(cls, document_id: int) -> bool:
        """Delete an employee by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("documentid", document_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return True
    
    @classmethod
    async def search_employee_by_name(cls, name: str) -> list[Employee]:
        """Search employees by name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").ilike("name", f"%{name}%").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given name", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]

    @classmethod
    async def search_employee_by_birthday(cls, birthday: date) -> list[Employee]:
        """Search employees by birthday."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("birth_date", birthday.isoformat()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given birthday", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]

    @classmethod
    async def search_employee_by_status(cls, status: bool) -> list[Employee]:
        """Search employees by status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("state", status).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given status", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]

    @classmethod
    async def search_employee_by_role(cls, role: EmployeeRole) -> list[Employee]:
        """Search employees by role."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("role", role.capitalize()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given role", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employee_by_name_and_role(cls, name: str, role: EmployeeRole) -> list[Employee]:
        """Search employees by name and role."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").ilike("name", f"%{name}%").eq("role", role.capitalize()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given name and role", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employee_by_name_and_status(cls, name: str, status: bool) -> list[Employee]:
        """Search employees by name and status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").ilike("name", f"%{name}%").eq("state", status).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given name and status", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employee_by_name_and_birthday(cls, name: str, birthday: date) -> list[Employee]:
        """Search employees by name and birthday."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").ilike("name", f"%{name}%").eq("birth_date", birthday.isoformat()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given name and birthday", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    
    @classmethod
    async def search_employee_by_role_and_status(cls, role: EmployeeRole, status: bool) -> list[Employee]:
        """Search employees by role and status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("role", role.capitalize()).eq("state", status).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found with the given role and status", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]


    @classmethod
    async def get_all_clients(cls) -> list[Client]:
        """Retrieve all clients."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No clients found", status_code=404)

        return [Client.model_validate(client) for client in response.data]

    @classmethod
    async def create_client(cls, client_: ClientCreate) -> Client:
        """Create a new client."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).insert(client_.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client creation failed", status_code=400)
        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_id(cls, _id: int, fields: dict) -> Client:
        """Update an existing client."""

        client = await get_db_client()
        
        if not(set(fields.keys()) < set(ClientCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of client", status_code=400)

        response = await client.table(SETTINGS.client_table).update(fields).eq("id", _id).execute()

        if not(bool(response.data)):

            if not cls.exist_client_by_id(_id):
                raise HTTPException(detail="Client not found", status_code=404)

            raise HTTPException(detail="Client update failed", status_code=500)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_email(cls, email: str, fields: dict) -> Client:
        """Update an existing client by email."""

        client = await get_db_client()
        
        if not(set(fields.keys()) < set(ClientCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of client", status_code=400)

        response = await client.table(SETTINGS.client_table).update(fields).eq("email", email).execute()

        if not(bool(response.data)):

            if not cls.exist_client_by_email(email):
                raise HTTPException(detail="Client not found", status_code=404)

            raise HTTPException(detail="Client update failed", status_code=500)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_documentid(cls, document_id: int, fields: dict) -> Client:
        """Update an existing client by document ID."""

        client = await get_db_client()

        if not(set(fields.keys()) < set(ClientCreate.__fields__.keys())):
            raise HTTPException(detail="Update fields are invalid", status_code=400)

        response = await client.table(SETTINGS.client_table).update(fields).eq("documentid", document_id).execute()

        if not(bool(response.data)):

            if not cls.exist_client_by_documentid(document_id):
                raise HTTPException(detail="Client not found", status_code=404)

            raise HTTPException(detail="Client update failed", status_code=500)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def exist_client_by_email(cls, email: str) -> bool:
        """Check if a client exists by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email").eq("email", email).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_client_by_id(cls, _id: int) -> bool:
        """Check if a client exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("id").eq("id", _id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_client_by_documentid(cls, document_id: int) -> bool:
        """Check if a client exists by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("documentid").eq("documentid", document_id).execute()

        return bool(response.data)
    
    @classmethod
    async def read_client_by_id(cls, client_id: int) -> Client:
        """Retrieve a client by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("id", client_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def read_client_by_email(cls, email: str) -> Client:
        """Retrieve a client by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    
    @classmethod
    async def read_client_by_documentid(cls, document_id: int) -> Client:   
        """Retrieve a client by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("documentid", document_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def delete_client_by_id(cls, client_id: int) -> bool:
        """Delete a client by ID."""

        client = await get_db_client()
        
        # check if the client exists
        if not await cls.exist_client_by_id(client_id):
            raise HTTPException(detail="Client not found", status_code=404)

        response = await client.table(SETTINGS.client_table).delete().eq("id", client_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed delete client", status_code=500)

        return True
    
    @classmethod
    async def delete_client_by_email(cls, email: str) -> bool:
        """Delete a client by email."""

        client = await get_db_client()
        
        # check if the client exists
        if not await cls.exist_client_by_email(email):
            raise HTTPException(detail="Client not found", status_code=404)

        response = await client.table(SETTINGS.client_table).delete().eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed delete client", status_code=500)

        return True
      
    @classmethod
    async def delete_client_by_documentid(cls, document_id: int) -> bool:
        """Delete a client by document ID."""

        client = await get_db_client()
        
        # check if the client exists
        if not await cls.exist_client_by_documentid(document_id):
            raise HTTPException(detail="Client not found", status_code=404)

        response = await client.table(SETTINGS.client_table).delete().eq("documentid", document_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed delete client", status_code=500)

        return True
     
    @classmethod
    async def search_client_by_name(cls, name: str) -> list[Client]:
        """Search clients by name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").ilike("name", f"%{name}%").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No clients found with the given name", status_code=404)

        return [Client.model_validate(client) for client in response.data]
    
    @classmethod
    async def search_client_by_status(cls, status: bool) -> list[Client]:
        """Search clients by status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("state", status).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No clients found with the given status", status_code=404)

        return [Client.model_validate(client) for client in response.data]
    
    
    @classmethod
    async def search_client_by_name_and_status(cls, name: str, status: bool) -> list[Client]:
        """Search clients by name and status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").ilike("name", f"%{name}%").eq("state", status).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No clients found with the given name and status", status_code=404)

        return [Client.model_validate(client) for client in response.data]