# The Game class
# General Definition
# A game consists of rolling of one or more similar dice (Die objects) one or more times.

# By similar dice, we mean that each die in a given game has the 
# same number of sides and associated faces, but each die object may have its own weights.

# Each game is initialized with a Python list that contains one or more dice.

# Game objects have a behavior to play a game, i.e. to roll all of the 
# dice a given number of times.

# Game objects only keep the results of their most recent play.

# Specific Methods and Attributes

from Die_class import Die
import numpy as np
import pandas as pd

class Game:

# An initializer.
# Takes a single parameter, a list of already instantiated similar dice.
# Ideally this would check if the list actually contains Die objects and 
# that they all have the same faces, but this is not required for this project.

    def __init__(self, die_list):
        self.die_list = die_list

# A play method.
# Takes an integer parameter to specify how many times the dice should be rolled.
# Saves the result of the play to a private data frame.
# The data frame should be in wide format, i.e. have the roll number as a named index, 
# columns for each die number (using its list index as the column name), and the 
# face rolled in that instance in each cell.

    def play(self, num_rolls):
        if isinstance(num_rolls, int) == False or num_rolls < 1:
            raise ValueError('The number of rolls needs to be an integer greater than 0.')
        
        results = {}
        for i in range(len(self.die_list)):
            results[i] = self.die_list[i].roll(num_rolls)

        self.__game_df = pd.DataFrame(results)
        self.__game_df.index.name = 'roll number'

# A method to show the user the results of the most recent play.
# This method just returns a copy of the private play data frame to the user.
# Takes a parameter to return the data frame in narrow or wide form 
# which defaults to wide form.
# The narrow form will have a MultiIndex, comprising the roll number and the 
# die number (in that order), and a single column with the outcomes (i.e. the face rolled).
# This method should raise a ValueError if the user passes an 
# invalid option for narrow or wide.

    def show(self, df_form='wide'):
        if hasattr(self, '_Game__game_df') == False:
            raise AttributeError('A game has not been played yet. DataFrame does not exist.')
        
        if df_form == 'wide':
            return self.__game_df
        elif df_form == 'narrow':
            return self.__game_df.stack()
        else:
            raise ValueError('Requested form needs to be wide or narrow.')