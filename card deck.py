# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:59:17 2023

@author: riley.barrett
"""

import random 
def header():
    print("\nBlackjack")
    print("blackjack payout is 3.2")
    print("enter x for bet amount")
    
    
def get_deck():
    deck=[]
    ranks=("ace","2","3","4","5","6","7","8","9","10",
           "jack","queen","king")
    suits=("clubs","diamonds","hearts","spades")
    for suit in suits:
     for rank in ranks:
        if rank == "ace":
            value= 11
        elif rank == "jack" or rank == "queen" or rank == "king":
            value = 10 
        else:
            value = int(rank)
            card = [rank,suit,value]
            deck.append(card)
            
    return deck

def shuffle(deck_cards):
    random.shuffle(deck_cards)
    
def deal_card(deck_cards):
    card = deck_cards.pop()
    return card 

def get_empty_hand():
    hand=[]
    return hand 

def add_card(hand,card):
    hand.append(card)

def get_points(hand):
    points = 0
    aces =   0
    for card in hand:
        points += card[2]
        if card[0] == "ace":
            aces += 1

    if aces > 0 and points > 21:
        points = points - (aces * 10)      
    if aces > 1and points <= 11:
        points += 10 
    return points 