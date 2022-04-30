
from functools import wraps


def __parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


def after_start(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        out = await func(*args, **kwargs)
        print("after_start")
        return out
    return wrapper


def with_keys(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        out = await func(*args, **kwargs)
        print("with_keys")
        print(kwargs)
        return out
    return wrapper


@__parametrized
def with_params(func, timeout: float):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        out = await func(*args, **kwargs)
        print("with_params")
        print(timeout)
        return out
    return wrapper


def with_func_name(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        out = await func(*args, **kwargs)
        print("with_func_name")
        print(func.__name__)
        return out
    return wrapper


def before_start(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print("before_start")
        return await func(*args, **kwargs)
    return wrapper


def on_error(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except:
            print('on_error')
        return {"Error": "Message"}
    return wrapper
