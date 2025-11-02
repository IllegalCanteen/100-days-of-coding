from silent_auction_logo import logo
print(logo)
auction_info={}
bids=[]
while True:
    name=input("What is your name: ")
    price=int(input("What is your bid price: "))
    auction_info[name]=price
    rebid=input("Are there any other people left to bid y/n ")
    if rebid =="n":
        highest_bid=0
        winner=""
        for bidder in auction_info:
            bid_price=auction_info[bidder]
            if bid_price>highest_bid:
                highest_bid=bid_price
                winner=bidder
        print(f"The winner is {winner} with a bid of ${bid_price}")
        break

    elif rebid == "y":
        print("\n"*1000)
    else:
        print("Invalid input,ending auction try again")