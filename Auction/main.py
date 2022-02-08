
import os

def find_highest_bidder(bidding_record):
    highest_price = 0
    for name, price in bidding_record.items():
        if price >= highest_price:
            highest_price = price
            highest_bidder = name
    
    return highest_bidder, highest_price


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bidding_finished = False
bids = {}
while not bidding_finished:
    name = input('What is your name?: ')
    price = int(input('What is your bid?: $'))
    bids[name] = price
    is_continue = input('Are there any other bidders? Type \'yes or no\'. \n')
    
    if is_continue == 'no':
        bidding_finished = True
        highest_bidder, highest_price = find_highest_bidder(bids)
        print(f'Highest bidder : {highest_bidder}\nHighest price : {highest_price}')
    elif is_continue == 'yes':
        os.system('clear')
        




