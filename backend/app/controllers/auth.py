from services import AuthService

class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def sign_up(self, email: str, password: str):
        return self.auth_service.sign_up(email, password)
        
    def sign_in(self, email: str, password: str):
        return self.auth_service.sign_in(email, password)
        
    def sign_out(self):
        return self.auth_service.sign_out()
        