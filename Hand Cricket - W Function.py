# Odd or even game

import random

# functions 

def errorcheck(l,t):

    while(True):
        i = input(t)
        if i.isdigit() and int(i) in l:
            return int(i)
        elif i.lower() in l:
            return i.lower()
        else:
            print('Invalid input')
            continue 
    
def plays (bowl, strike, bating):
    global score_ai, score_player

    if bowl == strike:
        print("OUT!!")

        if bating == 1:
            print("Your Score is :", score_player)
        else:
            print("Ai Score is :", score_ai)
        return False
    else:
        if bating == 1:
            score_player += strike
            print("Player score :", score_player)
        else:
            score_ai += strike
            print("Ai score :", score_ai)
        return True



while (True) :
    
    print("THIS IS A HAND CRICKET GAME")
    print("run = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
    StartOrStop = input("Enter start or stop:")
    print(end='\n')

    # Game elements

    run = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    toss = ("odd", "even")
    play = ("bat", "bowl")
    score_player = 0
    score_ai = 0

    #Toss

    if StartOrStop == "start":

        odd_eve = errorcheck(toss,"Enter Odd or Even :") # Asking odd or even
        player_toss = errorcheck(run,"Throw:")
        ai_toss = random.randint(0, 10)
        ai_bat_bowl = random.choice(play)


        if (ai_toss + player_toss) % 2 == 0 :
            print("Ai throw:",ai_toss)

            if odd_eve == "even":
                bat_bowl = errorcheck(play,"You win, choose to bat or bowl:")
            else:
                print("You lost, Ai choose to:", ai_bat_bowl)

                if ai_bat_bowl == "bat":
                    bat_bowl = "bowl"
                else:
                    bat_bowl = "bat"
        else:
            print("Ai throw:", ai_toss)

            if odd_eve == "odd" :
                bat_bowl = errorcheck(play,"You win, choose to bat or bowl:")

            else:
                print("You lost, Ai choose to:", ai_bat_bowl)

                if ai_bat_bowl == "bat":
                    bat_bowl = "bowl"
                else:
                    bat_bowl = "bat"

        # Game starts 

        print ("The Game starts now",'\n')

        if bat_bowl == "bat":
            print("You are Batting")

            while(1):
                
                strike1 = errorcheck(run,"Strike:")
                bowl2 = random.randint(0, 10)
                print("AI throw:", bowl2)
                if not plays(bowl2, strike1, 1):
                    break
            
            print("You are Bowling")

            while(1):
                bowl1 = errorcheck(run,"Throw:")
                strike2 = random.randint(0, 10)
                print("AI strike:", strike2)
                if not plays(bowl1, strike2, 2):
                    break
                if score_ai > score_player:
                    print("Ai score:",score_ai)
                    print("Ai WINS!!)")
                    break
            if score_ai == score_player:
                print("Match Draw!")
            elif score_ai < score_player:
                print("You WON!!")

        else:
            print("You are Bowling")

            while(1):
                bowl1 = errorcheck(run,"Throw:")
                strike2 = random.randint(0, 10)
                print("AI strike:", strike2)
                if not plays(bowl1, strike2, 2):
                    break

            print("You are Batting")

            while(1):

                strike1 = errorcheck(run,"Strike:")
                bowl2 = random.randint(0, 10)
                print("AI throw:", bowl2)
                if not plays(bowl2, strike1, 1):
                    break
                if score_player > score_ai:
                    print("Your score:",score_player)
                    print("YOU WIN!!)")
                    break

            if score_player == score_ai:
                print("Match Draw!")
            elif score_player < score_ai:
                print("Ai WON!!")

        print("---------------Match ended---------------",'\n')

    else:
        break