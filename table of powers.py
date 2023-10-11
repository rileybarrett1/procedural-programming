# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:18:24 2023

@author: riley.barrett
"""

print("Table Of Powers")
prog = True


while prog:
    start_number=int(input("Start number: "))
    stop=int(input("Stop number: "))
    line= "="

    if start_number>stop:
        print("Start number must be greater then top number please try again")
        prog=False
    else: 
       print("number\t\tSquared\t\tCubed")
       print("{}\t\t{}\t\t{}".format(line*6,line*7,line*5))
    
    for number in range(start_number,stop +1):
            squared = number ** 2
            cubed = number ** 3
           
            print("{}\t\t\t{}\t\t{}\t\t".format(start_number,squared,cubed))
        
            stop=False