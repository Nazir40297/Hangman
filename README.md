# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Created a file containing a list of 5 of my favourite fruits. Then used the random module to choose a random fruit from the list. Asked the user for a single letter input. 

Created an if statement which checked the user input whether it is a single letter and whether it was a letter and not a value. Incorporated an else statement which prints a message indicating the input was not valid.

A new file was made which incorporates the functions needed to check the guesses. A while loop was made so the code runs continuously. The user was asked for an input within this while loop. The guess was converted into lowercase. 

2 functions were created namely check_guess and ask_for_input whereby the two loops were included. The check_guess was called in the ask_for_input function and tested outside to make sure the code worked.

Then created a class Hangman. Defining the first __init__ method with the attributes of the game. The attributes included word to be guessed, a list of the letters of the word to be guessed, num letters including a list of the unique letters in the word to be guessed, num lives which is the number of lives the player gets which is set at 5 by default, word list includes the word list and list of guesses which includes a list of the guessed letters.

2 more methods were created within this class namely check_guess and ask_for_input methods. These methods took in the letter guessed by the user and checks if it is in the word to be guessed. If the letter is not in the word to be guessed then a message is printed telling the user they need to try again.

