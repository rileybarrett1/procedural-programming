# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 08:14:02 2023

@author: riley.barrett
"""

print(25 * "=")
print("Shipping calculater")
print(25 * "=")
while_running=True
shipping_cost=0
total_cost=0
while True:
    cost_of_items= float(input("\ncost of items ordered:"))
    if cost_of_items >= 0:        
        if cost_of_items < 30:
            shipping_cost=5.95
        elif  cost_of_items >=  30 and cost_of_items < 50:
            shipping_cost=7.95
        elif cost_of_items >= 50 and cost_of_items < 75:
            shipping_cost=9.95
     
        else:
            shipping_cost=0
       
        print("shipping cost:  {:.2f}\t\t\t\t".format(shipping_cost))
        print("total cost:     {:.2f}\t\t\t\t".format(shipping_cost+cost_of_items))
        cont= input("continue  (y/n):\t")
        print(25 * "=")
        if cont != "y":
            break
    else:
        print("please neter a positive number")
        print("byee!")
