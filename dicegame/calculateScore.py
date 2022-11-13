import argparse
import logging
import os
import random
from dicegame.strategies.Strategy import StrategyFactory
from dicegame.scoring.scoringCalculator import TraditionalScoringEngine
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Constants
IMAGES_PATH = "readme/images"
WINNING_SCORE = 10000
MODES = [ "simulateTurns", "simulateGames" ]

def rollOneDie():
    """
    Simulates the roll of a single 6-sided die

    :return: An integer in the range [1,6] randomly generated from a uniform distribution
    """
    return random.randint(1,6)

def rollDice(numDice):
    """
    Roll Dice

    Simulates multiple rolls of o 6-sided die

    :param numDice:     The number of dice to roll
    :return:            An array of size numDice each containing an iid random number in the range [1.6]
    """
    diceRolls = []
    for i in range(0,numDice):
        diceRolls.append(rollOneDie())
    return diceRolls


def simulateSinglePlayerGame(strategyName, threshold, scoringEngine):
    """
    Simulate Game

    Simulates one game of the dice game for a single player with the specified strategy and threshold (if relevant)

    :param strategyName:        The name of the strategy for the player involved
    :param threshold:           The numerical threshold to use for the strategy, where relevant
    :param scoringEngine:       The scoring engine for the game
    :return:                    An integer representing the number of turns it took this player to win the game (hit the
                                winning score)
    """
    strategy = StrategyFactory.getStrategy(strategyName, threshold)
    ctr = 0
    cumulativeScore = 0
    while cumulativeScore < WINNING_SCORE:
        ctr += 1
        scoreForTurn, numRollsForTurn = rollDiceWithStrategy(strategy, scoringEngine, cumulativeScore, {})
        cumulativeScore += scoreForTurn
    return cumulativeScore, ctr

def simulateGames(strategyName, threshold, scoringEngine, numGames, saveImages):
    """
    Simulate Games

    Simulates the specified number of games for a single player with the specified strategy and threshold (where relevant)

    :param strategyName:        The name of the strategy for the player involved
    :param threshold:           The numerical threshold to use for the strategy, where relevant
    :param scoringEngine:       The scoring engine for the game
    :param numGames:            An integer representing the number of games to simulate
    :param saveImages:          True to save images, False otherwise
    :return:                    A results JSON payload containing statistics on the number of turns to win per game and
                                the final score of each game
    """
    verboseStrategyName = "{}:{}".format(strategyName, threshold) if threshold is not None else strategyName
    logging.info("Starting simulation of games for strategy " + verboseStrategyName)

    ctr = 0
    numTurnsToWinArr = []
    finalScores = []
    while ctr < numGames:
        ctr += 1
        finalScore, numTurnsToWin = simulateSinglePlayerGame(strategyName, threshold, scoringEngine)
        logging.info("Received final score {} in {} turns for game number {}!".format(finalScore, numTurnsToWin, ctr))
        numTurnsToWinArr.append(numTurnsToWin)
        finalScores.append(finalScore)

    # Stats and plots for number of turns per game
    description = "Number of Turns to Win per Game"
    title = "Number of Turns to Win per Game for Strategy {}".format(verboseStrategyName)
    numTurnsStatsHistogram = generatePlot(numTurnsToWinArr, 1, description, title, saveImages)
    numTurnsStats = generateStatistics(numTurnsToWinArr, description)

    # Stats and plots for final scores
    description = "Final Score for Game"
    title = "Final Score per Game for Strategy {}".format(verboseStrategyName)
    finalScoresStatsHistogram = generatePlot(finalScores, 50, description, title, saveImages)
    finalScoresStats = generateStatistics(finalScores, description)

    # Results
    results = {
        "numTurnsStats" : numTurnsStats,
        "numTurnsStatsHistogram" : numTurnsStatsHistogram,
        "finalScoresStats" : finalScoresStats,
        "finalScoresStatsHistogram" : finalScoresStatsHistogram
    }
    return results


def simulateTurnsWithStrategyAndCalculateStats(strategyName, threshold, scoringEngine, maxNumTurns, saveImages):
    """
    Simulate Turns with Strategy and Calculate Stats

    Simulates a desired number of turns with the specified strategy and threshold (where relevant).

    :param strategyName:        The name of the strategy for the player involved
    :param threshold:           The numerical threshold to use for the strategy, where relevant
    :param scoringEngine:       The scoring engine for the game
    :param maxNumTurns:         The max number of turns to run the simulation for
    :param saveImages:          True to save images, False otherwise
    :return:                    A results JSON payload containing statistics on the number of rolls per turn and the final
                                score per game
    """
    strategy = StrategyFactory.getStrategy(strategyName, threshold)
    strategyName = "{}:{}".format(strategyName, threshold) if threshold is not None else strategyName

    # scoringEngine = TraditionalScoringEngine()

    ctr = 0
    scores = []
    numRollArr = []
    numTurnsToHit10K = 0
    cumulativeScore = 0
    while ctr < maxNumTurns:
        ctr += 1

        # Roll for the turn
        scoreForTurn, numRollsForTurn = rollDiceWithStrategy(strategy, scoringEngine, cumulativeScore, { })

        # Mark when this strategy hits 10K
        cumulativeScore += scoreForTurn
        if cumulativeScore >= WINNING_SCORE and numTurnsToHit10K == 0:
            numTurnsToHit10K = ctr

        # Add scores to arrays
        scores.append(scoreForTurn)
        numRollArr.append(numRollsForTurn)
        logging.info("Received score {} from {} rolls for turn/roll {}!".format(scoreForTurn, numRollsForTurn, ctr))

    # Scores per turn stats and plots
    scores = np.array(scores)
    scoresDescr = "Score for Turn"
    scoresTitle = "Histogram of Scores per Turn ({})".format(strategyName)
    scorePerTurnStatsHistogram = generatePlot(scores, 20, scoresDescr, scoresTitle, saveImages)
    scoresPerTurnStats = generateStatistics(scores, scoresDescr)

    # Number of rolls per turn stats and plots
    numRolls = np.array(numRollArr)
    rollsDescr =  "Number of Rolls for Turn"
    rollsTitle =  "Histogram of Num Rolls per Turn ({})".format(strategyName)
    rollsPerTurnStatsHistogram = generatePlot(numRolls, 10,rollsDescr, rollsTitle, saveImages)
    rollsPerTurnStats = generateStatistics(numRolls, rollsDescr)

    logging.info("User with strategy {} took {} turns to hit 10K!".format(strategyName, numTurnsToHit10K))

    # Results
    results = {
        "scoresPerTurnStats" : scoresPerTurnStats,
        "scoresPerTurnStatsHistogram" : scorePerTurnStatsHistogram,
        "rollsPerTurnStats" : rollsPerTurnStats,
        "rollsPerTurnStatsHistogram" : rollsPerTurnStatsHistogram
    }
    return results

def generatePlot(data, bins, dataDescription, title, save):
    """
    Generate Plot

    Generates a matplotlib.pyplot histogram of the data with the specified number of bins, description, and title

    :param data:                An array of data
    :param bins:                The number of bins to use for the histogram
    :param dataDescription:     A String describing the data, to be used as the X-axis label
    :param title:               A String representing the title of the histogram
    :param save:                True to save images, False otherwise
    """
    logging.debug("Generating plots for data " + dataDescription)
    histogram, bin_edges = np.histogram(data, bins=bins)
    fig, ax = plt.subplots()
    ax.hist(data, bin_edges, cumulative=False)
    ax.set_xlabel(dataDescription)
    ax.set_ylabel('Frequency')
    fig.suptitle(title, fontsize=15)
    fileName = None
    if save:
        fileName = title.replace(" ", "_").replace(":", "-").lower()
        fullName = '../{}/{}'.format(IMAGES_PATH, fileName)
        if os.path.exists(fullName):
            renameFileWithRetry(fullName, "bak")
        plt.savefig(fullName)
    plt.show()
    relativePathFromMainDir = "{}/{}.png".format(IMAGES_PATH, fileName)
    return relativePathFromMainDir

def renameFileWithRetry(fullFileName, suffix):
    """
    Rename File With Retry

    Renames a file incrementally to avoid overwriting other backups

    :param fullFileName:        The full path to the file to rename
    :param suffix:              The suffix that will be used to make a backup
    :return:
    """
    newFileName = "{}.{}".format(fullFileName, suffix)
    pathExists = os.path.exists(newFileName)
    ctr = 0
    while pathExists:
        ctr += 1
        newFileName = "{}.{}.{}".format(fullFileName, suffix, ctr)
        pathExists = os.path.exists(newFileName)

    os.rename(fullFileName, newFileName)


def generateStatistics(data, dataDescription):
    """
    Generate Statistics

    Generates summary statistics about the empirical distribution of the data

    :param data:                An array of data
    :param dataDescription:     A String describing the data
    :return:                    A scipy.statistics object containing summary statistics
    """
    statistics = stats.describe(data, ddof=1, bias=False)
    logging.info("Found statsistics {} for {}".format(statistics, dataDescription))
    statistics = statistics._asdict()
    for key in statistics.keys():
        try:
            if key == "minmax":
                statistics["minmax"] = [
                    statistics["minmax"][0].item(),
                    statistics["minmax"][1].item()
                ]
            else:
                statistics[key] = statistics[key].item()
        except Exception as e:
            logging.error("Encountered exception {} when reformatting statistics".format(e))
    return statistics

def rollDiceWithStrategy(strategy, scoringEngine, cumulativeGameScore, otherPlayerScores):
    """
    Roll Dice with Strategy

    Simulates a turn using the specified strategy, scoring engine, and other miscellaneous exogneous variables (cumulativeGameScore,
    otherPlayerScores), which may affect strategy decision-making

    :param strategy:                A String representing the name of a strategy to use
    :param scoringEngine:           A ScoringEngine object that will score the dice rolls
    :param cumulativeGameScore:     An integer representing the cumulative score for this player, prior to starting this turn
    :param otherPlayerScores:       A JSON payload containing a map of players to ther cumulatiive scores, prior to starting
                                    this turn.
    :return:                        The score for the turn and the number of rolls for the turn
    """
    cumulativeScore = 0
    lockedInScore = 0
    numRolls = 0
    keepRolling = True
    numDiceToRoll = 6
    logging.debug("Starting turn")
    while keepRolling:
        numRolls += 1
        logging.debug("Rolling")
        diceRoll = rollDice(numDiceToRoll)              # Roll the dice
        logging.debug("Calculating score")
        scoreDoc = scoringEngine.score(diceRoll)        # Get the score

        # How many dice are non-scoring -- that is how many we can reroll
        # Unless all the dice in our last roll were scoring, in which case we get to reroll the hand
        numDiceToRoll = 6 if len(scoreDoc["deadRolls"]) == 0 else len(scoreDoc["deadRolls"])

        # If the score from the last roll was 0, meaning that all rolls were dead, your turn is over
        if scoreDoc["optimalScore"] == 0:
            return lockedInScore, numRolls

        # Otherwise, add the non-zero score to our cumulative score. If we rolled a straight, or some other configuration
        # that gives us an automatic reroll, then lock in this score
        cumulativeScore += scoreDoc["optimalScore"]
        if scoreDoc["automaticReroll"]:
            lockedInScore = cumulativeScore

        # Whether or not to keep rolling is determined by the strategy
        keepRolling = strategy.shouldReroll(scoreDoc, cumulativeScore, cumulativeGameScore, otherPlayerScores)
        logging.debug("User with strategy {} will {}keep rolling".format(strategy.name, "" if keepRolling else "not "))
    return cumulativeScore, numRolls


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
    parser.add_argument('--strategy',               required=False,  action="store",         dest='strategy',                default='CrawdadStrategy',   help='Name of the strategy to use. Accepted values are {}'.format(StrategyFactory.getStrategyNames()))
    parser.add_argument('--threshold',              required=False,  action="store",         dest='threshold',               default=None,                help='Integer representing the threshold to use for the Threshold Strategy or Expected value strategy')
    parser.add_argument('--scoringEngine',          required=False,  action="store",         dest='scoringEngine',           default='Traditional',       help='Name of the scoring engine to use. Currently always uses Traditional Scoring Engine')
    parser.add_argument('--numSimulations',         required=False,  action="store",         dest='numSimulations',          default=1000,                help='Number of simulations (number of rolls if simulating rolls. number of games if simulating games)')
    parser.add_argument('--saveImages',             required=False,  action="store_true",    dest='saveImages',              default=False,               help='Include to save images.')
    parser.add_argument('--mode',                   required=False,  action="store",         dest='mode',                    default="simulateTurns",     help='What to simulate. valid options are {}'.format(MODES))
    return parser.parse_args()

def runScript():
    """
    Run Script

    Runs the functionality of the script, assuming command line arguments have not yet been parsed
    """
    args = setupArgs()
    main(args)

def runSimulation(args):
    """
    Run Simulation
    """
    return main(args)

def main(args):
    _configureLogger(args.logLevel.upper())
    random.seed()
    threshold = max(int(args.threshold), 0) if args.threshold is not None else None
    traditionalScoringEngine = TraditionalScoringEngine()
    numSimulations = max(int(args.numSimulations), 0) if args.threshold is not None else 1000

    mode = "simulateTurns"
    if args.mode is not None:
        mode = args.mode.strip()
    if mode == "simulateTurns":
        return simulateTurnsWithStrategyAndCalculateStats(args.strategy, threshold, traditionalScoringEngine, numSimulations, args.saveImages)
    elif mode == "simulateGames":
        return simulateGames(args.strategy, threshold, traditionalScoringEngine, numSimulations, args.saveImages)

#-------------------------------
if __name__ == "__main__":
    runScript()