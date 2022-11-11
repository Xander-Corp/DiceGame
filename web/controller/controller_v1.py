import json
import traceback

from flask import Flask, request, Blueprint, current_app
from web.service.simulation.simulationservice import SimulationService
import logging

controller_v1 = Blueprint('simple_page', __name__, template_folder='templates')
version = 1
ROOT_PATH = "/dicegame/api/v{}".format(version)

@controller_v1.route('{}/'.format(ROOT_PATH))
def hello_world():
    logging.info("Received request at index")
    return 'Welcome to the dice game web server!'

@controller_v1.route("{}/simulation/strategies".format(ROOT_PATH))
def list_simulation_strategies():
    logging.info("Received request at {}/simulation/strategies".format(ROOT_PATH))

    try:
        logging.info("Fetching simulation service...")
        simulationService = getService(SimulationService.__class__)
        response = {
            "strategies" : simulationService.listStrategies()
        }
        logging.info("Sending response {}".format(json.dumps(response, indent=4)))
        return response, 200

    except Exception as e:
        error = "Encountered an exception when accessing the simulation service: {}".format(e)
        logging.error(error)
        return error, 500

@controller_v1.route("{}/simulation/strategies/<strategyName>/description".format(ROOT_PATH), methods=['GET'])
def describe_simulation_strategies(strategyName=None):
    logging.info("Received request at {}/simulation/strategies/<strategyName>/description".format(ROOT_PATH))
    response = {
        "strategyName" : "None",
        "description" : "N/A",
        "msg" : ""
    }
    if strategyName is None:
        message = "No strategy name specified"
        response["msg"] = message
        logging.info(message)
        return response, 200

    response["strategyName"] = strategyName
    strategyName = strategyName.lower()
    try:
        logging.info("Fetching simulation service...")
        simulationService = getService(SimulationService)
        simulationStrategies = [ strategy.lower() for strategy in simulationService.listStrategies()]

        if strategyName not in simulationStrategies:
            response["msg"] = "Strategy {} not a valid strategy".format(strategyName)
            return response, 200

        strategyDescription = simulationService.getStrategyDecription(strategyName)
        response["description"] = strategyDescription
        logging.info("Sending response {}".format(json.dumps(response, indent=4)))
        return response, 200

    except Exception as e:
        error = "Encountered an exception when accessing the simulation service: {}".format(e)
        logging.error(error)
        logging.error(traceback.format_exc())
        return error, 500

def getService(clazz):
    """
    Get Service

    Gets a service from the service registry

    :param clazz:
    :return:
    """
    serviceRegistry = current_app.config["SERVICE_REGISTRY"]
    service = serviceRegistry.getService(clazz)
    if service is None:
        message = "No service found in registry for class {}".format(clazz)
        logging.error(message)
        raise Exception(message)
    return service