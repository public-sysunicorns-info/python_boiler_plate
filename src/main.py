
import uvicorn
import logging
import ssl

from application import Application

logger = logging.getLogger(__package__)

if __name__ == "__main__":
    try:
        _run = uvicorn.run(
            app="main:application",
            host="0.0.0.0",
            port=8080
        )
    except Exception as e:
        logger.critical(msg="Application Crash on uvicorn.run")
        logger.exception(e)
        exit(-1)
    else:
        exit(0)
else:
    application = Application()
