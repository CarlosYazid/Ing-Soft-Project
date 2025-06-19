class _BaseException(Exception):
    """Base class for all custom exceptions."""
    def __init__(self, message: str, code: int = 0):
        super().__init__(message)
        self.message = message
        self.code = code
    
    def __str__(self):
        return f"{self.message} (code {self.code})"
