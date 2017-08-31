# Name:Group4
# The game of Hangman

from random import randrange
from random import randint
from string import *
from hangman_lib import *

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    #word=words_dict[randint(0,len(words_dict)+1)]
    return word

# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word ="claptrap" 
letters_guessed=[]
#letters_guessed =["m","c","t","r","l","n"]

def word_guessed():
    '''
    Returns False if the player has successfully guessed the word,
    and True otherwise.
    '''
    global secret_word
    global letters_guessed

    if print_guessed()==secret_word:
        return False
    else:
        return True
    
def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed

    l=[]
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            l.insert(i,secret_word[i])
        else:
            l.insert(i,"-")
    return "".join(l)

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    secret_word=get_word()

    mistakes_made = 0

    while mistakes_made<MAX_GUESSES:

        if word_guessed():
            print mistakes_made,"Mistakes made"
            print MAX_GUESSES-mistakes_made,"Guesses left"
            print print_guessed(),"Gussed"
            ch=raw_input("Enter a guess \n").lower()
            

            if ch in letters_guessed:
                print "Letter already guessed"
                continue
                
            else:
                letters_guessed.append(ch)
                if ch not in secret_word:
                    print_hangman_image(mistakes_made)
                    mistakes_made+=1
        else:
            print "Congratulations ! You guessed the word correctly."
            break
    else:
        print "The word was:",secret_word
        print "Above art has been created by sk"
    
    return None

if __name__=="__main__":
    play_hangman() 
