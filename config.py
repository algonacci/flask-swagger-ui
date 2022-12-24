from dotenv import dotenv_values

config = dotenv_values(".env")

print(config["secret"])

CONFIG = {
    "PROPAGATE_EXCEPTIONS": True,
    "API_TITLE": "Testing Documentation of REST API",
    "API_VERSION": "v1",
    "OPENAPI_VERSION": "3.0.3",
    "OPENAPI_URL_PREFIX": "/",
    "OPENAPI_SWAGGER_UI_PATH": "/docs",
    "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
}
