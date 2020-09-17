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
    def test_personal_best(self):
        self.assertEqual(901, personal_best(self.scores))

    # Test top three from list of scores
    def test_personal_top_three(self):
        self.assertEqual([901, 811, 765], personal_top_three(self.scores))

    # Test ordered from highest to lowest

    def test_highest_to_lowest(self):
        scores = [1, 2, 3]
        self.assertEqual([3, 2, 1], personal_top_three(scores))

    # Test top three when there is a tie
    def test_top_three_tie(self):
        scores = [3, 1, 1, 3, 3, 2]
        self.assertEqual([3, 3, 3], personal_top_three(scores))

    # Test top three when there are less than three
    def test_top_three_when_less_than_three(self):
        scores = [99, 11]
        self.assertEqual([99, 11], personal_top_three(scores))

    # Test top three when there is only one
    def test_top_three_when_only_one(self):
        scores = [100]
        self.assertEqual([100], personal_top_three(scores))
