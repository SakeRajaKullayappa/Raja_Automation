import logging

logging.basicConfig(filename=".\\Logs\\automation.logs")


class GenLogs:

    @staticmethod
    def logGen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
