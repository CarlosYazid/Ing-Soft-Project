from datetime import date

from fastapi import APIRouter, Request, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel.ext.asyncio.session import AsyncSession

from models import EmployeeRole
from schemas import ClientCreate, ClientRead, ClientUpdate, EmployeeCreate, EmployeeRead, EmployeeUpdate
from crud import UserCrud
from db import get_session
from services import AuthService, UserService


router = APIRouter(prefix="/user")


@router.post("/employee/", response_model = EmployeeRead)
async def create_employee(request: Request,
                          employee: EmployeeCreate,
                          db_session : AsyncSession = Depends(get_session)):
    """
    Create a new employee.
    """
    return await UserCrud.create_employee(db_session, employee)

@router.get("/employee/{_id}", response_model = EmployeeRead)
async def read_employee(request: Request,
                        _id: int,
                        db_session : AsyncSession = Depends(get_session)):
    """
    Get an employee by ID.
    """
    return await UserCrud.read_employee(db_session, _id)

@router.get("/employee/", response_model = EmployeeRead)
async def read_employee_2(request: Request,
                          _id: int,
                          db_session : AsyncSession = Depends(get_session)):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee(db_session,_id)

@router.get("/employee/email/{email}", response_model = EmployeeRead)
async def read_employee_by_email(request: Request,
                                 email: str,
                                 db_session : AsyncSession = Depends(get_session)):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_email(db_session, email)

@router.get("/employee/email/", response_model = EmployeeRead)
async def read_employee_by_email_2(request: Request,
                                   email: str,
                                   db_session : AsyncSession = Depends(get_session)):
    """
    Get an employee by email.
    """
    return await UserCrud.read_employee_by_email(db_session, email)

@router.get("/employee/documentid/{document_id}", response_model = EmployeeRead)
async def read_employee_by_documentid(request: Request,
                                      document_id: int,
                                      db_session : AsyncSession = Depends(get_session)):
    """
    Get an employee by document ID.
    """
    return await UserCrud.read_employee_by_documentid(db_session, document_id)

@router.get("/employee/documentid/", response_model = EmployeeRead)
async def read_employee_by_documentid_2(request: Request,
                                        document_id: int,
                                        db_session : AsyncSession = Depends(get_session)):
    """
    Get an employee by document ID.
    """
    return await UserCrud.read_employee_by_documentid(db_session, document_id)

@router.patch("/employee/", response_model = EmployeeRead)
async def update_employee(request: Request,
                          fields : EmployeeUpdate,
                          db_session : AsyncSession = Depends(get_session)):
    """
    Update an existing employee by ID.
    """
    return await UserCrud.update_employee(db_session, fields)

@router.patch("/employee/email/", response_model = EmployeeRead)
async def update_employee_by_email(request: Request,
                                   fields: EmployeeUpdate,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing employee by email.
    """
    return await UserCrud.update_employee_by_email(db_session, fields)

@router.patch("/employee/documentid/", response_model = EmployeeRead)
async def update_employee_by_documentid(request: Request,
                                        fields: EmployeeUpdate,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing employee by document ID.
    """
    return await UserCrud.update_employee_by_documentid(db_session, fields)

@router.delete("/employee/{_id}")
async def delete_employee(request: Request,
                          _id: int,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Delete an employee by ID.
    """
    return await UserCrud.delete_employee(db_session, _id)

@router.delete("/employee/")
async def delete_employee_2(request: Request, 
                            _id: int,
                            db_session: AsyncSession = Depends(get_session)):
    """
    Delete an employee by ID.
    """
    return await UserCrud.delete_employee(db_session, _id)

@router.delete("/employee/email/{email}")
async def delete_employee_by_email(request: Request,
                                   email: str,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Delete an employee by email.
    """
    return await UserCrud.delete_employee_by_email(db_session, email)

@router.delete("/employee/email/")
async def delete_employee_by_email_2(request: Request,
                                     email: str,
                                     db_session: AsyncSession = Depends(get_session)):
    """
    Delete an employee by email.
    """
    return await UserCrud.delete_employee_by_email(db_session, email)
  
@router.delete("/employee/documentid/{document_id}")
async def delete_employee_by_documentid(request: Request,
                                        document_id: int, 
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Delete an employee by document ID.
    """
    return await UserCrud.delete_employee_by_documentid(db_session, document_id)

@router.delete("/employee/documentid/")
async def delete_employee_by_documentid_2(request: Request,
                                          document_id: int,
                                          db_session: AsyncSession = Depends(get_session)):
    """
    Delete an employee by document ID.
    """
    return await UserCrud.delete_employee_by_documentid(db_session, document_id)

@router.post("/client", response_model = ClientRead)
async def create_client(request: Request,
                        client: ClientCreate,
                        db_session : AsyncSession = Depends(get_session)):
    """
    Create a new client.
    """
    return await UserCrud.create_client(db_session, client)

@router.get("/client/{_id}", response_model = ClientRead)
async def read_client(request: Request,
                      _id: int,
                      db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve a client by ID.
    """
    return await UserCrud.read_client(db_session, _id)

@router.get("/client/", response_model = ClientRead)
async def read_client_2(request: Request,
                        _id: int,
                        db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve a client by ID.
    """
    return await UserCrud.read_client(db_session, _id)

@router.get("/client/email/{email}", response_model = ClientRead)
async def read_client_by_email(request: Request,
                               email: str,
                               db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve a client by email.
    """
    return await UserCrud.read_client_by_email(db_session, email)

@router.get("/client/email/", response_model = ClientRead)
async def read_client_by_email_2(request: Request,
                                 email: str,
                                 db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve a client by email.
    """
    return await UserCrud.read_client_by_email(db_session, email)

@router.get("/client/documentid/{document_id}", response_model = ClientRead)
async def read_client_by_documentid(request: Request,
                                    document_id: int,
                                    db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve a client by document ID.
    """
    return await UserCrud.read_client_by_documentid(db_session, document_id)

@router.get("/client/documentid/", response_model = ClientRead)
async def read_client_by_documentid_2(request: Request, 
                                      document_id: int,
                                      db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve a client by document ID.
    """
    return await UserCrud.read_client_by_documentid(db_session, document_id)

@router.patch("/client/", response_model = ClientRead)
async def update_client(request: Request,
                        fields: ClientUpdate,
                        db_session : AsyncSession = Depends(get_session)):
    """
    Update an existing client by ID.
    """
    return await UserCrud.update_client(db_session, fields)

@router.patch("/client/update/email/", response_model = ClientRead)
async def update_client_by_email_2(request: Request, 
                                   fields: ClientUpdate,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing client by email.
    """
    return await UserCrud.update_client_by_email(db_session, fields)

@router.patch("/client/update/documentid/", response_model = ClientRead)
async def update_client_by_documentid_2(request: Request, 
                                        fields: ClientUpdate,
                                        db_session: AsyncSession = Depends(get_session)):
    """ Update an existing client by document ID.
    """
    return await UserCrud.update_client_by_documentid(db_session, fields)

@router.delete("/client/{_id}")
async def delete_client(request: Request,
                        _id: int,
                        db_session : AsyncSession = Depends(get_session)):
    """
    Delete a client by ID.
    """
    return await UserCrud.delete_client(db_session, _id)

@router.delete("/client/")
async def delete_client_2(request: Request,
                          id: int, 
                          db_session: AsyncSession = Depends(get_session)):
    """
    Delete a client by ID.
    """
    return await UserCrud.delete_client(db_session, id)

@router.delete("/client/email/{email}")
async def delete_client_by_email(request: Request,
                                 email: str,
                                 db_session: AsyncSession = Depends(get_session)):
    """
    Delete a client by email.
    """
    return await UserCrud.delete_client_by_email(db_session, email)

@router.delete("/client/email/")
async def delete_client_by_email_2(request: Request,
                                   email: str,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Delete a client by email.
    """
    return await UserCrud.delete_client_by_email(db_session, email)

@router.delete("/client/documentid/{document_id}")
async def delete_client_by_documentid(request: Request,
                                      document_id: int,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Delete a client by document ID.
    """
    return await UserCrud.delete_client_by_documentid(db_session, document_id)

@router.delete("/client/documentid/")
async def delete_client_by_documentid_2(request: Request,
                                        document_id: int,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Delete a client by document ID.
    """
    return await UserCrud.delete_client_by_documentid(db_session, document_id)

@router.get("/employee/all/", response_model = Page[EmployeeRead])
async def read_all_employees(request: Request,
                              db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve all employees.
    """
    return await apaginate(db_session, UserService.read_all_employees())

@router.get("/employee/search/name/{name}", response_model = Page[EmployeeRead])
async def search_employees_by_name(request: Request,
                                   name: str,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Search employees by name.
    """
    return await apaginate(db_session, UserService.search_employees_by_name(name))

@router.get("/employee/search/birthday/{birthday}", response_model = Page[EmployeeRead])
async def search_employees_by_birthday(request: Request,
                                       birthday: date,
                                       db_session: AsyncSession = Depends(get_session)):
    """
    Search employees by birthday.
    """
    return await apaginate(db_session, UserService.search_employees_by_birthday(birthday))

@router.get("/employee/search/status/{status}", response_model = Page[EmployeeRead])
async def search_employees_by_status(request: Request,
                                     status: bool,
                                     db_session: AsyncSession = Depends(get_session)):
    """
    Search employees by status.
    """
    return await apaginate(db_session, UserService.search_employees_by_status(status))

@router.get("/employee/search/role/{role}", response_model = Page[EmployeeRead])
async def search_employees_by_role(request : Request,
                                   role : EmployeeRole,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Search employees by role.
    """
    return await apaginate(db_session, UserService.search_employees_by_role(role))

@router.get("/employee/search/name/{name}/role/{role}", response_model = Page[EmployeeRead])
async def search_employees_by_name_and_role(request: Request, 
                                            name: str,
                                            role: EmployeeRole,
                                            db_session: AsyncSession = Depends(get_session)):
    """Search employees by name and role.
    """
    return await apaginate(db_session, UserService.search_employees_by_name_and_role(name, role))

@router.get("/employee/search/name/{name}/status/{status}", response_model = Page[EmployeeRead])
async def search_employees_by_name_and_status(request: Request, 
                                              name: str,
                                              status: bool,
                                              db_session: AsyncSession = Depends(get_session)):
    """Search employees by name and status.
    """
    return await apaginate(db_session, UserService.search_employees_by_name_and_status(name, status))

@router.get("/employee/search/role/{role}/status/{status}", response_model = Page[EmployeeRead])
async def search_employees_by_role_and_status(request: Request, 
                                              role: EmployeeRole,
                                              status: bool,
                                              db_session: AsyncSession = Depends(get_session)):
    """Search employees by role and status.
    """
    return await apaginate(db_session, UserService.search_employees_by_role_and_status(role, status))

@router.get("/employee/search/name/{name}/birthday/{birthday}", response_model = Page[EmployeeRead])
async def search_employee_by_name_and_birthday(request: Request, 
                                               name: str,
                                               birthday: date,
                                               db_session: AsyncSession = Depends(get_session)):
    """Search employees by name and birthday.
    """
    return await apaginate(db_session, UserService.search_employees_by_name_and_birthday(name, birthday))

@router.get("/client/all/", response_model = Page[ClientRead])
async def read_all_clients(request: Request,
                           db_session : AsyncSession = Depends(get_session)):
    """
    Retrieve all clients.
    """
    return await apaginate(db_session, UserService.read_all_clients())

@router.get("/client/search/name/{name}", response_model = Page[ClientRead])
async def search_clients_by_name(request: Request,
                                 name: str,
                                 db_session: AsyncSession = Depends(get_session)):
    """
    Search clients by name.
    """
    return await apaginate(db_session, UserService.search_clients_by_name(name))

@router.get("/client/search/status/{status}", response_model = Page[ClientRead])
async def search_clients_by_status(request: Request,
                                   status: bool,
                                   db_session: AsyncSession = Depends(get_session)):
    """
    Search clients by status.
    """
    return await apaginate(db_session, UserService.search_clients_by_status(status))

@router.get("/client/search/name/{name}/status/{status}", response_model = Page[ClientRead])
async def search_clients_by_name_and_status(request: Request,
                                            name: str,
                                            status: bool,
                                            db_session: AsyncSession = Depends(get_session)):
    """Search clients by name and status.
    """
    return await apaginate(db_session, UserService.search_clients_by_name_and_status(name, status))