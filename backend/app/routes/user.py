from fastapi import APIRouter, Request, Depends
from datetime import date

from models import ClientCreate, EmployeeCreate, EmployeeRole
from crud import UserCrud
from services import AuthService, UserService


router = APIRouter(prefix="/user")


@router.post("/employee/")
async def create_employee(request: Request, 
                          employee: EmployeeCreate):
    """
    Create a new employee.
    """
    return await UserCrud.create_employee(employee)

@router.get("/employee/all")
async def read_all_employees(request: Request):
    """
    Retrieve all employees.
    """
    return await UserCrud.read_all_employees()

@router.get("/employee/base/all")
async def read_all_employees_base(request: Request):
    """
    Retrieve all employees in base format.
    """
    return await UserCrud.read_all_employees_base()

@router.get("/employee/{_id}")
async def read_employee(request: Request, _id: int):
    """
    Get an employee by ID.
    """
    return await UserCrud.read_employee(_id)   

@router.get("/employee/")
async def read_employee_2(request: Request, _id: int):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee(_id)

@router.get("/employee/base/{_id}")
async def read_employee_base(request: Request, _id: int):
    """
    Get an employee base by ID.
    """
    return await UserCrud.read_employee_base(_id)

@router.get("/employee/base/")
async def read_employee_base_2(request: Request, _id: int):
    """
    Get an employee base by ID.
    """
    return await UserCrud.read_employee_base(_id)


@router.get("/employee/email/{email}")
async def read_employee_by_email(request: Request, email: str):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_email(email)

@router.get("/employee/email/")
async def read_employee_by_email_2(request: Request, email: str):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_email(email)

@router.get("/employee/base/email/{email}")
async def read_employee_base_by_email(request: Request, email: str):
    """
    Get an employee base by email.
    """
    return await UserCrud.read_employee_base_by_email(email)

@router.get("/employee/base/email/")
async def read_employee_base_by_email_2(request: Request, email: str):
    """
    Get an employee base by email.
    """
    return await UserCrud.read_employee_base_by_email(email)


@router.get("/employee/documentid/{document_id}")
async def read_employee_by_documentid(request: Request, document_id: int):
    """
    Get an employee by document ID.
    """
    return await UserCrud.read_employee_by_documentid(document_id)

@router.get("/employee/documentid/")
async def read_employee_by_documentid_2(request: Request, document_id: int):
    """
    Get an employee by document ID.
    """
    return await UserCrud.read_employee_by_documentid(document_id)


@router.get("/employee/base/documentid/{document_id}")
async def read_employee_base_by_documentid(request: Request, document_id: int):
    """
    Get an employee base by document ID.
    """
    return await UserCrud.read_employee_base_by_documentid(document_id)

@router.get("/employee/base/documentid/")
async def read_employee_base_by_documentid_2(request: Request, document_id: int):
    """
    Get an employee base by document ID.
    """
    return await UserCrud.read_employee_base_by_documentid(document_id)

@router.put("/employee/{_id}")
async def update_employee(request: Request, _id: int, fields: dict):
    """
    Update an existing employee by ID.
    """
    return await UserCrud.update_employee(_id, fields)

@router.put("/employee/update/")
async def update_employee_2(request: Request, _id: int, fields: dict):
    """
    Update an existing employee by ID.
    """
    return await UserCrud.update_employee(_id, fields)

@router.put("/employee/email/{email}")
async def update_employee_by_email(request: Request, email: str, fields: dict):
    """
    Update an existing employee by email.
    """
    return await UserCrud.update_employee_by_email(email, fields)

@router.put("/employee/email/")
async def update_employee_by_email_2(request: Request, email: str, fields: dict):
    """
    Update an existing employee by email.
    """
    return await UserCrud.update_employee_by_email(email, fields)


@router.put("/employee/documentid/{document_id}")
async def update_employee_by_documentid(request: Request, document_id: int, fields: dict):
    """ Update an existing employee by document ID.
    """
    return await UserCrud.update_employee_by_documentid(document_id, fields)

@router.put("/employee/documentid/")
async def update_employee_by_documentid_2(request: Request, document_id: int, fields: dict):
    """ Update an existing employee by document ID.
    """
    return await UserCrud.update_employee_by_documentid(document_id, fields)

@router.delete("/employee/{_id}")
async def delete_employee(request: Request, _id: int):
    """
    Delete an employee by ID.
    """
    return await UserCrud.delete_employee(_id)

@router.delete("/employee/")
async def delete_employee_2(request: Request, _id: int):
    """
    Delete an employee by ID.
    """
    return await UserCrud.delete_employee(_id)

@router.delete("/employee/email/{email}")
async def delete_employee_by_email(request: Request, email: str):
    """
    Delete an employee by email.
    """
    return await UserCrud.delete_employee_by_email(email)


@router.delete("/employee/email/")
async def delete_employee_by_email_2(request: Request, email: str):
    """
    Delete an employee by email.
    """
    return await UserCrud.delete_employee_by_email(email)
  
@router.delete("/employee/documentid/{document_id}")
async def delete_employee_by_documentid(request: Request, document_id: int):
    """
    Delete an employee by document ID.
    """
    return await UserCrud.delete_employee_by_documentid(document_id)

@router.delete("/employee/documentid/")
async def delete_employee_by_documentid_2(request: Request, document_id: int):
    """
    Delete an employee by document ID.
    """
    return await UserCrud.delete_employee_by_documentid(document_id)

@router.post("/client")
async def create_client(request: Request, client: ClientCreate):
    """
    Create a new client.
    """
    # Here you would typically call a service to handle the creation logic
    return await UserCrud.create_client(client)

@router.get("/client/all")
async def read_all_clients(request: Request):
    """
    Retrieve all clients.
    """
    return await UserCrud.read_all_clients()

@router.get("/client/base/all")
async def read_all_clients_base(request: Request):
    """
    Retrieve all clients in base format.
    """
    return await UserCrud.read_all_clients_base()

@router.get("/client/{_id}")
async def read_client(request: Request, _id: int):
    """
    Retrieve a client by ID.
    """
    return await UserCrud.read_client(_id)

@router.get("/client/")
async def read_client_2(request: Request, _id: int):
    """
    Retrieve a client by ID.
    """
    return await UserCrud.read_client(_id)

@router.get("/client/base/{_id}")
async def read_client_base(request: Request, _id: int):
    """
    Retrieve a client by ID in base format.
    """
    return await UserCrud.read_client_base(_id)

@router.get("/client/base/")
async def read_client_base_2(request: Request, _id: int):
    """
    Retrieve a client by ID in base format.
    """
    return await UserCrud.read_client_base(_id)

@router.get("/client/email/{email}")
async def read_client_by_email(request: Request, email: str):
    """
    Retrieve a client by email.
    """
    return await UserCrud.read_client_by_email(email)

@router.get("/client/email/")
async def read_client_by_email_2(request: Request, email: str):
    """
    Retrieve a client by email.
    """
    return await UserCrud.read_client_by_email(email)

@router.get("/client/base/email/{email}")
async def read_client_base_by_email(request: Request, email: str):
    """
    Retrieve a client by email in base format.
    """
    return await UserCrud.read_client_base_by_email(email)


@router.get("/client/base/email/")
async def read_client_base_by_email_2(request: Request, email: str):
    """
    Retrieve a client by email in base format.
    """
    return await UserCrud.read_client_base_by_email(email)

@router.get("/client/documentid/{document_id}")
async def read_client_by_documentid(request: Request, document_id: int):
    """
    Retrieve a client by document ID.
    """
    return await UserCrud.read_client_by_documentid(document_id)

@router.get("/client/documentid/")
async def read_client_by_documentid_2(request: Request, document_id: int):
    """
    Retrieve a client by document ID.
    """
    return await UserCrud.read_client_by_documentid(document_id)


@router.put("/client/{_id}")
async def update_client(request: Request, _id: int, fields: dict):
    """
    Update an existing client by ID.
    """
    return await UserCrud.update_client(_id, fields)

@router.put("/client/update/")
async def update_client_2(request: Request, id: int, fields: dict):
    """
    Update an existing client by ID.
    """
    return await UserCrud.update_client(id, fields)

@router.put("/client/update/email/{email}")
async def update_client_by_email(request: Request, email: str, fields: dict):
    """
    Update an existing client by email.
    """
    return await UserCrud.update_client_by_email(email, fields)

@router.put("/client/update/email/")
async def update_client_by_email_2(request: Request, email: str, fields: dict):
    """
    Update an existing client by email.
    """
    return await UserCrud.update_client_by_email(email, fields)

@router.put("/client/update/documentid/{document_id}")
async def update_client_by_documentid(request: Request, document_id: int, fields: dict):
    """ Update an existing client by document ID.
    """
    return await UserCrud.update_client_by_documentid(document_id, fields)

@router.put("/client/update/documentid/")
async def update_client_by_documentid_2(request: Request, document_id: int, fields: dict):
    """ Update an existing client by document ID.
    """
    return await UserCrud.update_client_by_documentid(document_id, fields)

@router.delete("/client/{_id}")
async def delete_client(request: Request, _id: int):
    """
    Delete a client by ID.
    """
    return await UserCrud.delete_client(_id)

@router.delete("/client/")
async def delete_client_2(request: Request, id: int):
    """
    Delete a client by ID.
    """
    return await UserCrud.delete_client(id)

@router.delete("/client/email/{email}")
async def delete_client_by_email(request: Request, email: str):
    """
    Delete a client by email.
    """
    return await UserCrud.delete_client_by_email(email)

@router.delete("/client/email/")
async def delete_client_by_email_2(request: Request, email: str):
    """
    Delete a client by email.
    """
    return await UserCrud.delete_client_by_email(email)

@router.delete("/client/documentid/{document_id}")
async def delete_client_by_documentid(request: Request, document_id: int):
    """
    Delete a client by document ID.
    """
    return await UserCrud.delete_client_by_documentid(document_id)

@router.delete("/client/documentid/")
async def delete_client_by_documentid_2(request: Request, document_id: int):
    """
    Delete a client by document ID.
    """
    return await UserCrud.delete_client_by_documentid(document_id)

@router.get("/employee/search/name/{name}")
async def search_employees_by_name(request: Request, name: str):
    """
    Search employees by name.
    """
    return await UserService.search_employees_by_name(name)


@router.get("/employee/search/birthday/{birthday}")
async def search_employees_by_birthday(request: Request, birthday: date):
    """
    Search employees by birthday.
    """
    return await UserService.search_employees_by_birthday(birthday)

@router.get("/employee/search/status/{status}")
async def search_employees_by_status(request: Request, status: bool):
    """
    Search employees by status.
    """
    return await UserService.search_employees_by_status(status)

@router.get("/employee/search/role/{role}")
async def search_employees_by_role(request : Request, role : EmployeeRole):
    """
    Search employees by role.
    """
    return await UserService.search_employees_by_role(role)

@router.get("/employee/search/name/{name}/role/{role}")
async def search_employees_by_name_and_role(request: Request, name: str, role: EmployeeRole):
    """Search employees by name and role.
    """
    return await UserService.search_employees_by_name_and_role(name, role)


@router.get("/employee/search/name/{name}/status/{status}")
async def search_employees_by_name_and_status(request: Request, name: str, status: bool):
    """Search employees by name and status.
    """
    return await UserService.search_employees_by_name_and_status(name, status)


@router.get("/employee/search/role/{role}/status/{status}")
async def search_employees_by_role_and_status(request: Request, role: EmployeeRole, status: bool):
    """Search employees by role and status.
    """
    return await UserService.search_employees_by_role_and_status(role, status)

@router.get("/employee/search/name/{name}/birthday/{birthday}")
async def search_employee_by_name_and_birthday(request: Request, name: str, birthday: date):
    """Search employees by name and birthday.
    """
    return await UserService.search_employees_by_name_and_birthday(name, birthday)

@router.get("/client/search/name/{name}")
async def search_clients_by_name(request: Request, name: str):
    """
    Search clients by name.
    """
    return await UserService.search_clients_by_name(name)

@router.get("/client/search/status/{status}")
async def search_clients_by_status(request: Request, status: bool):
    """
    Search clients by status.
    """
    return await UserService.search_clients_by_status(status)

@router.get("/client/search/name/{name}/status/{status}")
async def search_clients_by_name_and_status(request: Request, name: str, status: bool):
    """Search clients by name and status.
    """
    return await UserService.search_clients_by_name_and_status(name, status)