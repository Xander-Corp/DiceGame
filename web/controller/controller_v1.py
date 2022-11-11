import json
from flask import Flask, request, Blueprint, current_app
from web.service.simulation.simulationservice import SimulationService
import logging

controller_v1 = Blueprint('simple_page', __name__, template_folder='templates')
version = 1
ROOT_PATH = "/dicegame/api/v{}".format(version)

@controller_v1.route('{}/'.format(ROOT_PATH))
def hello_world():
    return 'Welcome to the dice game web server!'

@controller_v1.route("{}/simulation/strategies".format(ROOT_PATH))
def list_simulation_strategies():

    try:
        print("Fetching simulation service...")
        simulationService = getService(SimulationService.__class__)
        response = {
            "strategies" : simulationService.listStrategies()
        }
        print("Sending response {}".format(json.dumps(response, indent=4)))
        return response, 200

    except Exception as e:
        error = "Encountered an exception when accessing the simulation service: {}".format(e)
        print(error)
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
        raise Exception("No service found in registry for class {}".format(clazz))
    return service