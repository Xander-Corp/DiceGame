from web.service.service import Service
from dicegame.strategies.Strategy import StrategyFactory


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
        self.strategyFactory = StrategyFactory()

    def listStrategies(self):
        """
        List Strategies
        """
        return self.strategyFactory.getStrategyNames()

    def getStrategyDecription(self, stratgeyName):
        """
        Get Strategy Description
        """
        strategy = self.strategyFactory.getStrategy(stratgeyName, None)
        return strategy.description

