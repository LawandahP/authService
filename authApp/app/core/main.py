
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core import config
from app.api.endpoints.login import api as login_router
# from app.core.database import database

main_app = FastAPI(title=config.PROJECT_NAME,
                   version=config.VERSION,
                   docs_url=config.DOCS_URL,
                   redoc_url=config.REDOC_URL,
                   description=config.DESCRIPTION)

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @main_app.on_event("startup")
# async def startup():
#     await database.connect()


# @main_app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


main_app.include_router(login_router, tags=['LOGIN'])
# main_app.include_router(unit_router, tags=['UNITS'], prefix=config.API_PREFIX_UNITS)

