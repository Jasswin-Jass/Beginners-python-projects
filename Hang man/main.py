import random

import art

import words

word = random.choice(words.wordlist)
correct = []

a = ""
for i in word:
    a += "_"
print(a)

life = 6

while life:
    guess = input("Guess a letter: ").lower()

    if guess in correct:
        print("You already guessed this letter")

    disp = ""

    for i in word:
        if i == guess:
            disp += i
            correct.append(i)
        elif i in correct:
            disp += i
        else:
            disp += '_'

    if guess not in word:
        life -= 1

    print(disp)

    if disp == word:
        print("**************** YOU WIN! ****************")
        break

    print(f"You have {life} life balance ")

    print(art.hangmanimg[life], "\n")

if disp != word:
    print(f"The word was {word}")
    print("**************** YOU LOSE! ****************")
