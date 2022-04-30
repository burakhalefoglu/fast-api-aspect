from functools import wraps
from cerberus import Validator
from custom_exceptions.custom_exceptions import ValidationException


def __parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@__parametrized
def validation_aspect(func, schema: dict):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        v = Validator(schema)
        if v.validate(kwargs) is False:
            raise ValidationException(v.errors)
        else:
            return await func(*args, **kwargs)
    return wrapper
