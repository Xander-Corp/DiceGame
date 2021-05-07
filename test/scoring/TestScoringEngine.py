import unittest
import json
from dicegame.scoring.scoringCalculator import TraditionalScoringEngine


class TestTraditionalScoringEngine(unittest.TestCase):

    def setUp(self):
        self.scoringEngine = TraditionalScoringEngine()

    ####################################################################################################################
    # Test Methods
    ####################################################################################################################

    def testStraight(self):
        straightRolls = [ 1, 2, 3, 4, 5, 6]
        scoreDoc = self.scoringEngine.score(straightRolls)

        print("Received scoreDoc {}".format(json.dumps(scoreDoc, indent=4)))

        self.assertIn("diceRolls", scoreDoc)
        self.assertEqual(straightRolls, scoreDoc["diceRolls"])

        self.assertIn("optimalScore", scoreDoc)
        self.assertEqual(1000, scoreDoc["optimalScore"])

        self.assertIn("optimalDiceUsage", scoreDoc)
        self.assertEqual(straightRolls, scoreDoc["optimalDiceUsage"])

        self.assertIn("automaticReroll", scoreDoc)
        self.assertTrue(scoreDoc["automaticReroll"])

    def testDeadRoll(self):
        deadRolls = [2, 2, 3, 3, 4, 4]
        scoreDoc = self.scoringEngine.score(deadRolls)


if __name__ == '__main__':
    unittest.main()
