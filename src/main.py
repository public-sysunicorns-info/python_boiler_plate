
import uvicorn
import logging
import ssl

from application import Application
from application.config import application_config_factory

logger = logging.getLogger(__package__)

if __name__ == "__main__":
    try:
        _application_config = application_config_factory()
    except Exception as e:
        logger.critical(msg="Unable to retrieve ApplicationConfig")
        logger.exception(e)
    
    try:
        _run = uvicorn.run(
            app="main:application",
            host=_application_config.uvicorn_host,
            port=_application_config.uvicorn_port,
            workers=_application_config.uvicorn_workers
        )
    except Exception as e:
        logger.critical(msg="Application Crash on uvicorn.run")
        logger.exception(e)
        exit(-1)
    else:
        exit(0)
else:
    application = Application()
