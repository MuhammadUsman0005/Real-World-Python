# JUMBLE WORD GAME
# This is a simple game where the user has to guess the correct word from jumbled letters.
# The user has 3 chances to guess the word correctly.
import random

# open random words file 
f = open("random_words.txt","r")
a = f.read()
words = a.split(",")

# for random word
word = random.choice(words)

# for jumble word
jumble = "".join(random.sample(word,len(word)))

print('*' * 30)
print("WELCOME TO JUMBLE WORD GAME")
print('*' * 30)
chances = 3

while chances != 0:
    print("The jumbled word is:",jumble)
    guess = input("Guess the word: ")
    if guess.lower() == word.lower():
        print("Congratulations! You guessed the word correctly.")
        break
    else:
        chances -= 1
        print(f"Wrong guess! You have {chances} chances left.")
else:
    print(f"Sorry, you have no chances left. The word was '{word}'.")


