# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:30:31 2023

@author: riley.barrett
"""

print("\ntip Calculater")
cost_of_meal=float(input("Cost Of Meal:"))
while True:
    print("15%")
    print("\ntip amount:  {.2f}".format(cost_of_meal/15))
    print("\ntotal amount:  {.2f}".format(cost_of_meal*0.15))
    print("20%")
    print("\ntip amount:  {.2f}".format(cost_of_meal/20))
    print("\nTotal amount:  {.2f}".format(cost_of_meal*0.20))
    print("25%")
    print("\ntip amount:  {.2f}".format(cost_of_meal/25))
    print("\ntTotal Amount:  {.2f}".format(cost_of_meal*0.25))
    break