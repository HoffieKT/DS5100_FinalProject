import numpy as np
import pandas as pd

class Die:
    """
    The Die class represents an object that has N sides (faces) and weighted probabilities,
    that can be rolled to select a face.
    """

    def __init__(self, faces):
        """
        Creates a Die object and saves the faces and weights of the Die in a private data frame.

        Parameters:
            faces (np.ndarray): A NumPy array of faces. Array can contain strings or numbers, but 
                                values must be distinct.

        Returns:
            N/A
        """

        # Check if faces is the correct dtype
        if isinstance(faces, np.ndarray) == False:
            raise TypeError('faces needs to be a NumPy array.')
        
        # Ensure that all the faces are unique (no repeated face values)
        if len(faces) != len(set(faces)):
            raise ValueError('All of the faces need to be unique.')
        
        # Save faces and weights (initialized to 1.0) to a private data frame
        self.__die_df = pd.DataFrame({'weight': [1.0]*len(faces)}, index = faces)

    def weight_changer(self, face_value, new_weight):
        """
        Changes the weight of a specified side (face)

        Parameters:
            face_value (str | int | float): Face value that is getting its weight changed
            new_weight (str | int | float): The new weight for teh specified face

        Returns:
            N/A
        """

        # Checks if the face value is on the Die
        if face_value not in self.__die_df.index:
            raise IndexError(str(face_value) + ' is not in faces')
        
        # See if the new weight is castable to a float (numeric)
        try:
            new_weight = float(new_weight)
        except TypeError:
            raise TypeError('Weights need to be numeric.')

        # Weight needs to be a value greater than or equal to 1
        if new_weight < 0:
            raise ValueError('Weights need to be positive numbers, including 0.')
        
        # Save weight change in the private data frame
        self.__die_df.at[face_value, 'weight'] = new_weight

    def roll(self, num_rolls=1):
        """
        Rolls the Die a specified number of times

        Parameters:
            num_rolls (int): Number of times to roll the Die. Defaulted to 1 if not specified.

        Returns:
            list: List of outcomes from the rolls
        """

        # turn weights into probabilities
        probabilities = self.__die_df['weight'] / self.__die_df['weight'].sum()
        return list(np.random.choice(self.__die_df.index, size=num_rolls, replace=True, p=probabilities))

    def show_currentState(self):
        """
        Shows the current state of the Die

        Parameters:
            N/A

        Returns:
            pd.DataFrame: Private Die data frame
        """

        return self.__die_df
    
class Game:
    """
    The Game class is made up of one or more similar Die objects, where a game of rolling the dice
    can happen one or more times.

    Similar Die objects simply mean they have the same number of sides and associated faces.
    """

    def __init__(self, die_list):
        """
        Creates the Game object and saves a die list attribute.

        Parameters:
            die_list (list): A list of similar Die objects

        Returns:
            N/A
        """

        # Save list of similar Die objects to die_list attribute
        self.die_list = die_list

    def play(self, num_rolls):
        """
        Rolls the Die object(s) a specified number of times, and saves the results in a private data frame.

        Parameters:
            num_rolls (int): Number of times to roll the Die object(s)

        Returns:
            N/A
        """

        # Checks if the number of rolls is an integer greater than 0
        if isinstance(num_rolls, int) == False or num_rolls < 1:
            raise ValueError('The number of rolls needs to be an integer greater than 0.')
        
        # Get the results of each roll iteration for all Die object(s)
        results = {}
        for i in range(len(self.die_list)):
            results[i] = self.die_list[i].roll(num_rolls)

        # Save the results in a private, wide format data frame with the roll_number as the index
        self.__game_df = pd.DataFrame(results)
        self.__game_df.index.name = 'roll number'

    def show(self, df_form='wide'):
        """
        Shows the results of the most recent play in a specified format

        Parameters:
            df_form (str): The desired format of the play results. Defaulted to wide format.
        
        Returns:
            pd.DataFrame: A wide or narrow format data frame.
        """

        # Check if a play as occurred by seeing if the private data frame exists yet
        if hasattr(self, '_Game__game_df') == False:
            raise AttributeError('A game has not been played yet. DataFrame does not exist.')
        
        # Check if a valid form was asked by the user
        if df_form == 'wide':
            return self.__game_df
        elif df_form == 'narrow':
            return self.__game_df.stack()
        else:
            raise ValueError('Requested form needs to be wide or narrow.')
        
class Analyzer:
    """
    The Analyzer class is responsible for providing various descriptive statitistical properties
    about the results from a single game.
    """

    def __init__(self, game):
        """
        Creates an Analyzer object

        Parameters:
            game (Game): A game

        Returns:
            N/A
        """
        if isinstance(game, Game) == False:
            raise ValueError('Analyzer class was initialized with an object that was not a Game object.')

        self.game = game
        self.results = self.game.show()

    def jackpot(self):
        """
        Calculates how many times a jackpot (all faces were the same) was hit in a game.

        Parameters:
            N/A

        Returns:
            int: The number of jackpots hit
        """
        return int(self.results.apply(lambda row: row.nunique() == 1, axis = 1).sum())

    def face_counts(self):
        """
        Determines how many times a given face value was rolled in each iteration.

        Parameters:
            N/A

        Returns:
            pd.DataFrame: Wide format data frame with roll number as index, face values as columns
                          and count values in the cells.
        """
        return self.results.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype(int)

    def combo_counts(self):
        """
        Computes the count of distinct combinations of faces rolled.

        Parameters:
            N/A

        Returns:
            pd.DataFrame: MultiIndex data frame with the combinations as indices, and a column of 
                          associated counts.
        """

        # Get the distinct combinations
        combinations = self.results.apply(lambda row: tuple(sorted(row)), axis = 1)
        # Get the counts of the distinct combinations
        comboCount_df = combinations.value_counts().to_frame('count')
        # Turn tuple single index into a MultiIndex
        comboCount_df.index = pd.MultiIndex.from_tuples(comboCount_df.index, names = self.results.columns)
        return comboCount_df

    def permutation_counts(self):
        """
        Computes the count of distinct permutations of faces rolled.

        Parameters:
            N/A

        Returns:
            pd.DataFrame: MultiIndex data frame with the permutations as indices, and a column of 
                          associated counts.
        """

        # Get the distinct permutations
        permutations = self.results.apply(lambda row: tuple(row), axis = 1)
        # Get the counts of the distinct permutations
        permCount_df = permutations.value_counts().to_frame('count')
        # Turn the tuple single index into a MultiIndex
        permCount_df.index = pd.MultiIndex.from_tuples(permCount_df.index, names = self.results.columns)
        return permCount_df
