import imp
from pydoc import describe
import pydantic
from application.version import version

DEFAULT_APPLICATION_NAME = "Python Boilerplate"
DEFAULT_APPLICATION_DESCRIPTION = "Python Boiler Plate from https://github.com/public-sysunicorns-info/python_boiler_plate"


class ApplicationConfig(pydantic.BaseSettings):
    name: str = pydantic.Field(default=DEFAULT_APPLICATION_NAME)
    description: str = pydantic.Field(default=DEFAULT_APPLICATION_DESCRIPTION)
    version: str = pydantic.Field(default=version, const=version)
    uvicorn_host: str = pydantic.Field(default="0.0.0.0")
    uvicorn_port: int = pydantic.Field(default=8080)
    uvicorn_workers: int = pydantic.Field(default=1, const=1)



def application_config_factory () -> ApplicationConfig:
    return ApplicationConfig()
