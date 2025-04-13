# this is a guess game

print("This is a Guess Game")
print("""\nThe rules are: 
    1. You need to guess the number between 1 to 10
    2. You have 3 chances
    3. the game will be played 10 times""")

import random
x = 0

for k in range(1,11):
   num = random.randint(1, 10)
   print("Number ",k)
   for n in range(1,4):
        gnum = int(input("Guess the number : "))
        if num == gnum:
            print("Correct answer")
            x += 1
            break
        else:
            print("Wrong answer")
print("Your score is : {}/10".format(x))