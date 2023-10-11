# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 08:59:11 2023

@author: riley.barrett
"""

print("Blackjack:")
print("Blackjack payout is 3.2")
print("Enter 'x' for bet to exit")

starting_money=float(input("Starting Money\t\t\n\n"))


while True:
    bet_amount = input("bet_amount\t\t\n\n")
    if (bet_amount) == 'x':
        break
    else:
        bwpl =input("Win\t\t\t")
        if (bwpl=="b"):
            starting_money += float(bet_amount) * 1.5
            print(starting_money)
        elif (bwpl=="w"):
            starting_money += float(bet_amount) 
            print(starting_money)
        elif (bwpl=="p"):
            print(starting_money)
        elif (bwpl=="l"):
            starting_money -= float(bet_amount) 
            print(starting_money)
print("byee!")