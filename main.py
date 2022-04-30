import asyncio
from fastapi import FastAPI
from aspects.cache_aspect import cache_aspect, cache_remove_aspect
from aspects.exception_aspect import exception_aspect
from aspects.log_aspect import debug_log_aspect, error_log_aspect, info_log_aspect
from aspects.performance_aspect import performance_aspect
from aspects.security_aspect import security_aspect
from aspects.validation_aspect import validation_aspect
from logger.logger import init_log

app = FastAPI()
init_log()
validation_schema = {'page': {'type': 'integer'}}


# All aspect for service layer. But I used for testing on controller!!!
@app.get("/{page}")
@exception_aspect
# @validation_aspect(validation_schema)
# @info_log_aspect
# @error_log_aspect
# @debug_log_aspect
# @performance_aspect(5)
# @security_aspect
# @cache_aspect
# @cache_remove_aspect
async def read_root(page):
    print("fast_api work")
    return {"Hello": "World",
            "Page": page}
