import logging

class Registry(object):
    """
    Resgistry
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logging.info("Creating registry")
            cls._instance = super(Registry, cls).__new__(cls)
            cls.__items = {
            }
        return cls._instance

    def registerService(self, key, value):
        logging.info("Registering service with class {}".format(key))
        self.__items[key] = value

    def getService(self, key):
        logging.debug("Fetching service with class {}".format(key))
        return self.__items[key]