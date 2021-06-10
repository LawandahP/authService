# from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "GITKA RMS AUTH SERVICE"
VERSION = "1.0.0"
# API_PREFIX_BUILDINGS = "/api/buildings"
# API_PREFIX_UNITS = "/api/units"
DOCS_URL = "/api/v1/docs"
REDOC_URL = "/api/v1/redocs"
OPENAPI_URL = "/api/v1/openapi.json"
DESCRIPTION = "This is an authentication and authorization that"\
              "basically generates and verifies jwt tokens"

SECRET_KEY = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES = config(
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    cast=int,
    default=7 * 24 * 60  # one week
)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str, default="HS256")
JWT_AUDIENCE = config("JWT_AUDIENCE", cast=str, default="kgHomes:auth")
JWT_TOKEN_PREFIX = config("JWT_TOKEN_PREFIX", cast=str, default="Bearer")

# POSTGRES_USER = config("POSTGRES_USER", cast=str, default='githaiga')
# POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default='admin')
# POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="buildingunitdb")

# POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
# POSTGRES_DB = config("POSTGRES_DB", cast=str, default='buildingunit_db')
# DATABASE_URL = config(
#     "DATABASE_URL",
#     cast=DatabaseURL,
#     default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:/{POSTGRES_DB}"
# )




