
class Registry(object):
    """
    Resgistry
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Registry, cls).__new__(cls)
            cls.__items = {
            }
        return cls._instance

    def registerService(self, key, value):
        self.__items[key] = value

    def getService(self, key):
        return self.__items[key]