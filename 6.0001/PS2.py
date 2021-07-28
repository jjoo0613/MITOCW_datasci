# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')     # inFile: file
    line = inFile.readline() # line: string
    wordlist = line.split() # wordlist: list of strings of words
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist): #return random word from wordlist
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    x=True
    char_secret_word =list(set(secret_word)) 
    for i in char_secret_word:
        if i not in letters_guessed:
            x= False
    return x

def get_guessed_word(secret_word, letters_guessed):
    secret_word_list = list(secret_word)
    word_hidden=['_ ']*len(secret_word)
    count=0
    for guess in letters_guessed: 
        for i in range(len(secret_word)):
            if secret_word_list[i] == guess: 
                word_hidden[i] = guess
                count+=1     
    return "".join(word_hidden)

def get_available_letters(letters_guessed):
    alphabet = list(string.ascii_lowercase)
    for guess in letters_guessed: 
        if guess in alphabet: 
            alphabet.remove(guess)
    return ''.join(alphabet)


def hangman(secret_word):
    print('Welcome to Hangman game!')
    print('I am thinking of a ', len(secret_word), ' letter long word.') 
    print('-----------------')
    count = 6
    letters_used = []
    secretwordlist = list(set(secret_word))
    
    while count >= 0 :
        print('letters you guessed: ', letters_used)
        print('You have total ',count, 'guesses left.')
        print('available: ', get_available_letters(letters_used))
        print('--'*15)
        
        letter=input('Write your guess: ')
        if letter in letters_used: 
            raise ValueError('Error: your guess is already in your guessed list')
        letters_used.append(letter)
       
        if is_word_guessed(secret_word, letters_used): #if True
            print('You have successfully guessed the word: ', secret_word)
            break
        if letter in secretwordlist: 
            print('Your guess ', letter, 'is in the list: ', get_guessed_word(secret_word, letters_used))
        else:         
            print('Your guess ', letter, 'is NOT in the list: ', get_guessed_word(secret_word, letters_used))
            count -=1
        if count ==0:
            print('\n You have used all your guesses!')
            break

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
