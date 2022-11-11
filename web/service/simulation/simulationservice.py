from web.service.service import Service
from dicegame.strategies.Strategy import StrategyFactory
import logging

class SimulationService(Service):
    """
    Simulation Service

    Manages the provisioning of hosts, OS, and other miscellaneous base
    """

    def __init__(self, serviceRegistry):
        """
        Provisioning Service Constructor

        :param serviceRegistry:
        """
        Service.__init__(self, serviceRegistry)
        logging.debug("Creating SimulationService")
        self.strategyFactory = StrategyFactory()

    def listStrategies(self):
        """
        List Strategies
        """
        logging.info("Fetching strategy names")
        return self.strategyFactory.getStrategyNames()

    def getStrategyDecription(self, stratgeyName):
        """
        Get Strategy Description
        """
        logging.debug("Getting strategy description for {}".format(stratgeyName))
        strategy = self.strategyFactory.getStrategy(stratgeyName, None)
        return strategy.description

