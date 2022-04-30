from functools import wraps
import json
import pandas as pd
from cache.in_memory_cache import delete_cache, get_from_cache, set_cache
from typing import Callable


def cache_aspect(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        class_name = (func.__qualname__).split('.')[0]
        result = get_from_cache(class_name, func.__name__ + str(kwargs))
        if result.empty is False:
            return result.to_dict()[0]
        else:
            out = await func(*args, **kwargs)
            if out is not None:
                set_cache(class_name, func.__name__ +
                          str(kwargs), pd. DataFrame(out.items()))
            return out
    return wrapper


def cache_remove_aspect(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        class_name = (func.__qualname__).split('.')[0]
        delete_cache(class_name)
        out = await func(*args, **kwargs)
        return out
    return wrapper
