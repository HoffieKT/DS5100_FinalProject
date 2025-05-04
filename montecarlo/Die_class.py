#The Die class
# General Definition¶
# A die has  𝑁
#   sides, or “faces”, and  𝑊
#   weights, and can be rolled to select a face.

# For example, a “die” with  𝑁=2
#   is a coin, and a one with

# $N = 6$ is a standard die.
# Normally, dice and coins are “fair,” meaning that the each side

# has an equal weight. An unfair die is one where the weights are
# unequal.
# Each side contains a unique symbol. Symbols may be all alphabetic or all numeric.

# 𝑊
#   defaults to  1.0
#   for each face but can be changed after the object is created.

# The weights are just positive numbers (integers or floats, including  0
#  ), not a normalized probability distribution.

# The die has one behavior, which is to be rolled one or more times.

# Specific Methods and Attributes

# An initializer.
# Takes a NumPy array of faces as an argument. Throws a TypeError if not a NumPy array.
# The array’s data type dtype may be strings or numbers.
# The array’s values must be distinct. Tests to see if the values are distinct and 
# raises a ValueError if not.
# Internally initializes the weights to  1.0
#   for each face.
# Saves both faces and weights in a private data frame with faces in the index.

import numpy as np
import pandas as pd

class Die:

    def __init__(self, faces):
        if isinstance(faces, np.ndarray) == False:
            raise TypeError('faces needs to be a NumPy array.')
        
        if len(faces) != len(set(faces)):
            raise ValueError('All of the faces need to be unique.')
        
        self.__die_df = pd.DataFrame({'weight': [1.0]*len(faces)}, index = faces)

# A method to change the weight of a single side.
# Takes two arguments: the face value to be changed and the new weight.
# Checks to see if the face passed is valid value, i.e. if it is in the die array. 
# If not, raises an IndexError.
# Checks to see if the weight is a valid type, i.e. if it is numeric (integer or float) 
# or castable as numeric. If not, raises a TypeError.

    def weight_changer(self, face_value, new_weight):
        if face_value not in self.__die.df.index:
            raise IndexError(str(face_value) + ' is not in faces')
        
        try:
            new_weight = float(new_weight)
        except TypeError:
            raise TypeError('Weights need to be numeric.')

        if new_weight < 0:
            raise ValueError('Weights need to be positive numbers, including 0.')
        
        self.__die_df.at[face_value, 'weight'] = new_weight

# A method to roll the die one or more times.
# Takes a parameter of how many times the die is to be rolled; defaults to  1
#  .
# This is essentially a random sample with replacement, from the private die data frame, 
# that applies the weights.
# Returns a Python list of outcomes.
# Does not store internally these results.

    def roll(self, num_rolls=1):
        probabilities = self.__die_df['weight'] / self.__die_df['weight'].sum()
        return list(np.random.choice(self.__die_df.index, size=num_rolls, replace=True, p=probabilities))

# A method to show the die’s current state.
# Returns a copy of the private die data frame.

    def show_currentState(self):
        return self.__die_df