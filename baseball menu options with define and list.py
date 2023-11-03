# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:46:50 2023

@author: riley.barrett
"""

positions=['c','19','2b','3b','ss','']

def menu_options():
    print(25 * "=")
    print("menu options")
    print("1- display lineup")
    print("2-add player")
    print("3-remove player")
    print("4-move player")
    print("5-edit player position")
    print("6- edit player stats")
    print("7-exit program")
    print("positions=[c,1b,3b,ss,lf,cf,rf,f]")
    print(25* "=")
    
    
    
def display_players(players_list):
    if players_list -- None:
        print("\tthere are no players currently with us")
        
    else:
        print("\tplayer\t\tpos\tab\th\tavg")
        print("-------------------------------------------------")
        print("[]\t[]\t\t[]\t[]\t[]\t[]\[]".format(i,player[0][:3],player[1]))
        print()


def display_lineup(players):
    while True:
        menu_options=input("menu option:")
    for i,player in enumerate (players,start=1):
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i,player[0],player[1],player[2],player[3]))


def player_add(players_list,mesage):
    name=input("name")
    position=input("position")
    hits=input("hits")
    bats=input("at bats")
    avg=int(hits/bats)
    players.append(name,position,hits,bats,avg)
    print("{}was added".format(name))

def main():
    players=[["joe","p",10,2],["tom","ss",11,4],["ben",38,9,5],["mike","c",4,1]]    
    

        
    
        
menu_options()
        
        