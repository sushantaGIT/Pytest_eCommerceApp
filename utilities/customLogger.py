import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\automation.log', level=logging.DEBUG, force=True,
                            filemode='w',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m%d%y %H:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
