#!/usr/bin/env python3.10
"""
Entrypoint for the Dockerfile of the application
"""
import logging
import sys

import uvicorn

from application import Application
from application.config import application_config_factory

logger = logging.getLogger(__package__)

if __name__ == "__main__":
    try:
        _application_config = application_config_factory()
    except RuntimeError as e:
        logger.critical(msg="Unable to retrieve ApplicationConfig")
        logger.exception(e)
        sys.exit(-1)

    try:
        uvicorn.run(
            app="main:application",
            host=_application_config.uvicorn_host,
            port=_application_config.uvicorn_port,
            workers=_application_config.uvicorn_workers
        )
    except RuntimeError as e:
        logger.critical(msg="Application Crash on uvicorn.run")
        logger.exception(e)
        sys.exit(-1)
    else:
        sys.exit(0)
else:
    application = Application()
