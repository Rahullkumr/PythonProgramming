"""METHODS:"""

# 1. instance method:
    # any method that is accepting object address as parameter is called IM
# 2. class method
# 3. static method





"""INSTANCE METHODS"""
# class Test:
#     def spam(self):
#         print("spam method")
#         print("\033[31m", f"address of self: {self}", "\033[0m")

# t = Test()
# print("\033[31m", f"address of object t: {t}", "\033[0m")
 
# # calling through the object
# t.spam()

# # calling through the class name
# Test.spam(t)    # mandatory to pass obj





# class Emp:
#     def salary(self):
#         amount = 1000       # local variable
#         print(f'Salary is : {amount}')
# e = Emp()
# e.salary()
# Emp.salary(e)





# class Palindrome:
#     def pali(self, name):
#         return (name,True) if name==name[::-1] else (name,False)
    
# d = Palindrome()
# print(d.pali("madam"))
# print(d.pali("hello"))





"""
# ACCESSING AND MODIFYING USING OBJECT

class Amazon:
    pname = 'watch'
    price = 1000
    cname = 'Sunny'
    cadd = 'Pune'


    def order(self):
        print(f'Product Name: {self.pname}, price: {self.price}, customer name: {self.cname}')

    def delivery_address(self):
        print(f'Delivery address is : {self.cadd}')

a = Amazon()
a.cname = "RAHUL"
# ACCESSING AND MODIFYING USING OBJECT
a.order()
a.delivery_address()





# ACCESSING AND MODIFYING USING CLASS 
class Amazon:
    pname = 'watch'
    price = 1000
    cname = 'Sunny'
    cadd = 'Pune'
    def order(self):
        print(f'Product Name: {self.pname}, price: {self.price}, customer name: {self.cname}')

    def delivery_address(self):
        print(f'Delivery address is : {self.cadd}')

a = Amazon()
Amazon.cname = "PRITAM"
# ACCESSING USING CLASS NAME
Amazon.order(a)
Amazon.delivery_address(a)





# =========================

class Qsp:
    rating = "1*"
    sub = "SQL"

    def display_mock_rating(self):
        print(f"ur mock rating is {self.rating} in {self.sub} in subject")

q = Qsp()
q.display_mock_rating()
#   ur mock rating is 1* in SQL in subject

Qsp.sub = "Apti"
Qsp.rating = "1"
q.display_mock_rating()
#   ur mock rating is 1 in Apti in subject

q.sub = "MANUAL"
q.rating = "2"
q.display_mock_rating()
#  ur mock rating is 2 in MANUL in subject

Qsp.sub = "Python"
Qsp.rating = "3"
q.display_mock_rating()
# ur mock rating is 2 in MANUL in subject
"""





# WAP to accept list from the user when the method is called,first index element in the list, if it is str then reverse it then replace in same position and return, else if int then ask for user to add an element in the list and return the updated list, else reverse the list and return 
"""
class Operation:
    def check(self, l):
        if isinstance(l[1], str):
            l[1] = l[1][::-1]
            return l
        elif isinstance(l[1], int):
            element = input('enter an element in list:' )
            l.append(element)
            return l
        else:
            return l[::-1]
        

o = Operation()
print(o.check(['234', 'I am string', 'helloooj', 33, [1, 3], 1]))
print(o.check(['234', 87, 'helloooj', 33, [1, 3], 1]))
print(o.check(['234', ('I am', 'tuple'), 'helloooj', 33, 1]))
"""

