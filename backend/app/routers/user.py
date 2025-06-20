from fastapi import APIRouter, Request, Depends

from models import Employee, Client
from crud import UserCrud
from services import AuthService, UserService


router = APIRouter(prefix="/user")


@router.get("/employee/all")
async def get_employees(request: Request):
    return await UserCrud.get_all_employees()

@router.get("/employee/base/all")
async def get_employees_base(request: Request):
    """
    Retrieve all employees in base format.
    """
    return await UserService.get_all_employees_base()


@router.post("/employee")
async def create_employee(request: Request, 
                          employee: Employee):
    """
    Create a new employee.
    """
    # Here you would typically call a service to handle the creation logic
    return await UserCrud.create_employee(employee)

@router.post("/employee/{_id}")
async def update_employee_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing employee by ID.
    """
    return await UserCrud.update_employee_by_id(_id, fields)

@router.post("/employee/")
async def update_employee_by_id_2(request: Request, id: int, fields: dict):
    """
    Update an existing employee by ID.
    """
    return await UserCrud.update_employee_by_id(id, fields)

@router.post("/employee/{email}")
async def update_employee_by_email(request: Request, email: str, fields: dict):
    """
    Update an existing employee by email.
    """
    return await UserCrud.update_employee_by_email(email, fields)


@router.get("/employee/{_id}")
async def get_employee_by_id(request: Request, _id: int):
    """
    Get an employee by ID.
    """
    return await UserCrud.read_employee_by_id(_id)   

@router.get("/employee/")
async def get_employee_by_id_2(request: Request, id: int):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_id(id)


@router.get("/employee/base/{_id}")
async def get_employee_base_by_id(request: Request, _id: int):
    """
    Get an employee base by ID.
    """
    return await UserService.get_employee_base_by_id(_id)

@router.get("/employee/base/")
async def get_employee_base_by_id_2(request: Request, id: int):
    """
    Get an employee base by ID.
    """
    return await UserService.get_employee_base_by_id(id)


@router.get("/employee/{email}")
async def get_employee_by_email(request: Request, email: str):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_email(email)

@router.get("/employee/")
async def get_employee_by_email_2(request: Request, email: str):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_email(email)

@router.get("/employee/base/{email}")
async def get_employee_base_by_email(request: Request, email: str):
    """
    Get an employee base by email.
    """
    return await UserService.get_employee_base_by_email(email)

@router.get("/employee/base/")
async def get_employee_base_by_email_2(request: Request, email: str):
    """
    Get an employee base by email.
    """
    return await UserService.get_employee_base_by_email(email)


@router.get("/employee/exists/{_id}")
async def exist_employee_by_id(request: Request, _id: int):
    """
    Check if an employee exists by ID.
    """
    return await UserCrud.exist_employee_by_id(_id)

@router.get("/employee/exists/")
async def exist_employee_by_id_2(request: Request, id: int):
    """
    Check if an employee exists by ID.
    """
    return await UserCrud.exist_employee_by_id(id)

@router.get("/employee/exists/email/{email}")
async def exist_employee_by_email(request: Request, email: str):
    """
    Check if an employee exists by email.
    """
    return await UserCrud.exist_employee_by_email(email)

@router.get("/employee/exists/email/")
async def exist_employee_by_email_2(request: Request, email: str):
    """
    Check if an employee exists by email.
    """
    return await UserCrud.exist_employee_by_email(email)

@router.delete("/employee/{_id}")
async def delete_employee_by_id(request: Request, _id: int):
    """
    Delete an employee by ID.
    """
    return await UserCrud.delete_employee_by_id(_id)

@router.delete("/employee/")
async def delete_employee_by_id_2(request: Request, id: int):
    """
    Delete an employee by ID.
    """
    return await UserCrud.delete_employee_by_id(id)

@router.delete("/employee/{email}")
async def delete_employee_by_email(request: Request, email: str):
    """
    Delete an employee by email.
    """
    return await UserCrud.delete_employee_by_email(email)


@router.delete("/employee/")
async def delete_employee_by_email_2(request: Request, email: str):
    """
    Delete an employee by email.
    """
    return await UserCrud.delete_employee_by_email(email)

@router.get("/client/all")
async def get_clients(request: Request):
    """
    Retrieve all clients.
    """
    return await UserCrud.get_all_clients()

@router.get("/client/base/all")
async def get_clients_base(request: Request):
    """
    Retrieve all clients in base format.
    """
    return await UserService.get_all_clients_base()

@router.post("/client")
async def create_client(request: Request,
                        client: Client):
    """
    Create a new client.
    """
    # Here you would typically call a service to handle the creation logic
    return await UserCrud.create_client(client)

@router.get("/client/{_id}")
async def get_client_by_id(request: Request, _id: int):
    """
    Retrieve a client by ID.
    """
    return await UserCrud.read_client_by_id(_id)

@router.get("/client/")
async def get_client_by_id_2(request: Request, id: int):
    """
    Retrieve a client by ID.
    """
    return await UserCrud.read_client_by_id(id)


@router.get("/client/base/{_id}")
async def get_client_base_by_id(request: Request, _id: int):
    """
    Retrieve a client by ID in base format.
    """
    return await UserService.get_client_base_by_id(_id)


@router.get("/client/base/")
async def get_client_base_by_id_2(request: Request, id: int):
    """
    Retrieve a client by ID in base format.
    """
    return await UserService.get_client_base_by_id(id)


@router.get("/client/{email}")
async def get_client_by_email(request: Request, email: str):
    """
    Retrieve a client by email.
    """
    return await UserCrud.read_client_by_email(email)

@router.get("/client/")
async def get_client_by_email_2(request: Request, email: str):
    """
    Retrieve a client by email.
    """
    return await UserCrud.read_client_by_email(email)

@router.get("/client/base/{email}")
async def get_client_base_by_email(request: Request, email: str):
    """
    Retrieve a client by email in base format.
    """
    return await UserService.get_client_base_by_email(email)


@router.get("/client/base/")
async def get_client_base_by_email_2(request: Request, email: str):
    """
    Retrieve a client by email in base format.
    """
    return await UserService.get_client_base_by_email(email)


@router.post("/client/{_id}")
async def update_client_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing client by ID.
    """
    return await UserCrud.update_client_by_id(_id, fields)

@router.post("/client/")
async def update_client_by_id_2(request: Request, id: int, fields: dict):
    """
    Update an existing client by ID.
    """
    return await UserCrud.update_client_by_id(id, fields)

@router.post("/client/{email}")
async def update_client_by_email(request: Request, email: str, fields: dict):
    """
    Update an existing client by email.
    """
    return await UserCrud.update_client_by_email(email, fields)

@router.post("/client/")
async def update_client_by_email_2(request: Request, email: str, fields: dict):
    """
    Update an existing client by email.
    """
    return await UserCrud.update_client_by_email(email, fields)

@router.delete("/client/{_id}")
async def delete_client_by_id(request: Request, _id: int):
    """
    Delete a client by ID.
    """
    return await UserCrud.delete_client_by_id(_id)

@router.delete("/client/")
async def delete_client_by_id_2(request: Request, id: int):
    """
    Delete a client by ID.
    """
    return await UserCrud.delete_client_by_id(id)

@router.delete("/client/{email}")
async def delete_client_by_email(request: Request, email: str):
    """
    Delete a client by email.
    """
    return await UserCrud.delete_client_by_email(email)

@router.delete("/client/")
async def delete_client_by_email_2(request: Request, email: str):
    """
    Delete a client by email.
    """
    return await UserCrud.delete_client_by_email(email)

@router.get("/client/exists/{_id}")
async def exist_client_by_id(request: Request, _id: int):
    """
    Check if a client exists by ID.
    """
    return await UserCrud.exist_client_by_id(_id)

@router.get("/client/exists/")
async def exist_client_by_id_2(request: Request, id: int):
    """
    Check if a client exists by ID.
    """
    return await UserCrud.exist_client_by_id(id)

@router.get("/client/exists/{email}")
async def exist_client_by_email(request: Request, email: str):
    """
    Check if a client exists by email.
    """
    return await UserCrud.exist_client_by_email(email)

@router.get("/client/exists/")
async def exist_client_by_email_2(request: Request, email: str):
    """
    Check if a client exists by email.
    """
    return await UserCrud.exist_client_by_email(email)
