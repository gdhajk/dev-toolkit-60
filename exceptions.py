class CustomError(Exception):
    """Base class for other exceptions."""
    pass

class ValidationError(CustomError):
    """Raised when validation fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ConnectionError(CustomError):
    """Raised for connection issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TimeoutError(CustomError):
    """Raised when a timeout occurs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(CustomError):
    """Raised when a resource is not found."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)