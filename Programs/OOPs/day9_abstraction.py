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

# ================================================

from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def deposit(self, amt):
        pass

    @abstractmethod
    def withdrawal(self, w_amt):
        pass

class Atm(Bank):
    def __init__(self, bank_name, bal):
        self.bank_name = bank_name
        self.bal = bal

    def balance(self):
        print(f"Your current Balance is : {self.bal}")

    def deposit(self, amt):
        print(f'Deposited balance is: {amt}')
        self.bal += amt
    
    def withdrawal(self, w_amt):
        self.bal -= w_amt
        print(f'Withdrawal amount is : {w_amt}')

    
print("WELCOME TO OUR BANKING SYSTEM")
a = Atm('Alpha', 5000)
print(f'Bank name is : {a.bank_name}')
print(f'Balance is : {a.bal}')
a.deposit(1000)
a.balance()
a.withdrawal(50)
a.balance()



# hw: book ticket
# ticket food no of members, theater name, movie 

# constructor and methods



# need attention