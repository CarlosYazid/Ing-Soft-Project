from models import UserBase
from crud import UserCrud

class UserService:
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
             "documentid": user.documentID,
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
             "documentid": user.documentID,
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
             "documentid": user.documentID,
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
             "documentid": user.documentID,
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
             "documentid": user.documentID,
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
             "documentid": user.documentID,
            }
        )
