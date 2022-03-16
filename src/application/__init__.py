
import fastapi
from starlette.types import Receive, Scope, Send

from .container import Container

from .version import version
import application.api


class Application:

    fastapi_object: fastapi.FastAPI = None
    container: Container


    TITLE = "Python Boilerplate"
    DESCRIPTION = "Python Boiler Plate from https://github.com/public-sysunicorns-info/python_boiler_plate"


    def __init__(self) -> None:
        
        # Initialize and wire dependency-injection
        self.container = Container()
        self.container.wire(modules=[
            application.api
        ])

        # Initialize FastAPI Object
        self.fastapi_object = fastapi.FastAPI(
            title=self.TITLE,
            description=self.DESCRIPTION,
            version=version
        )

        # Include API Router from child package
        self.fastapi_object.include_router(application.api.api_router)

        # Register Startup/Shutdown Handler on FastAPI
        # https://fastapi.tiangolo.com/advanced/events/
        self.fastapi_object.add_event_handler(event_type="startup", func=self.on_startup)
        self.fastapi_object.add_event_handler(event_type="shutdown", func=self.on_shutdown)

    async def on_startup(self) -> None:
        # Init Ressource Object
        self.container.init_resources()

    async def on_shutdown(self) -> None:
        # Shutdown Resource
        self.container.shutdown_resources()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if self.fastapi_object.root_path:
            scope["root_path"] = self.fastapi_object.root_path
        await self.fastapi_object.__call__(scope, receive, send)
