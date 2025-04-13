# Odd or even game

while(True):
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

    # Toss

    import random

    if StartOrStop == "start":

        # Asking Odd or Even
        while (True):

            oddeve = input("Enter odd or even:")

            if oddeve in toss:
                break
            else:
                print("Invalid choice")
                continue

        # Throwing Toss
        while (True):

            player_toss = int(input("Throw:"))

            if player_toss in run:
                break
            else:
                print("Invalid choice")
                continue

        ai_toss = random.randint(0, 10)  # AI thrwing Toss
        ai_batbowl = random.choice(play)  # AI choice of play

        if (ai_toss + player_toss) % 2 == 0:

            print("AI throw:", ai_toss)

            if oddeve == "even":

                while (True):

                    batbowl = input("You Win, choose to Bat or Bowl:")

                    if batbowl in play:
                        break
                    else:
                        print("Invalid choice")
                        continue

            else:
                print("You lost, AI choose to:", ai_batbowl)

                if ai_batbowl == "bat":
                    batbowl = "bowl"
                else:
                    batbowl = "bat"

        else:
            print("AI throw:", ai_toss)
            if oddeve == "odd":

                while (True):
                    batbowl = input("You Win, choose to Bat or Bowl:")

                    if batbowl in play:
                        break
                    else:
                        print("Invalid choice")
                        continue

            else:
                print("You lost, AI choose to:", ai_batbowl)

                if ai_batbowl == "bat":
                    batbowl = "bowl"
                else:
                    batbowl = "bat"

        # The Game Starts

        print("The Game Starts Now")

        if batbowl == "bat":

            print("You  are Batting")
            while (True):
                bowl2 = random.randint(0, 10)

                while (True):
                    strike1 = int(input("Strike:"))

                    if strike1 in run:
                        break
                    else:
                        print("Invalid choice")
                        continue

                if bowl2 == strike1:
                    print("AI throw:", bowl2)
                    print("OUT")
                    print("Your Score is :", score_player)
                    break
                elif strike1 in range(0, 11):
                    print("AI throw:", bowl2)
                    score_player += strike1
                    print("Player score :", score_player)
                    continue
                elif strike1 == 0:
                    print("AI throw:", bowl2)
                    score_player += bowl2
                    print("Player score :", score_player)
                else:
                    print("Invalid choice")
                    continue

            print("You are Bowling")
            while (True):
                strike2 = random.randint(0, 10)

                while (True):
                    bowl1 = int(input("Throw:"))

                    if bowl1 in run:
                        break
                    else:
                        print("Invalid choice")
                        continue

                if bowl1 == strike2:
                    print("AI strike:", strike2)
                    print("AI IS OUT")
                    print("AI Score is :", score_ai)
                    break
                elif bowl1 in range(0, 11):
                    print("AI strike:", strike2)
                    score_ai += strike2
                    print("AI score :", score_ai)
                elif strike1 == 0:
                    print("AI strike:", strike2)
                    score_ai += bowl1
                    print("AI score :", score_ai)
                else:
                    print("Invalid choice")
                    continue

                if score_ai > score_player:
                    break


        else:

            print("You are Bowling")
            while (True):
                strike2 = random.randint(0, 10)

                while (True):
                    bowl1 = int(input("Throw:"))

                    if bowl1 in run:
                        break
                    else:
                        print("Invalid choice")
                        continue

                if bowl1 == strike2:
                    print("AI strike:", strike2)
                    print("AI IS OUT")
                    print("AI Score is :", score_ai)
                    break
                elif strike2 in range(0, 11):
                    print("AI strike:", strike2)
                    score_ai += strike2
                    print("AI score :", score_ai)
                    continue
                elif strike2 == 0:
                    print("AI strike:", strike2)
                    score_ai += bowl1
                    print("AI score :", score_ai)
                else:
                    print("Invalid choice")
                    continue

            print("You  are Batting")
            while (True):
                print("You  are Batting")
                bowl2 = random.randint(0, 10)

                while (True):
                    strike1 = int(input("Strike:"))

                    if strike1 in run:
                        break
                    else:
                        print("Invalid choice")
                        continue

                if bowl2 == strike1:
                    print("AI throw:", bowl2)
                    print("OUT")
                    print("Your Score is :", score_player)
                    break
                elif strike1 in range(0, 11):
                    print("AI throw:", bowl2)
                    score_player += strike1
                    print("Player score :", score_player)
                elif strike1 == 0:
                    print("AI throw:", bowl2)
                    score_player += bowl2
                    print("Player score :", score_player)
                else:
                    print("Invalid choice")
                    continue

                if score_player > score_ai:
                    break

        # Conclusion of the Game

        if score_player > score_ai:
            print("YOU WIN :)")
        elif score_player < score_ai:
            print("YOU LOST")
        else:
            print("MATCH DRAW")

        print("---------------Match ended---------------")

    elif StartOrStop == "stop":
        break
