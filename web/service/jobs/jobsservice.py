import yaml
import json
from web.service.service import Service
from web.service.config.configservice import ConfigService
import logging
from pymongo import MongoClient, write_concern
from datetime import date, datetime
from bson import json_util, ObjectId

MONGO_CONN_URI_CONFIG_NAME = "db.mongodb.connectionUri"
GLOBAL_MONGODB_WRITE_CONCERN = write_concern.WriteConcern(
    w="majority",
    wtimeout=5000
)

class JobsService(Service):
    """
    Config Service

    A service to fetch the config for the system
    """

    def __init__(self, serviceRegistry):
        """
        Provisioning Service Constructor

        :param serviceRegistry:
        """
        Service.__init__(self, serviceRegistry)
        logging.info("Started jobs service.")

        # TODO -- move this to separate DAO
        configService = serviceRegistry.getService(ConfigService)

        logging.info("Setting up MongoDB connection")
        mongoConnUri = configService.getConfigValue(MONGO_CONN_URI_CONFIG_NAME)
        self.mongoClient = MongoClient(mongoConnUri)
        self.diceGameDB = self.mongoClient["dicegame"]
        self.jobsColl = self.diceGameDB["jobs"].with_options(
            write_concern=GLOBAL_MONGODB_WRITE_CONCERN
        )


    def createJob(self, jobName, params):
        """
        Create Job

        Creates a job and assigns a unique id
        """
        jobDoc = {
            "state" : "new",
            "name" : jobName,
            "params" : params,
            "lastUpdate" : datetime.now()
        }
        result = self.jobsColl.insert_one(jobDoc)
        resultJson = {
            "acknowledged" : result.acknowledged,
            "inserted_id" : result.inserted_id
        }
        logging.debug("Got result {}".format(json_util.dumps(resultJson, indent=4)))
        return result.inserted_id

    def getJob(self, jobId):
        """
        Get Job

        """
        queryDoc = {
            "_id" : ObjectId(jobId)
        }
        removeId = {
            "_id" : 0
        }
        result = self.jobsColl.find_one(queryDoc, removeId)
        logging.debug("Got result {}".format(json_util.dumps(result, indent=4)))
        return result

    def updateJob(self, jobId, state, logs, results=None):
        """
        Update Job
        """
        queryDoc = {
            "_id": ObjectId(jobId)
        }
        updateDoc = {
            "$set" : {
                "state" : state,
                "lastUpdate" : datetime.now()
            },
            "$push" : {
                "logs" : logs
            }
        }
        if results is not None:
            updateDoc["$set"]["results"] = results
        logging.debug("Sending update with query {} and update spec {} to MongoDB".format(
            json_util.dumps(queryDoc, indent=4),
            json_util.dumps(updateDoc, indent=4)
        ))
        result = self.jobsColl.update_one(queryDoc, updateDoc)
        resultJson = {
            "acknowledged" : result.acknowledged,
            "matched_count" : result.matched_count,
            "modified_count" : result.modified_count,
            "upserted_id" : result.upserted_id,
        }
        logging.debug("Got result {}".format(json_util.dumps(resultJson, indent=4)))
        return result