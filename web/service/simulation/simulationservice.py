from web.service.service import Service
from web.service.jobs.jobsservice import JobsService
from dicegame.strategies.Strategy import StrategyFactory
import logging
import json
from datetime import date, datetime
from bson import json_util

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
        self.jobsService = serviceRegistry.getService(JobsService)

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

    def startSimulation(self, strategyName, params):
        """
        Start Simulation
        """
        logging.debug("Starting simulation for strategy {} and params {}".format(strategyName, json.dumps(params, indent=4)))
        jobId = self.jobsService.createJob("Simulate.{}".format(strategyName), params=params)

        # Start job
        state = "inProg"
        logEntry = { "date" : datetime.utcnow(), "log" : "started simulation" }
        self.jobsService.updateJob(str(jobId), state, logEntry)

        # Perform simulation
        state = "complete"
        logEntry = {"date": datetime.utcnow(), "log": "completed simulation"}
        results = { "avg" : 100 }
        self.jobsService.updateJob(str(jobId), state, logEntry, results=results)
        return jobId

    def fetchSimulation(self, jobId):
        """
        Fetch Simulation

        """
        logging.debug("Fetching job with id {}".format(jobId))
        jobDoc = self.jobsService.getJob(jobId)
        logging.debug("Found job {}".format(json_util.dumps(jobDoc, indent=4)))
        return jobDoc
