# INHERITANCE
# 1. SINGLE INHERITANCE / SINGLE LEVEL INHERITANCE
# 2. MULTI LEVEL INHERITANCE
# 3. MULTIPLE INHERITANCE
# 4. HIERARCHICAL INHERITANCE
# 5. HYBRID INHERITANCE

"""
# MULTI LEVEL INHERITANCE
class Grandpa:
    name = "Rajesh Arora"
    def property(self):
        print('villa')
        print(dir(Grandpa))

class Dad(Grandpa):
    def antique(self):
        print('Antique watch')
        print(dir(Dad))

class Son(Dad):
    def vehicle(self):
        print('bike')
        print(dir(Son))

s = Son()
s.property()
s.antique()
s.vehicle()
print(s.name)

# 3. MULTIPLE INHERITANCE
class Father:
    f_gift = 'bike'
    def thing(self):
        print('Dad has a bike')

class Mother:
    m_gift = 'gold chain'
    def thing(self):
        print('Mom has a gold watch')

class Son(Father, Mother):
    def thing(self):
        print(f'Son has both property of mom and dad: {self.f_gift} and {self.m_gift}')

s = Son()
s.thing()

class Restaurent:
    def rest(self):
        print('restaurant')
class Del_boy:
    def db(self):
        print('delivery boy')

class Customer(Restaurent, Del_boy):
    def cust(self):
        print('customer')    
c = Customer()
c.rest()
c.db()
c.cust()


# HIERARCHICAL 
class RBI:
    sal = 12345
    def print_sal(self):
        print(self.sal)
class ICICI(RBI):
    def print_sal(self):
        print(self.sal)
class PO(RBI):
    def print_sal(self):
        print(self.sal)

i = ICICI()
po = PO()

print(i.sal)
print(po.sal)

# method chaining 
class Student:
    print("Method chaining example")
    def class1(self):
        print("Student class")
        
class Student2(Student):
    def class1(self):
        super().class1()
        print("Student2 class")

s = Student2()
s.class1()



# constructor chaining
class Hi:
    print("Constructor chaining example")
    def __init__(self):
        print("Hi class")

class Bye(Hi):
    def __init__(self):
        super().__init__()
        print("Bye class")

o = Bye()

# passing params

class Student:
    print("Constructor chaining example")
    def __init__(self):
        print("Hi class")

class Bye(S):
    def __init__(self):
        super().__init__()
        print("Bye class")

c = Clg(clg_name, clg_loc)

# =============================================

class Mobile:
    def __init__(self, update, calls):
        self.update = update
        self.calls = calls
    

class Whatsapp(Mobile):
    def __init__(self, communities, chat):
        super().__init__('3updates today', 'Manasi')
        self.comm= communities
        self.chat = chat

    def display(self):
        print(f'updates are: {self.update}, calls: {self.calls}')
        print(f'updates are: {self.comm}, calls: {self.chat}')
        

    

m = Whatsapp(['sports', 'entertainment'], 'with boss')
m.display()

class Student:
    def __init__(self, update, calls):
        self.update = update
        self.calls = calls
    def display(self):
        print(f'updates are: {self.update}, calls: {self.calls}')

class Clg(Student):
    def __init__(self, communities, chat):
        super().__init__('3updates today', 'Manasi')
        self.comm= communities
        self.chat = chat

    def display(self):
        print(f'updates are: {self.update}, calls: {self.calls}')
        print(f'communities are: {self.comm}, calls: {self.chat}')
        

    

m = Whatsapp(['sports', 'entertainment'], 'with boss')
m.display()
"""


# HYBRID INHERITANCE

class Father:
    item = 'car'
    def f(self):
        print("father's car")


class Mother:
    item = 'gold chain'
    def f(self):
        print("mother's gold chain")



class Son(Father):
    item = 'denim jacket'
    def s_fn(self):
        print("son jacket and father's car")

class Daughter(Father, Mother):
    item = 'iphone'
    def d_fn(self):
        print("daughter's iphone and mother's jewellery")

d = Daughter()
d.d_fn()

s = Son()
s.s_fn()


# need attention