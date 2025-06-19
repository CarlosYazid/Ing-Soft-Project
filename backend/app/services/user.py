from infra import UserNotCreatedError
from db import client as db_client
from schemas import Employee, Client, Admin
from core import SETTINGS

class UserService:
    def __init__(self):
        self.db_client = db_client

    def create_employee(self, employee : Employee) -> Employee:
        """Create a new employee."""
        
        response = self.db_client.table(SETTINGS.employee_table).insert(employee.model_dump_json()).execute()

        if response is not None:
            if response.error:
                raise UserNotCreatedError(f"Employee creation failed: {response.error.message}")
            return response.data
    
    def create_admin(self, admin: Admin) -> Admin:
        """Create a new admin."""
        
        response = self.db_client.table(SETTINGS.admin_table).insert(admin.model_dump_json()).execute()

        if response is not None:
            if response.error:
                raise UserNotCreatedError(f"Admin creation failed: {response.error.message}")
            return response.data
    
    def create_client(self, client: Client) -> Client:
        """Create a new client."""
        
        response = self.db_client.table(SETTINGS.client_table).insert(client.model_dump_json()).execute()

        if response is not None:
            if response.error:
                raise UserNotCreatedError(f"Client creation failed: {response.error.message}")
            return response.data