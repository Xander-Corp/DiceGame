

class Service():

    def __init__(self, serviceRegistry):
        self.serviceRegistry = serviceRegistry
        self.register()

    def register(self):
        self.serviceRegistry.registerService(self.__class__, self)
