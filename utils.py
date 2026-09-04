import time
import functools
import logging

# Configure logger for dev-toolkit-60
logger = logging.getLogger('dev-toolkit')

def retry_on_failure(retries=3, delay=2, exceptions=(Exception,)):
    """Decorator to implement exponential backoff for network operations."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {current_delay}s...")
                    if attempt < retries:
                        time.sleep(current_delay)
                        current_delay *= 2  # Exponential backoff
            
            logger.error(f"Function {func.__name__} failed after {retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

# Example usage for network calls
@retry_on_failure(retries=3, delay=1)
def fetch_remote_config(url):
    """Placeholder for actual network request logic."""
    # Simulating connection logic
    return {"status": "success"}