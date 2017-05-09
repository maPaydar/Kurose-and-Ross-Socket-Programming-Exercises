import logging


class Log:
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger()
    logger.setLevel("DEBUG")

    @staticmethod
    def i(msg, *args, **kwargs):
        Log.logger.info(msg, *args, **kwargs)

    @staticmethod
    def d(msg, *args, **kwargs):
        Log.logger.debug(msg, *args, **kwargs)

    @staticmethod
    def w(msg, *args, **kwargs):
        Log.logger.warning(msg, *args, **kwargs)

    @staticmethod
    def setLevel(level="DEBUG"):
        Log.logger.setLevel(level)
