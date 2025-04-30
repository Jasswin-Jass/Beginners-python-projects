def find_hightest_bidder(bidding_dictionary):
    winner=""
    highest_bid = 0

    for bidder in bidding_dictionary :
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    """ The above code can be done like this :
    winner = max(bidding_dictionary)
    print("The winner is",winner,"with the bidding amount of", bidding_dictionary[winner])"""

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_hightest_bidder(bids)
    elif should_continue == "yes":
        print("\n " * 50)
    else:
        continue_bidding = False
        find_hightest_bidder(bids)