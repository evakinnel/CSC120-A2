"""
Filename: main.py
Description: Contains the ResaleShop class *not used in main because I could not get it to work* 
Assignment: A2: Object-ification
Class: CSC120: Object-Oriented Programming
Author: Eva Kinnel
Date: 18 September 2022
"""

from typing import Dict, Union, Optional
from computer import *

class ResaleShop:
  '''
  the Resale Shop is an inventory of all the computers owned by the shop

  can add (buy) and remove (sell) computers
  '''

  # Attributes 
  inventory : Dict[int, Dict[str, Union[int, int, bool]]] = {}

  # Constructor
  def __init__(self, inventory):
    self.__inventory = inventory 

  # Methods

  ########  cannot figure out how to use the returns from Computer    #######
    
  def buy(self, computer):
    '''
    adds a computer to inventory
    '''
    self.__inventory[Computer.__id] = Computer.getDetailsDict()
    print(self.__inventory)
    
  def sell(self): 
  '''    
  removes computer from inventory
  '''   
    self.__inventory.pop(Computer.__id)
  
    