import yaml
import json
from web.service.service import Service
import logging

class ConfigService(Service):
    """
    Config Service

    A service to fetch the config for the system
    """

    def __init__(self, serviceRegistry, configDirectory):
        """
        Provisioning Service Constructor

        :param serviceRegistry:
        """
        Service.__init__(self, serviceRegistry)
        self.config = yaml.safe_load(open(configDirectory))
        logging.info("Started config service.")
        logging.debug("Loaded config {}".format(json.dumps(self.config, indent=4)))

    def getConfigValue(self, configName):
        logging.info("Getting config with name {}".format(configName))
        configNameParts = configName.split(".")
        value = self.config
        for configNamePart in configNameParts:
            logging.debug("Looking for nested config property {} in {}".format(configNamePart, json.dumps(value, indent=4)))
            if configNamePart in value:
                value = value[configNamePart]
            else:
                logging.info("Config with name {} is not in configuration file".format(configName))
                return None
        logging.info("Found value {} for config {}".format(json.dumps(value, indent=4), configName))
        return value


