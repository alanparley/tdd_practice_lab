import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]

    # Test latest score (the last thing in the list)

    def test_latest(self):
        self.assertEqual(811, latest(self.scores))

        # Test personal best (the highest score in the list)

        # Test top three from list of scores
    # def test_fizz_buzz__3_returns_fizz(self):
    #     self.assertEqual("fizz", fizz_buzz(3))
    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
