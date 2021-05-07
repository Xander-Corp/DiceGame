import argparse
import logging
import random
import json
from dicegame.scoring.scoringCalculator import TraditionalScoringEngine


def getScoringEngine(engineName):
    """
    Get Scoring Engine

    A scoring engine factory method. Currently only supports TraditionalScoringEngine
    :param engineName:
    :return:
    """
    if engineName is None:
        return TraditionalScoringEngine()
    elif "traditional" == engineName.lower():
        return TraditionalScoringEngine()
    else:
        return TraditionalScoringEngine()

def getDiceRolls(diceRollStr):
    """
    Get Dice Rolls

    :param diceRollStr:
    :return:
    """
    diceRolls = []
    if diceRollStr is not None:
        logging.debug("Using user-defined dice rolls")
        diceRollParts = diceRollStr.split(",")
        ctr = 0
        for diceRoll in diceRollParts:
            diceRoll = int(diceRoll)
            if diceRoll > 6 or diceRoll < 1:
                raise Exception("Dice rolls must be in the range [1,6]")
            diceRolls.append(int(diceRoll))
            if ctr == 6:
                break
            ctr +=1

        # if len(diceRollParts) < 6:
        #     numDiceToAdd = 6 - ctr
        #     for diceRoll in generateRandomDiceRolls(numDiceToAdd):
        #         diceRolls.append(diceRoll)
    else:
        logging.debug("Using randomly generated dice rolls")
        diceRolls = generateRandomDiceRolls(6)
    return diceRolls

def generateRandomDiceRolls(numRolls):
    diceRolls = []
    for i in range(0, numRolls):
        diceRolls.append(random.randint(1, 6))
    return diceRolls


def _configureLogger(logLevel):
    format = '%(message)s'
    if logLevel != 'INFO':
        format = '%(levelname)s: %(message)s'
    logging.basicConfig(format=format, level=logLevel.upper())


def setupArgs():
    """
    Setup args
    Parses all command line arguments to the script
    """
    parser = argparse.ArgumentParser(description='')

    # Atlas configurations
    parser.add_argument('--loglevel',               required=False,  action="store",         dest='logLevel',                default='info',                   help='Log level. Possible values are [none, info, debug]')
    parser.add_argument('--diceRolls',              required=False,  action="store",         dest='diceRolls',               default=None,                     help='Log level. Possible values are [none, info, debug]')
    parser.add_argument('--scoringEngine',          required=False,  action="store",         dest='scoringEngine',           default="traditional",            help='Log level. Possible values are [none, info, debug]')
    return parser.parse_args()

def runScript():
    """
    Run Script

    Runs the functionality of the script, assuming command line arguments have not yet been parsed
    """
    args = setupArgs()
    main(args)

def main(args):
    _configureLogger(args.logLevel.upper())
    random.seed()
    diceRolls = getDiceRolls(args.diceRolls)
    logging.info("Using dice rolls {}...".format(diceRolls))
    scoringEngine = getScoringEngine(args.scoringEngine)
    scoreDoc = scoringEngine.score(diceRolls)
    logging.info("Got score: {}".format(json.dumps(scoreDoc, indent=4)))

#-------------------------------
if __name__ == "__main__":
    runScript()