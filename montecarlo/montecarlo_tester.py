import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer

class MonteCarloTestSuite(unittest.TestCase):

    def test_Die__init__(self):
        self.assertTrue(Die(np.array(['H', 'T'])), Die)

    def test_Die_weight_changer(self):
        die = Die(np.array(['H', 'T']))
        die.weight_changer('T', 5)
        self.assertEqual(die.show_currentState().loc['T', 'weight'], 5)

    def test_Die_roll(self):
        die = Die(np.array(['H', 'T']))
        results = die.roll(10)
        self.assertTrue(isinstance(results, list))
        self.assertEqual(len(results), 10)

    def test_Die_show_currentState(self):
        die = Die(np.array(['H', 'T']))
        self.assertTrue(isinstance(die.show_currentState(), pd.DataFrame))

    def test_Game__init__(self):
        die = Die(np.array(['H', 'T']))
        self.assertTrue(isinstance(Game([die, die]), Game))

    def test_Game_play(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        self.assertEqual(game.show().index.nlevels, 1)

    def test_Game_show(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        self.assertTrue(isinstance(game.show(df_form='narrow').index, pd.MultiIndex))

    def test_Analyzer__init__(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        self.assertTrue(isinstance(Analyzer(game), Analyzer))

    def test_Analyzer_jackpot(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        analyzer = Analyzer(game)
        self.assertTrue(isinstance(analyzer.jackpot(), int))

    def test_Analyzer_face_counts(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        analyzer = Analyzer(game)
        self.assertTrue(isinstance(analyzer.face_counts(), pd.DataFrame))

    def test_Analyzer_combo_counts(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        analyzer = Analyzer(game)
        self.assertTrue(isinstance(analyzer.combo_counts().index, pd.MultiIndex))

    def test_Analyzer_permutation_counts(self):
        die = Die(np.array(['H', 'T']))
        game = Game([die, die])
        game.play(num_rolls=5)
        analyzer = Analyzer(game)
        self.assertTrue(isinstance(analyzer.permutation_counts().index, pd.MultiIndex))

if __name__ == '__main__':
    unittest.main(verbosity=3)
