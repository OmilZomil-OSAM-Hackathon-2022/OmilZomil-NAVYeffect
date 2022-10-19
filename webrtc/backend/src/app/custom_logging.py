from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, format="{time:HH:mm:ss} {level} {message}", level="DEBUG")
logger.add(sys.stdout, format="{time:HH:mm:ss} {level} {extra[ip]} {message} ", 
    filter=lambda record: "ip" in record["extra"], level="DEBUG"
)





logger.debug("hello world")
logger.info("hello world")
logger.warning("hello world")
