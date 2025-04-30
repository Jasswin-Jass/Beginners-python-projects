import random

game_elements = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def game():
    user_cards = []

    dealer_cards = []

    user_cards.append(random.choice(game_elements))

    user_cards.append(random.choice(game_elements))

    dealer_cards.append(random.choice(game_elements))

    dealer_cards.append(random.choice(game_elements))

    take_card = True

    while take_card:

        user_sum = sum(user_cards)

        dealer_sum = sum(dealer_cards)

        while 11 in user_cards and sum(user_cards) > 21:
            i = user_cards.index(11)
            user_cards[i] = 1

        while 11 in dealer_cards and sum(dealer_cards) > 21:
            i = dealer_cards.index(11)
            dealer_cards[i] = 1

        print(f"Your cards are: {user_cards}", f"And your sum is {user_sum}")

        print(f"Dealer's first card is: {dealer_cards[0]}")

        if user_sum == 21 and dealer_sum != 21:
            print("You win!!")
            play_again = input("Enter 'y' if you want to play again else type 'n': ")

            if play_again == 'y':
                game()
            return

        elif dealer_sum == 21:
            print(f"Dealer's cards are: {dealer_cards}", f"And their sum is: {dealer_sum}")
            print("You lose!")
            return

        elif user_sum > 21:
            print("You lose!")
            return

        next_card = input("Enter 'y' if you want another card or enter 'n' if you don't: ")

        if next_card == 'y':
            user_cards.append(random.choice(game_elements))
            continue
        else:
            take_card = False

    while dealer_sum < 17:
        dealer_cards.append(random.choice(game_elements))
        dealer_sum = sum(dealer_cards)
        while 11 in dealer_cards and sum(dealer_cards) > 21:
            i = dealer_cards.index(11)
            dealer_cards[i] = 1

    print(f"Dealer's cards are: {dealer_cards}", f"And their sum is: {dealer_sum}")

    if dealer_sum > 21:
        print("You win!")

    elif dealer_sum > user_sum:
        print("You lose!")

    elif user_sum > dealer_sum:
        print("You win!")

    elif user_sum == dealer_sum:
        print("Draw")

    play_again = input("Enter 'y' if you want to play again else type 'n': ")

    if play_again == 'y':
        game()


game()
