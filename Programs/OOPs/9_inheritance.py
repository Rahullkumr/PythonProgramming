# ABSTRACTION
# abstract class and methods

"""
from abc import ABC, abstractmethod
class Pyspider(ABC):        # parent class
    @abstractmethod
    def sub1(self):     # declaration
        pass
    
    @abstractmethod
    def sub2(self):
        pass

    @abstractmethod
    def sub3(self):
        pass

class Qspider(Pyspider):        # child class
    def sub1(self):
        print('First subject is Python')

    def sub2(self):
        print('Second Subject is sql')

    def sub3(self):
        print('webtech')

q = Qspider()
q.sub1()
q.sub2()
q.sub3()
"""

from abc import ABC, abstractmethod
class Bank(ABC):

    @abstractmethod
    def balance(self):
        pass 

    @abstractmethod
    def withdrawal(self, amount):
        pass 

    @abstractmethod
    def deposit(self, amount):
        pass 

class Atm(Bank):
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def 

# hw: book ticket
ticket food no of members, theater name, movie 

construcor and methods



# need attention