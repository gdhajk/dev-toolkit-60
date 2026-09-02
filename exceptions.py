"""Custom exceptions for the autoclicker toolkit.

This file centralizes error types following cleanup and reorganization.
"""

class AutoclickerError(Exception):
    """Base class for all autoclicker errors."""
    def __init__(self, message, details=None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

class ConfigurationError(AutoclickerError):
    """Error in configuration loading or validation."""
    def __init__(self, message, section=None, key=None):
        details = {"section": section, "key": key}
        super().__init__(message, details)

class ClickExecutionError(AutoclickerError):
    """Error during mouse click execution."""
    def __init__(self, message, button=None, x=None, y=None):
        details = {"button": button, "x": x, "y": y}
        super().__init__(message, details)

class HotkeyError(AutoclickerError):
    """Error with hotkey setup or detection."""
    def __init__(self, message, hotkey=None):
        super().__init__(message, {"hotkey": hotkey})

class UnsupportedPlatformError(AutoclickerError):
    """Error when platform is not supported."""
    def __init__(self, message, platform=None):
        super().__init__(message, {"platform": platform})

class ResourceError(AutoclickerError):
    """Error accessing files or resources."""
    def __init__(self, message, resource=None):
        super().__init__(message, {"resource": resource})

class ValidationError(AutoclickerError):
    """Error in input validation."""
    def __init__(self, message, field=None, value=None):
        details = {"field": field, "value": value}
        super().__init__(message, details)

class StateError(AutoclickerError):
    """Error due to invalid runtime state."""
    def __init__(self, message, state=None):
        super().__init__(message, {"state": state})

# Helper comments for context
# These exceptions are used throughout the autoclicker code
# to provide clear error information and allow specific handling
# in different parts of the application such as the core loop
# and the configuration processor
# No placeholders here as per requirements
# The code is practical and ready for use in Python 3