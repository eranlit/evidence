
from logging.config import dictConfig
import logging
from config import LogConfig

class AppLogger:
    """This class provides an application root logger 
    """
    def __init__(self):
        dictConfig(LogConfig().dict())
        self.logger = logging.getLogger("evidenceapp")


applog = AppLogger()
logger = applog.logger
