import yaml
import json
from web.service.service import Service

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

    def getConfigValue(self, configName):
        configNameParts = configName.split(".")
        value = self.config
        for configNamePart in configNameParts:
            if configNamePart in value:
                value = value[configNamePart]
            else:
                print("Config with name {} is not in configuration file".format(configName))
                return None
        print("Found value {} for config {}".format(json.dumps(value, indent=4), configName))
        return value


