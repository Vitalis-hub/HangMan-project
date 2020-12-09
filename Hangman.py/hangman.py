import random
from words import hangman_words

def get_word():
    word = random.choice(hangman_words)
    return word.upper()



def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to the hangman game!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        #if first guess and is an alphabet
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                #shows the user how many words were guessed correctly
                word_as_list = list(word_completion)
                positions = [i for i, letter in enumerate(word) if letter == guess]
                for index in positions:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("congrats, you guessed the word. You wins!")

    else:
        print("You are out of trials. The word was " + word)


    #elif len(guess) == len(word) and guess.isalpha():



def display_hangman(tries):
    stages = [ """
        
        
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |        |
                    |       / \\
                    -
                 """
                    ,
                """
                     -------
                     |      |
                     |     \\|/
                     |       |
                     |      /
                     -
                """
                   ,
                """
                
                      --------
                      |       |
                      |       O
                      |      \\|/
                      |        |
                      -
                """
                   ,
                """
                
                    ---------
                    |        |
                    ]        O
                    |       \\|
                    |         |
                    -
                """
                    ,
                """

                    ---------
                    |        |
                    |        O
                    |        |
                    |        |
                    |
                    -
                """
                   ,
                """

                    --------
                    |      |
                    |      O
                    |
                    |
                    |
                    -
                """
                    ,
                """

                    --------
                    |      |
                    |
                    |
                    |
                    |
                    -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again (Y/N) ").upper() == 'Y' :
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
