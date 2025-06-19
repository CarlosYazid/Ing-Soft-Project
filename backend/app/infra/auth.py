from fastapi import HTTPException
from fastapi import status

class AuthError(HTTPException):
    """Custom exception for authentication errors."""
    def __init__(self, detail: str, code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=code, detail=detail)

    
    def __str__(self):
        return f"AuthError (code {self.status_code}): {self.detail}"
    
class UserNotSignUpError(AuthError):
    """Custom exception for user sign-up errors."""
    def __init__(self, detail: str, code: int = 400):
        super().__init__(detail, code)
    
    def __str__(self):
        return f"UserNotSignUpError (code {self.status_code}): {self.detail}"

class UserNotSignInError(AuthError):
    """Custom exception for user sign-in errors."""
    def __init__(self, detail: str, code: int = 400):
        super().__init__(detail, code)
    
    def __str__(self):
        return f"UserNotSignInError (code {self.status_code}): {self.detail}"
    
class UserNotSignOutError(AuthError):
    """Custom exception for user sign-out errors."""
    def __init__(self, detail: str, code: int = 400):
        super().__init__(detail, code)
    
    def __str__(self):
        return f"UserNotSignOutError (code {self.status_code}): {self.detail}"

class PasswordResetError(AuthError):
    """Custom exception for password reset errors."""
    def __init__(self, detail: str, code: int = 400):
        super().__init__(detail, code)
    
    def __str__(self):
        return f"PasswordResetError (code {self.status_code}): {self.detail}"

class PasswordUpdateError(AuthError):
    """Custom exception for password update errors."""
    def __init__(self, detail: str, code: int = 400):
        super().__init__(detail, code)
    
    def __str__(self):
        return f"PasswordUpdateError (code {self.code}): {self.message}"