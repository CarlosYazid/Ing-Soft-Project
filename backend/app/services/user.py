from datetime import date

from models import UserBase, EmployeeRole
from crud import UserCrud

class UserService:
    
    
    @classmethod
    async def search_employee_by_name(cls, name: str) -> list[UserBase]:
        """Search employees by name."""
        users = await UserCrud.search_employee_by_name(name)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_employee_by_birthday(cls, birthday: str) -> list[UserBase]:
        """Search employees by birthday."""
        users = await UserCrud.search_employee_by_birthday(birthday)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_employee_by_status(cls, status: bool) -> list[UserBase]:
        """Search employees by status."""
        users = await UserCrud.search_employee_by_status(status)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_employee_by_role(cls, role: EmployeeRole) -> list[UserBase]:
        """Search employees by role."""
        users = await UserCrud.search_employee_by_role(role)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_employee_by_name_and_role(cls, name: str, role: EmployeeRole) -> list[UserBase]:
        """Search employees by name and role."""
        users = await UserCrud.search_employee_by_name_and_role(name, role)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
        
    @classmethod
    async def search_employee_by_name_and_status(cls, name: str, status: bool) -> list[UserBase]:
        """Search employees by name and status."""
        users = await UserCrud.search_employee_by_name_and_status(name, status)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_employee_by_role_and_status(cls, role: EmployeeRole, status: bool) -> list[UserBase]:
        """Search employees by role and status."""
        users = await UserCrud.search_employee_by_role_and_status(role, status)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_employee_by_name_and_birthday(cls, name: str, birthday: date) -> list[UserBase]:
        """Search employees by name and birthday."""
        users = await UserCrud.search_employee_by_name_and_birthday(name, birthday)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def get_all_employees_base(cls) -> list[UserBase]:
        """Retrieve all employees."""
        users = await UserCrud.get_all_employees()
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]

    @classmethod
    async def get_employee_base_by_id(cls, employee_id: int) -> UserBase:
        """Retrieve a user by ID."""
        user = await UserCrud.read_employee_by_id(employee_id)
        return UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }
        )
        
    @classmethod
    async def get_employee_base_by_email(cls, email: str) -> UserBase:
        """Retrieve a user by email."""
        user = await UserCrud.read_employee_by_email(email)
        return UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }
        )
        
        
    @classmethod
    async def get_employee_base_by_documentid(cls, documentid: str) -> UserBase:
        """Retrieve a user by document ID."""
        user = await UserCrud.read_employee_by_documentid(documentid)
        return UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }
        )
        
    @classmethod
    async def get_all_clients_base(cls) -> list[UserBase]:
        """Retrieve all clients."""
        users = await UserCrud.get_all_clients()
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def get_client_base_by_id(cls, client_id: int) -> UserBase:
        """Retrieve a client by ID."""
        user = await UserCrud.read_client_by_id(client_id)
        return UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }
        )
    
    @classmethod
    async def get_client_base_by_email(cls, email: str) -> UserBase:
        """Retrieve a client by email."""
        user = await UserCrud.read_client_by_email(email)
        return UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }
        )

    @classmethod
    async def search_client_by_name(cls, name: str) -> list[UserBase]:
        """Search clients by name."""
        users = await UserCrud.search_client_by_name(name)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
        
    @classmethod
    async def search_client_by_status(cls, status: bool) -> list[UserBase]:
        """Search clients by status."""
        users = await UserCrud.search_client_by_status(status)
        return [UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
            }) for user in users]
    
    @classmethod
    async def search_client_by_name_and_status(cls, name: str, status: bool) -> list[UserBase]:
        """Search clients by name and status."""
        users = await UserCrud.search_client_by_name_and_status(name, status)
        return [UserBase.model_validate(
             {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid,
              }) for user in users]

    @classmethod
    async def get_client_base_by_documentid(cls, documentid: str) -> UserBase:
        """Retrieve a client by document ID."""
        user = await UserCrud.read_client_by_documentid(documentid)
        return UserBase.model_validate(
            {"id": user.id,
             "name": user.name,
             "email": user.email,
             "phone": user.phone,
             "created_at": user.created_at,
             "updated_at": user.updated_at,
             "state": user.state,
             "documentid": user.documentid})