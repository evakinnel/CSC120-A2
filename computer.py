"""
Filename: computer.py
Description: stores the Computer class
Assignment: A2: Object-ification
Class: CSC120: Object-Oriented Programming
Author: Eva Kinnel
Date: 18 September 2022
"""

class Computer:
  '''
  The Computer has information about each individual computer: Item ID, Price, Year Made, and if OS is updated

  has the ability to alter attributes appropriately:
  designate an ID #, designate a price based on year, update OS if necessary
  '''

  # Attributes
  code: int = 1
  id: int = 1
  price: int = 0
  year_made: int = 0
  os: bool = 0
  
  # Constructor
  def __init__(self, id, price, year_made, os):
    self.__id = Computer.code
    Computer.code += 1   # increment id each time a new computer is created
    self.__price = price
    self.__year_made = year_made
    self.__os = os
    print(f"Year Made: {year_made} \nNew OS: {os}")
        
  # Methods 
  def updatePrice(self, amount):
    ''' 
    replaces old price with new price
    prints
    '''
    self.__price = amount
    # print(f"New Price: ${self.__price:.2f}.\n")
    # print(f"ID: {self.__id}")
    # print(f"Year Made: {self.__year_made}")
    # print(f"Price: ${self.__price}")
    return("")

  def updateOS(self):
    ''' 
    tells you that OS is up to date or updates it
    '''
    if self.__os == True:
      print("OS: Up to date")
    else:
      self.__os = True
      print("OS: Updating...\nOS: Updated")

    return("")

  def refurbish(self):
    '''
    asseses year made to decide how to update price
    calls updatePrice() and updateOS()
    prints new info
    '''
    if self.__year_made < 2000:
      print("DONATE")
      print(self.updatePrice(0))
    elif self.__year_made < 2012:
      print(self.updatePrice(250))
      print(self.updateOS())
    elif self.__year_made < 2018:
      print(self.updatePrice(550))
      print(self.updateOS())
    else:
      print(self.updatePrice(1000))
      print(self.updateOS())
    print(f"ID: {self.__id}")
    print(f"Year Made: {self.__year_made}")
    print(f"Price: ${self.__price}")
    print(f"New OS: {self.__os}\n")
    # computer = [self.__year_made, self.__price, self.__os]
    # print(computer)

  def getDetailsDict(self):
    '''
    returns a dictionary containing {year, price, os}
    '''
    computer = {'Year': {self.__year_made}, 'Price': {self.__price}, 'OS': {self.__os}}
    # print(computer)
    return(computer)

  def getID(self):
    '''
    returns the item id created in __init__
    '''
    ID = self.__id
    # print(ID)
    return(ID)
    
    

