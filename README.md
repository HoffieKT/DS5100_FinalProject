# DS5100_FinalProject

Metadata:

  Name: Kyle Troy Hoffman
  Project: Monte Carlo Simulator

Synopsis:

  Installation:
    With the montecarlo package (folder) in your current working directory,
    type this in the command line: 
    
    pip install montecarlo 

    You should get a message similar to this if the installation was a            success:

    Successfully built montecarlo
    Installing collected packages: montecarlo
    Successfully installed montecarlo-0.1.17# Pasted code

  Importing:
    To import the montecarlo module and to access its classes, type this line     in your Python notebook or script:

    import montecarlo.montecarlo

  Coded example:
    Creating a dice (Die object):
      dice = Die(np.array(['1', '2', '3', '4', '5', '6'])
    Play a game (Game object):
      game = Game([die, die, die])
      game.play(num_rolls = 1000)
    Analyze game (Analyzer object):
      analyzer = Analyzer(game)
      analyzer.jackpot() # shows number of jackpots

API Description:
    
      class Analyzer(builtins.object)
       |  Analyzer(game)
       |  
       |  The Analyzer class is responsible for providing various descriptive           statitistical properties
       |  about the results from a single game.
       |  
       |  Methods defined here:
       |  
       |  __init__(self, game)
       |      Creates an Analyzer object
       |      
       |      Parameters:
       |          game (Game): A game
       |      
       |      Returns:
       |          N/A
       |  
       |  combo_counts(self)
       |      Computes the count of distinct combinations of faces rolled.
       |      
       |      Parameters:
       |          N/A
       |      
       |      Returns:
       |          pd.DataFrame: MultiIndex data frame with the combinations                     as indices, and a column of associated counts.
       |  
       |  face_counts(self)
       |      Determines how many times a given face value was rolled in each               iteration.
       |      
       |      Parameters:
       |          N/A
       |      
       |      Returns:
       |          pd.DataFrame: Wide format data frame with roll number as                      index, face values as columns and count values in the cells.
       |  
       |  jackpot(self)
       |      Calculates how many times a jackpot (all faces were the same)                 was hit in a game.
       |      
       |      Parameters:
       |          N/A
       |      
       |      Returns:
       |          int: The number of jackpots hit
       |  
       |  permutation_counts(self)
       |      Computes the count of distinct permutations of faces rolled.
       |      
       |      Parameters:
       |          N/A
       |      
       |      Returns:
       |          pd.DataFrame: MultiIndex data frame with the permutations                     as indices, and a column of associated counts.
       |  
       |  --------------------------------------------------------------------
       
      class Die(builtins.object)
       |  Die(faces)
       |  
       |  The Die class represents an object that has N sides (faces) and               weighted probabilities, that can be rolled to select a face.
       |  
       |  Methods defined here:
       |  
       |  __init__(self, faces)
       |      Creates a Die object and saves the faces and weights of the Die               in a private data frame.
       |      
       |      Parameters:
       |          faces (np.ndarray): A NumPy array of faces. Array can                         contain strings or numbers, but values must be distinct.
       |      
       |      Returns:
       |          N/A
       |  
       |  roll(self, num_rolls=1)
       |      Rolls the Die a specified number of times
       |      
       |      Parameters:
       |          num_rolls (int): Number of times to roll the Die. Defaulted                   to 1 if not specified.
       |      
       |      Returns:
       |          list: List of outcomes from the rolls
       |  
       |  show_currentState(self)
       |      Shows the current state of the Die
       |      
       |      Parameters:
       |          N/A
       |      
       |      Returns:
       |          pd.DataFrame: Private Die data frame
       |  
       |  weight_changer(self, face_value, new_weight)
       |      Changes the weight of a specified side (face)
       |      
       |      Parameters:
       |          face_value (str | int | float): Face value that is getting                    its weight changed
       |          new_weight (str | int | float): The new weight for the                        specified face
       |      
       |      Returns:
       |          N/A
       |  
       |  --------------------------------------------------------------------
    
      class Game(builtins.object)
       |  Game(die_list)
       |  
       |  The Game class is made up of one or more similar Die objects, where           a game of rolling the dice can happen one or more times.
       |  
       |  Similar Die objects simply mean they have the same number of sides            and associated faces.
       |  
       |  Methods defined here:
       |  
       |  __init__(self, die_list)
       |      Creates the Game object and saves a die list attribute.
       |      
       |      Parameters:
       |          die_list (list): A list of similar Die objects
       |      
       |      Returns:
       |          N/A
       |  
       |  play(self, num_rolls)
       |      Rolls the Die object(s) a specified number of times, and saves                 the results in a private data frame.
       |      
       |      Parameters:
       |          num_rolls (int): Number of times to roll the Die object(s)
       |      
       |      Returns:
       |          pd.DataFrame: Wide format data frame that contains the                        results of the play
       |  
       |  show(self, df_form='wide')
       |      Shows the results of the most recent play in a specified format
       |      
       |      Parameters:
       |          df_form (str): The desired format of the play results.                         Defaulted to wide format.
       |      
       |      Returns:
       |          pd.DataFrame: A wide or narrow format data frame.
       |  
       |  --------------------------------------------------------------------
