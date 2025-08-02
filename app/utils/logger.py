import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("comfyapi")

def debug(msg):
    logger.debug(msg)
