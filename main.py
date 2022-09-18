"""
Filename: main.py
Description: Main code to run computer store
Assignment: A2: Object-ification
Class: CSC120: Object-Oriented Programming
Author: Eva Kinnel
Date: 18 September 2022
"""

# Import a few useful containers from the typing module
from typing import Dict, Union, Optional
from computer import *
# from oo_resale_shop import *


def main():
  #info about a bought computer: id (automatically incremented, price(does not matter what price it starts with), year made, and new os (True/!True))
  
  comp1: Computer = Computer(id, 10, 2020, False)
  comp1.refurbish()
  # comp1.getDetailsDict() #only works with .refurbish() running too
  # comp1.getID()

  print("\n-----------------\n")
  
  comp2: Computer = Computer(id, 0, 2017, True)
  comp2.refurbish()  
  # comp2.getDetailsDict() #only works with .refurbish() running too
  # comp2.getID()

  print("\n-----------------\n")

  comp3: Computer = Computer(id, 0, 2011, True)
  comp3.refurbish()  
  # comp3.getDetailsDict() #only works with .refurbish() running too
  # comp3.getID()

  print("\n-----------------\n")
  
  inventory = {}
  # inventory[comp1.getID()] = comp1.getDetailsDict()
  inventory[comp1.getID()] = comp1.getDetailsDict() #add computer 1
  # print(inventory)
  inventory[comp2.getID()] = comp2.getDetailsDict() #add computer 2
  # print(inventory)
  inventory[comp3.getID()] = comp3.getDetailsDict() #add computer 3
  print(inventory)

  inventory.pop(comp2.getID()) #remove computer 2
  print(inventory)

  print("\n-----------------\n")


  comp4: Computer = Computer(id, 30, 2002, 0)
  comp4.refurbish()  

  inventory[comp4.getID()] = comp4.getDetailsDict() #add computer 4
  print(inventory)


 ########## What I wanted to be able to do: ###########
  
  # inventory: ResaleShop = ResaleShop({})
  # print(inventory.buy(comp1))
  # print(inventory.sell(comp1))
  
  


if __name__ == "__main__": 
    main()