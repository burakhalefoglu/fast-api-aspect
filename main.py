from functools import wraps
from fastapi import FastAPI


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


app = FastAPI()


@app.get("/{test_path}")
@before_start
@after_start
@with_keys
@on_error
async def read_root(test_path):
    print("fast_api")
    # raise Exception("fast_api error")
    return {"Hello": "World",
            "Page": test_path}
