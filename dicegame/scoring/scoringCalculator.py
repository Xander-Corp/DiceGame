
class ScoringEngine():

    def __init__(self):
        self.nothing = ""
    def score(self, diceRolls):
        return {
            "diceRolls" : diceRolls,
            "optimalScore" : [],
            "optimalDiceUsage" : []
        }
    def getRollMap(self, diceRolls):
        rollMap = {}
        for diceRoll in diceRolls:
            if diceRoll not in rollMap:
                rollMap[diceRoll] = 1
            else:
                rollMap[diceRoll] += 1
        return rollMap

class TraditionalScoringEngine(ScoringEngine):
    """

    """

    def __init__(self):
        ScoringEngine.__init__(self)

    def isDeadRoll(self, roll):
        return roll in [2, 3, 4, 6]

    def isStraight(self, rollMap):
        if len(rollMap.keys()) < 6:
            return False
        for roll in rollMap.keys():
            if rollMap[roll] != 1:
                return False
        return True

    # TODO -- test this
    def score(self, diceRolls):
        rollMap = self.getRollMap(diceRolls)
        scoreDoc = {
            "diceRolls": diceRolls,
            "optimalScore": 0,
            "optimalDiceUsage": [],
            "deadRolls" : [],
            "automaticReroll" : False
        }

        # Check for straight
        if self.isStraight(rollMap):
            scoreDoc["optimalScore"] = 1000
            scoreDoc["optimalDiceUsage"] = list(rollMap.keys())
            scoreDoc["automaticReroll"] = True
            return scoreDoc

        for roll in rollMap.keys():
            numRollsAtValue = rollMap[roll]

            if numRollsAtValue >= 3:
                if roll == 1:
                    scoreMultiplier = pow(2, max(numRollsAtValue - 3, 0))
                    scoreDoc["optimalScore"] += 1000 * scoreMultiplier
                    for i in range(0, numRollsAtValue):
                        scoreDoc["optimalDiceUsage"].append(roll)
                else:
                    scoreMultiplier = pow(2, max(numRollsAtValue - 3, 0))
                    scoreDoc["optimalScore"] += roll * 100 * scoreMultiplier
                    for i in range(0, numRollsAtValue):
                        scoreDoc["optimalDiceUsage"].append(roll)

            # If the dice value cast was rolled fewer than 3 times and is not a dead roll, it is non-scoring
            elif self.isDeadRoll(roll):
                for i in range(0, numRollsAtValue):
                    scoreDoc["deadRolls"].append(roll)

            # Otherwise, if the dice value cast was a 1 or a 5 and was cast less than 3 times
            else:
                scoreMultiplier = numRollsAtValue
                diceValue = 100 if roll == 1 else 50
                scoreDoc["optimalScore"] +=  diceValue * scoreMultiplier
                for i in range(0, numRollsAtValue):
                    scoreDoc["optimalDiceUsage"].append(roll)
        return scoreDoc