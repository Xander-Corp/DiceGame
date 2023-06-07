from flaskApp import MyApp
import os

from util.util import Registry
from web.service.simulation.simulationservice import SimulationService
from web.service.config.configservice import ConfigService
from web.service.jobs.jobsservice import JobsService
from flask_swagger_ui import get_swaggerui_blueprint
import logging

app = None

def wireServices():
    """
    Wire Services

    """
    logging.info("Starting up services")
    serviceRegistry = Registry()

    # Config service must be registered first
    configService = ConfigService(serviceRegistry, "conf/config.yml")

    # Other services can be registered subsequently
    jobsService = JobsService(serviceRegistry)
    simulationService = SimulationService(serviceRegistry)

    # Override default logging
    configureLogger(configService)
    return serviceRegistry

def configureLogger(configService):
    """
    Configure Logger
    """
    format = '%(asctime)s - %(levelname)s - %(message)s'
    loggingLevelConfig = configService.getConfigValue("logging.level")
    logging.info("Configuring logger with logging level '{}'".format(loggingLevelConfig))

    try:
        logging.basicConfig(format=format, level=loggingLevelConfig.upper())
    except:
        message = "Encountered error when attempting to override logger configuration"
        logging.basicConfig(format=format, level=logging.INFO)
        logging.error(message)


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
    logging.info("Registering flask blueprints")

    logging.info("Registering controller controller_v1")
    from web.controller.controller_v1 import controller_v1
    app.register_blueprint(controller_v1)
    return app

def setup_swagger(app):
    """
    Setup Swagger

    """
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Sample API"
        }
    )
    app.register_blueprint(swaggerui_blueprint)
    return app


def start_server():
    """
    Start Server

    """
    format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=format, level=logging.DEBUG)
    serviceRegistry = wireServices()
    app = getFlaskApp(serviceRegistry)
    app = registerBlueprints(app)
    app = setup_swagger(app)
    app.run()

if __name__ == '__main__':
    start_server()
