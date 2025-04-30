#Stone paper scissor game

elements = ["stone", "paper", "scissor"]
print("This is a stone paper scissor Game.This game will continue until you enter the word 'stop'.")
print(end='\n')

while(True):
    import random

    ai_choice = random.choice(elements)
    player_choice = input("Enter stone or paper or scissor:")

    if ai_choice == "stone" and player_choice == "stone":
        print("AI choice is", ai_choice)
        print("Its a DRAW")
        print(end='\n')
        continue
    elif ai_choice == "stone" and player_choice == "paper":
        print("AI choice is", ai_choice)
        print("YOU WIN :)")
        print(end='\n')
    elif ai_choice == "stone" and player_choice == "scissor":
        print("AI choice is", ai_choice)
        print("YOU LOST")
        print(end='\n')
    elif ai_choice == "paper" and player_choice == "stone":
        print("AI choice is", ai_choice)
        print("YOU LOST")
        print(end='\n')
    elif ai_choice == "paper" and player_choice == "paper":
        print("AI choice is", ai_choice)
        print("Its a DRAW")
        print(end='\n')
        continue
    elif ai_choice == "paper" and player_choice == "scissor":
        print("AI choice is", ai_choice)
        print("YOU WIN")
        print(end='\n')
    elif ai_choice == "scissor" and player_choice == "stone":
        print("AI choice is", ai_choice)
        print("you win")
        print(end='\n')
    elif ai_choice == "scissor" and player_choice == "paper":
        print("AI choice is", ai_choice)
        print("YOU LOST")
        print(end='\n')
    elif ai_choice == "scissor" and player_choice == "scissor":
        print("AI choice is", ai_choice)
        print("Its a DRAW")
        print(end='\n')
        continue
    elif player_choice == "stop":
        break
    else:
        print("Invalid choice")
        print(end='\n')
        continue



