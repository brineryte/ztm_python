import unittest
from practice_exercises import guessing_game


class TestGuessingGame(unittest.TestCase):

    def test_evaluateGuess(self):
        self.assertTrue(guessing_game.evaluateGuess(1, 1))

    def test_evaluateGuessFalse(self):
        self.assertFalse(guessing_game.evaluateGuess(2, 1))


if __name__ == '__main__':
    unittest.main()
