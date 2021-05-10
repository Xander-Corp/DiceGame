from strategies.Strategy import StrategyFactory
import calculateScore
import argparse
import logging
import json
import math

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
    parser = argparse.ArgumentParser(description='Calculate statistics on scores of the Dice Game resulting from a particular strategy')

    # Atlas configurations
    parser.add_argument('--loglevel',               required=False,  action="store",         dest='logLevel',                default='info',              help='Log level. Possible values are [none, info, debug]')
    parser.add_argument('--scoringEngine',          required=False,  action="store",         dest='scoringEngine',           default='Traditional',       help='Name of the scoring engine to use. Currently always uses Traditional Scoring Engine')
    parser.add_argument('--numSimulations',         required=False,  action="store",         dest='numSimulations',          default=1000,                help='Number of simulations (number of rolls if simulating rolls. number of games if simulating games)')
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

    # strategies = ["CrawdadStrategy", "TylerStrategy", "ThresholdStrategy" ]
    modes = ["simulateGames", "simulateTurns"]
    # thresholds = [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ]
    thresholds = [ 210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
                   310, 320, 330, 340, 350, 360, 370, 380, 390, 400 ]
    results = {
    }
    for strategy in StrategyFactory.getStrategyNames():
        # Skip for now
        if strategy in ["ExpectedValueStrategy"]:
            continue

        args.loglevel = None
        args.strategy = strategy
        args.threshold = None
        for mode in modes:
            args.mode = mode

            if strategy in ["CrawdadStrategy", "TylerStrategy"]:
                    logging.info("Running simulations on strategy {} and mode {}".format(strategy, mode))

                    strategyName = strategy
                    if strategyName not in results:
                        results[strategyName] = { }
                    if mode not in results[strategyName]:
                        results[strategyName][mode] = { }
                    results[strategyName][mode] = calculateScore.main(args)
            else:
                for threshold in thresholds:
                    logging.info("Running simulations on strategy {} and threshold {}".format(strategy, threshold))
                    args.threshold = threshold

                    strategyName = "{}:{}".format(strategy, threshold)
                    if strategyName not in results:
                        results[strategyName] = {}
                    if mode not in results[strategyName]:
                        results[strategyName][mode] = {}
                    results[strategyName][mode] = calculateScore.main(args)

    # Print results
    logging.info("Printing results...")
    logging.info(json.dumps(results, indent=4))

    for key in results.keys():
        numTurnsToWin = "{}|{}".format(results[key]["simulateGames"]["numTurnsStats"]["mean"],
                                       math.sqrt(results[key]["simulateGames"]["numTurnsStats"]["variance"]))
        finalScores = "{}|{}".format(results[key]["simulateGames"]["finalScoresStats"]["mean"],
                                       math.sqrt(results[key]["simulateGames"]["finalScoresStats"]["variance"]))
        scoresPerTurn = "{}|{}".format(results[key]["simulateTurns"]["scoresPerTurnStats"]["mean"],
                                       math.sqrt(results[key]["simulateTurns"]["scoresPerTurnStats"]["variance"]))
        rollsPerTurn = "{}|{}".format(results[key]["simulateTurns"]["rollsPerTurnStats"]["mean"],
                                       math.sqrt(results[key]["simulateTurns"]["rollsPerTurnStats"]["variance"]))
        logging.info("|{}|{}|{}|{}|{}|".format(key, numTurnsToWin, finalScores, scoresPerTurn, rollsPerTurn))

#-------------------------------
if __name__ == "__main__":
    runScript()