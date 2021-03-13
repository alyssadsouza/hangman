# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        response = False
        if letter in lettersGuessed:
            response = True
        if response == False:
            break
    return response



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    my_word = ""
    
    for i in secretWord:
        if i in lettersGuessed:
            my_word += " " + i + " "
        else:
            my_word += " _ "
    
    return my_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    
    available = ''
    
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available += letter
    
    return available
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    
    print('Welcome to the game, Hangman!\nI am thinking of a word that is', len(secretWord), 'letters long.')
    guessesLeft = 8
    print('----------------------------------')
    
    while guessesLeft > 0:
        print('You have', guessesLeft, 'guesses left.\nAvailable letters:', availableLetters)
        guess = input('Please guess a letter: ').lower()
        
        if guess.isalpha():
            if guess not in availableLetters:
                print('Oops! You\'ve already guessed that letter:', getGuessedWord(secretWord, lettersGuessed))
        
            elif guess not in secretWord:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                availableLetters = getAvailableLetters(lettersGuessed)
                guessesLeft -= 1
                
            else:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                availableLetters = getAvailableLetters(lettersGuessed)
                
        else:
            print('Oops! That\'s not a letter!', getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        
        guessWord = input('Would you like to guess the word? Type \'yes\' or \'enter\' to continue: ')
        
        if guessWord.lower() == 'yes':
            wordGuess = input('Guess the word: ')
            if wordGuess == secretWord:
                print('Congratulations, you won!')
                guessed = True
                break
            else:
                print('Sorry, that\'s not the word!')
        
        print('----------------------------------')
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            guessed = True
            break
    
    if not guessed:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
