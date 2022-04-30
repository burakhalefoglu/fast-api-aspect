from functools import wraps
from datetime import datetime
from custom_exceptions.custom_exceptions import SecurityException
from logger.logger import *


def security_aspect(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        # check security
        is_insecure = True
        if is_insecure:
            logger.error("func ->  " + func.__name__ +
                         "; parameters ->   " + str(kwargs) +
                         "; security_message: " + "Güvenlik ihlali")
            raise SecurityException
        else:
            return await func(*args, **kwargs)
    return wrapper
