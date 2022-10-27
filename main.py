from itertools import count
import random
from list import words

list = words
secret_word = random.choice(list)
guess=""
guess_count = 0
guess_limit = 5
out_of_guessses = False


while guess!=secret_word and not (out_of_guessses):
    if guess_count<guess_limit:
        guess = input("Please guess a word: ")
        guess_count +=1
        print("you used " + str(guess_count))
    else:
        out_of_guessses=True


if out_of_guessses:
    print("out of guesses you lose")
    print("the word was " + str(secret_word))
else:
    print("good job you win")
    print("the word was " + str(secret_word))


input("press any key to exit")


