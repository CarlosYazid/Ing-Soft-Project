from fastapi import APIRouter

from schemas import Employee, Admin, Client
from controllers import UserController

router = APIRouter()

@router.get("/users")
async def get_users():
    return {"message": "List of users"}


@router.post("/user/employee")
async def create_employee(employee: Employee):
    """
    Create a new employee.
    """
    # Here you would typically call a service to handle the creation logic
    return UserController().create_employee(employee)

@router.post("/user/admin")
async def create_admin(admin: Admin):
    """
    Create a new admin.
    """
    # Here you would typically call a service to handle the creation logic
    return UserController().create_admin(admin)

@router.post("/user/client")
async def create_client(client: Client):
    """
    Create a new client.
    """
    # Here you would typically call a service to handle the creation logic
    return UserController().create_client(client)