
import fastapi
from starlette.types import Receive, Scope, Send
from dependency_injector import wiring

from .config import ApplicationConfig
from .container import Container
import application.api


class Application:

    fastapi_object: fastapi.FastAPI = None
    container: Container
    application_config: ApplicationConfig = wiring.Provide[Container.application_config]
    
    def _init_container(self):
        """
            Initialize and wire dependency-injection
            to the Application and API modules
        """
        self.container = Container()
        self.container.wire(modules=[
            __name__,
            application.api
        ])

    def _init_fastapi(self):
        """
            Initialize FastAPI Object, include api_router and related event_handler
        """
        self.fastapi_object = fastapi.FastAPI(
            title=self.application_config.name,
            description=self.application_config.description,
            version=self.application_config.version
        )

        # Include API Router from child package
        self.fastapi_object.include_router(application.api.api_router)

        # Register Startup/Shutdown Handler on FastAPI
        # https://fastapi.tiangolo.com/advanced/events/
        self.fastapi_object.add_event_handler(event_type="startup", func=self.on_startup)
        self.fastapi_object.add_event_handler(event_type="shutdown", func=self.on_shutdown)

    def __init__(self) -> None:
        """
            Instanciate Application Object by launch init of child object
        """
        self._init_container()
        self._init_fastapi()

    async def on_startup(self) -> None:
        """
            EventHandler on StartUp for FastAPI Object and ASGI
        """
        # Init Ressource Object
        self.container.init_resources()

    async def on_shutdown(self) -> None:
        """
            EventHandler on ShutDown for FastAPI Object and ASGI
        """
        # Shutdown Resource
        self.container.shutdown_resources()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """
            ASGI handler Proxy for FastAPI Handler
        """
        if self.fastapi_object.root_path:
            scope["root_path"] = self.fastapi_object.root_path
        await self.fastapi_object.__call__(scope, receive, send)
