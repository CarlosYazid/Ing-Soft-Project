from fastapi import HTTPException
from fastapi import status

from infra import UserNotSignUpError
from services import UserService
from schemas import Employee, Admin, Client

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create_employee(self, employee: Employee):
        try:
            return self.user_service.create_employee(employee)
        except UserNotCreatedError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        
    def create_admin(self, admin: Admin):
        try:
            return self.user_service.create_admin(admin)
        except UserNotCreatedError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    def create_client(self, client: Client):
        try:
            return self.user_service.create_client(client)
        except UserNotCreatedError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))