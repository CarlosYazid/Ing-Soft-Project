from fastapi import APIRouter, Request, Depends

from models import Employee, Client
from crud import UserCrud
from services import AuthService


router = APIRouter(prefix="/user")

@router.get("/")
async def get_users():
    return {"message": "List of users"}


@router.get("/employee/all")
async def get_employes(request: Request):
    return await UserCrud.get_all_employees()


@router.post("/employee")
async def create_employee(request: Request, 
                          employee: Employee,
                          current_user : dict = Depends(AuthService.current_user)):
    """
    Create a new employee.
    """
    # Here you would typically call a service to handle the creation logic
    return await UserCrud.create_employee(employee)


@router.post("/client")
async def create_client(request: Request,
                        client: Client,
                         current_user: dict = Depends(AuthService.current_user)):
    """
    Create a new client.
    """
    # Here you would typically call a service to handle the creation logic
    return await UserCrud.create_client(client)