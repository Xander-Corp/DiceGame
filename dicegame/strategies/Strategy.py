
class StrategyFactory():
    """
    Strategy Factory

    A class that produces and returns a strategy
    """
    @staticmethod
    def getStrategy(strategyName, threshold=None):
        if strategyName is None:
            return CrawdadStrategy()
        elif strategyName.lower() == "CrawdadStrategy".lower():
            return CrawdadStrategy()
        elif strategyName.lower() == "TylerStrategy".lower():
            return TylerStrategy()
        elif strategyName.lower() == "ThresholdStrategy".lower():
            return ThresholdStrategy(threshold)
        # elif strategyName.lower() == "GreedyThresholdStrategy".lower():
        #     return GreedyThresholdStrategy()
        elif strategyName.lower() == "ExpectedValueStrategy".lower():
            return ExpectedValueStrategy(threshold)
        else:
            raise Exception("{} does not map to a valid strategy!".format(strategyName))

    @staticmethod
    def getStrategyNames():
        return [
            "CrawdadStrategy", "TylerStrategy", "ThresholdStrategy", "ExpectedValueStrategy"
        ]


class Strategy():
    """
    Strategy

    An abstract class representing a set of decisions how to play the dice game
    """
    def __init__(self):
        self.name = "Strategy"

    def shouldReroll(self, rollScoreDoc, cumulativeTurnScore, cumulativeGameScore, otherPlayerScores):
        """
        Should Reroll

        :return:
        """
        return False

class CrawdadStrategy(Strategy):
    """
    CrawdadStrategy

    An extremely risk-loving strategy that will always reroll when possible.
    """

    def __init__(self):
        Strategy.__init__(self)
        self.name = "CrawdadStrategy"

    def shouldReroll(self, rollScoreDoc, cumulativeTurnScore, cumulativeGameScore, otherPlayerScores):
        """
        Should Reroll

        CrawdadStrategy always rerollss

        :param diceRoll:
        :return:
        """
        return True

class TylerStrategy(Strategy):
    """
    TylerStrategy

    An extremely risk-averse strategy that will only reroll when the previous rolls' scores are guaranteed
    """

    def __init__(self):
        Strategy.__init__(self)
        self.name = "TylerStrategy"

    def shouldReroll(self, rollScoreDoc, cumulativeTurnScore, cumulativeGameScore, otherPlayerScores):
        """
        Should Reroll

        TylerStrategy will only reroll when there is an automatic rerolls

        :param diceRoll:
        :return:
        """
        return rollScoreDoc["automaticReroll"]

class ThresholdStrategy(Strategy):
    """
    Threshold Strategy

    A strategy that will continue to roll until a minimum score is reached
    """
    def __init__(self, minScoreThreshold):
        Strategy.__init__(self)
        self.name = "ThresholdStrategy"
        self.minScoreThreshold = minScoreThreshold

    def shouldReroll(self, rollScoreDoc, cumulativeTurnScore, cumulativeGameScore, otherPlayerScores):
        """
        Should Reroll

        ThresholdStrategy will reroll when the previous rolls' scores are guaranteed or when the latest rolls' score is
        less than a specified threshold

        :param diceRoll:
        :return:
        """
        return rollScoreDoc["automaticReroll"] or cumulativeTurnScore < self.minScoreThreshold

class ExpectedValueStrategy(Strategy):
    def __init__(self, expectedValueThreshold):
        Strategy.__init__(self)
        self.name = "ExpectedValueStrategy"
        self.expectedValueThreshold = expectedValueThreshold

    def shouldReroll(self, rollScoreDoc, cumulativeTurnScore, cumulativeGameScore, otherPlayerScores):
        """
        Should Reroll

        ExpectedValueStrategy will reroll when the previous rolls' scores are guaranteed or when the expected value of
        the roll of the remaining dice is above a specified threshold

        :param diceRoll:
        :return:
        """
        expectedValueOfRemainingDice = 100 # TODO -- try to compute this (at least non-recursive)
        return rollScoreDoc["automaticReroll"] or cumulativeTurnScore < self.expectedValueThreshold
