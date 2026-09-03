import logging
import time
import urllib.request
from urllib.error import URLError, HTTPError

logger = logging.getLogger(__name__)

def execute_network_request(url: str, max_retries: int = 3, backoff_factor: float = 1.5) -> str:
    """
    Executes an HTTP GET request with exponential backoff retry logic.
    
    Args:
        url: The target URL to fetch.
        max_retries: Maximum number of retry attempts.
        backoff_factor: Multiplier for exponential delay calculation.
        
    Returns:
        The response content as a string.
    """
    last_exception = None
    
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'DevToolkit60/1.0'}
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.read().decode('utf-8')
        except (URLError, HTTPError, TimeoutError) as error:
            last_exception = error
            if attempt < max_retries:
                delay = backoff_factor ** attempt
                logger.warning(f"Attempt {attempt} failed: {error}. Retrying in {delay:.2f}s...")
                time.sleep(delay)
            else:
                logger.error(f"All {max_retries} attempts failed for URL: {url}")
                
    raise RuntimeError(f"Network operation failed after {max_retries} retries") from last_exception
