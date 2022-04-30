from functools import wraps
from logger.logger import *


def info_log_aspect(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        out = await func(*args, **kwargs)
        logger.info("func ->  " + func.__name__ +
                    "; parameters ->   " + str(kwargs))
        return out
    return wrapper


def debug_log_aspect(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        out = await func(*args, **kwargs)
        logger.debug("func ->  " + func.__name__ +
                     "; parameters ->   " + str(kwargs) +
                     "; result -> " + str(out))
        return out
    return wrapper


def error_log_aspect(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.error(str(e), exc_info=True)
    return wrapper
