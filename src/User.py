# Importing necessary libraries
import random

# Defining the User class
class User:
    def __init__(self, name, balance=0,owed=0):
        self.name = name
        self.balance = balance
        self.owed = owed

    def update_balance(self, amount,owed):
        self.balance += amount
        self.owed -= owed
        
    

