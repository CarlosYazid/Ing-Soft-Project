from infra.main import _BaseException

class DatabaseError(_BaseException):
    """Custom exception for database errors."""
    def __init__(self, message: str, code: int = 500):
        super().__init__(message, code)
    
    def __str__(self):
        return f"DatabaseError (code {self.code}): {self.message}"

class UserNotCreatedError(DatabaseError):
    """Custom exception for user creation errors."""
    def __init__(self, message: str, code: int = 400):
        super().__init__(message, code)
    
    def __str__(self):
        return f"UserNotCreatedError (code {self.code}): {self.message}"