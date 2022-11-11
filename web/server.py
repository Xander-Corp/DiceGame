from flaskApp import MyApp
import os

from util.util import Registry
from web.service.simulation.simulationservice import SimulationService
from web.service.config.configservice import ConfigService

app = None

def wireServices():
    """
    Wire Services

    """
    serviceRegistry = Registry()
    simulationService = SimulationService(serviceRegistry)
    serviceRegistry.registerService(SimulationService.__class__, simulationService)

    configService = ConfigService(serviceRegistry, "conf/config.yml")
    serviceRegistry.registerService(ConfigService.__class__, configService)
    configService.getConfigValue("logging.level")

    return serviceRegistry

def getFlaskApp(serviceRegistry):
    """
    Get Flask App
    """
    app = MyApp()
    app.config["SERVICE_REGISTRY"] = serviceRegistry
    return app

def registerBlueprints(app):
    """
    Resgister Blueprints

    Register controllers as blueprints for flask app

    """
    # Register version 1 of the api
    from web.controller.controller_v1 import controller_v1
    app.register_blueprint(controller_v1)
    return app

def start_server():
    """
    Start Server

    """
    serviceRegistry = wireServices()
    app = getFlaskApp(serviceRegistry)
    app = registerBlueprints(app)
    app.run()

if __name__ == '__main__':
    start_server()
