from functools import wraps
from datetime import datetime
from logger.logger import *


def __parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@__parametrized
def performance_aspect(func, t: float):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = datetime.now()
        out = await func(*args, **kwargs)
        end = datetime.now()
        dt = end - start
        if t <= dt.seconds:
            logger.debug("func ->  " + func.__name__ +
                         "; parameters ->   " + str(kwargs) +
                         "; expected_max_second: " + str(t) +
                         "; valid_second: " + "{:.12f}".format(dt.total_seconds()))
        return out
    return wrapper
