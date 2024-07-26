# DEFAULT CONSTRUCTOR

"""

class Animal:
    def animal(self):
        print('welcome to zoo')
a = Animal()
a.animal()

# NON PARAMETERISED CONSTRUCTOR (without parameters)


# class Student:
#     def __init__(self):
#         print()

class Bank:
    def __init__(self):
        acc_no = 12346
        cname = 'Sindhu'
        ifsc = 'sbiin00004567'
        branch = 'Pune'
        add = 'Pyspider'
        print(f'my acount no is {acc_no} and customer name is {cname} and bank ifsc code is {ifsc}')
        print(f'branch name is {branch} customer address is {add}')

b = Bank()
b1 = Bank()

# PARAMETERISED CONSTRUCTOR (with parameters)
class Bank1:
    def __init__(self, acc_no, cname, bank_name,ifsc, branch, add):
        acc_no = acc_no
        cname = cname
        ifsc = bank_name
        branch = branch
        add = add
        print(f'my acount no is {acc_no} and customer name is {cname} and bank ifsc code is {ifsc}')
        print(f'branch name is {branch} customer address is {add}')

x = Bank1("Rekha", 'icici', 'icici000', 1234567, 'pune', 'qspider')
x1 = Bank1("Madhu", 'sbi', 'sbi0087000', 9876543, 'Delhi', 'Jspider')

class Bank:
    def __init__(self) -> None:
        self.bal = 0.0

    def deposit(self, amt):
        self.bal = amt
        print(f'total bal: {self.bal}')

x = Bank()
print(x.bal)

# modification through clasname ==> it will not affect and will not throw error

Bank.bal = 500

# modification through object
x.bal = 500
x.deposit(1000)
"""









# ===============

class Bank:

    def m(self):
        x = ''
        self.mv = 5

    def n(self):
        self.nv = self.mv
        print(self.nv)

o = Bank()
o.n()


















# =======================================
"""
with and without using parameters
class Amazon:
    def __init__(self, pdt_name, price, total_count, loc):
        self. pdt_name = pdt_name
        self.price = price
        self. total_count = total_count
        self. loc = loc

    def display_details(self):
        print(f'product name is {self.pdt_name}, price: {self.price}, total count: {self.total_count} and Delivery address: {self.loc}')
        

a = Amazon('rocket', 12345, 5, 'Pune')
a.display_details()
"""

# multiple constructors METHOD OVERLOADING (PARTIALLY) USING DEFAULT VARIABLES

# constructor overloading using default variables
# class Test:
#     def __init__(self, a):
#         print(a)

#     def __init__(self, a,b):
#         print(a,b)

#     # def __init__(self, a,b,c):
#     #     print(a,b,c)

#   the magic happens here

#     # def __init__(self, a=0,b=0,c=0):
#     #     print(a,b,c)

# t = Test(1,2,3)
"""
# method overloading using default variables
class Test:
    

    def add(self, a):
        print(a)

    def add(self, a,b):
        print(a+b)

    def add(self, a,b,c):
        print(a+b+c)

#   the magic happens here
    def add(self, a=0,b=0,c=0):
        print(a+b+c)


t = Test()
# t.add(1,2,3)
# t.add(11)
t.add(1,29)
"""
# =====================

# variable length arguments
# class Car:
#     def __init__(self, cname, color, *args):
#         print(f'car name: {cname} and color: {color}')
#         print(f'extra info: {args}')

# c = Car('Lamborghini', 'black', 1000000)



# need attention