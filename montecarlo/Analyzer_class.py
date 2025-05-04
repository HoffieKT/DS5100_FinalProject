# The Analyzer class
# General Definition
# An Analyzer object takes the results of a single game and computes 
# various descriptive statistical properties about it.

# Specific Methods and Attributes

# An initializer.
# Takes a game object as its input parameter. Throws a ValueError if the 
# passed value is not a Game object.

import numpy as np
import pandas as pd
from Die_class import Die
from Game_class import Game

class Analyzer:

    def __init__(self, game):
        if isinstance(game, Game) == False:
            raise ValueError('Analyzer class was initialized with an object that was not a Game object.')

        self.game = game
        self.results = self.game.show()

# A jackpot method.
# A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.
# Computes how many times the game resulted in a jackpot.
# Returns an integer for the number of jackpots.

    def jackpot(self):
        return self.results.apply(lambda row: row.nunique() == 1, axis = 1).sum()

# A face counts per roll method.
# Computes how many times a given face is rolled in each event.
# For example, if a roll of five dice has all sixes, then the counts 
# for this roll would be  5
#   for the face value ‘6’ and  0
#   for the other faces.
# Returns a data frame of results.
# The data frame has an index of the roll number, face values as columns, and 
# count values in the cells (i.e. it is in wide format)..

    def face_counts(self):
        return self.results.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype(int)

# A combo count method.
# Computes the distinct combinations of faces rolled, along with their counts.
# Combinations are order-independent and may contain repetitions.
# Returns a data frame of results.
# The data frame should have a MultiIndex of distinct combinations and a 
# column for the associated counts.

    def combo_counts(self):
        combinations = self.results.apply(lambda row: tuple(sorted(row)), axis = 1)
        comboCount_df = combinations.value_counts().to_frame('count')
        comboCount_df.index = pd.MultiIndex.from_tuples(comboCount_df.index, names = self.results.columns)
        return comboCount_df

# An permutation count method.
# Computes the distinct permutations of faces rolled, along with their counts.
# Permutations are order-dependent and may contain repetitions.
# Returns a data frame of results.
# The data frame should have a MultiIndex of distinct permutations 
# and a column for the associated counts.

    def permutation_counts(self):
        return self.results.value_counts().to_frame('count')



die = Die(np.array(['1', '2', '3', '4', '5', '6']))
die1  = Die(np.array(['1', '2', '3', '4', '5', '6']))

game = Game([die, die1])
game.play(num_rolls = 1000)

anal = Analyzer(game)
print(anal.jackpot())
print(anal.face_counts())
print(anal.combo_counts())
print(anal.permutation_counts())
print(game.show())