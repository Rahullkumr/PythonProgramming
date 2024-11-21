#            """PARAMETERIZED DECORATOR""" 


# structure
""" 
def outer_most(parameter):
    def outer(func):
        def inner(*a, **k):
            stmt
            func(*a, *k)
        return inner 
    return outer

@outer_most(parameters)
def main_fn():
    statement

main_fn()
"""

# examples
"""
import time
def outer_most(n, waiting_time):
    def outer(func):
        def inner(*a, **k):
            print(n)
            time.sleep(waiting_time)
            func(*a, **k)
        return inner
    return outer

@outer_most('Addition operation',1)
def add(a,b):
    print(f'{a} + {b} = {a+b}')

@outer_most('Subtraction operation',2)
def sub(a,b):
    print(f'{a} - {b} = {a-b}')

@outer_most('Multiplication operation',3)
def mul(a,b):
    print(f'{a} * {b} = {a*b}')

@outer_most('Division operation',4)
def div(a,b):
    print(f'{a} / {b} = {a/b}')

add(5,10)
sub(20,3)
mul(2,5)
div(100,3)
"""


# waDF to check the role of a person if role is admin, print username and pwd;
# if employee, print access denied; if not both print invalid role
def outer_most(r):
    def outer(func):
        def inner(*a, **k):
            if r == 'admin':
                print('access granted')
                func(*a, **k)
            elif r == 'employee':
                print('access denied')
            else:
                print('invalid role')

        return inner

    return outer


# @outer_most('employee')
@outer_most('admin')
# @outer_most('someone')
def checking():
    uname = 'Rahul'
    pwd = '1234aswd'
    print(f'username: {uname} and password: {pwd}')


checking()
