# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:40:18 2023

@author: riley.barrett
"""



def title():
    print("sales data")
    print("enter sales data")

def program():
           sales = "y"
           input_print=1
           total_sales=0
           while sales.lower() == "y":
               amount=float(input("amount:\t\t\t:"))
               year=int(input("year\t\t\t:"))
               month=int(input("month 1-12\t\t\t:"))
               day=int(input("day 1-31:"))
    
        
           if month in range(1,4):
                quarter_1="quarter 1"
           elif month in range(4,7):
                quarter_2='quarter 2'
           elif month in range(7,10):
                 quarter_3="quarter 3"
    
        
           else:
            quarter="quarter 4"
            print("\n{}.\t\t\t\t{}--{}--{}\t\t{}\t\t${:.1f})".format(input_print, year,month,day,quarter,amount))
            total_sales=amount
            input_print=+1
            sales_loop = input("enter more sales? (y/n)")
            def end():            
                print("total sales")
                print(20*"=")
                print("${:.1f}".format(total_sales))
                print("\nbyeeee")
                
def main():
    