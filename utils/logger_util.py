"""
Module of logger_util. Class Logger is represented in this module.
"""
import logging
from utils.singleton_util import Singleton
from typing import Optional


class Logger(metaclass=Singleton):
    """
    Class Logger contains method of getting logger.
    Logger is based on Singleton metaclass for keep the only instance of logger.
    Methods: logger. This method returns instance of logger.
    """
    __logger: Optional[logging.Logger] = None

    def logger(self):
        """
        Method is for configuring and getting logger
        :return: Instance of logger.
        """

        if self.__logger is None:
            self.__logger = logging.getLogger(Logger.__name__)
            self.__logger.setLevel(level=logging.DEBUG)
            ch = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            ch.setFormatter(formatter)
            self.__logger.addHandler(ch)
        return self.__logger
