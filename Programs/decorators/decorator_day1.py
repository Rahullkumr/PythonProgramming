#               DECORATORS OR META PROGRAMMING

"""
types of decorator:
    1. inbuilt  ===> eg: @staticmethod
    2. user defined
"""

# =========================================
# wap to implement: before executing main fn wait for 5 sec
# DELAY DECORATOR

"""
import time
def outer(func):
    def inner(*args, **kwargs):
        print("waiting 5 sec")
        time.sleep(5)
        func(*args, **kwargs)
    return inner

@outer
def main_fn():
    print("main function")

main_fn()
"""

# ===========================================
# ADDITION OPERATION

"""
def outer(func):
    def inner(a,b):
        print("addition operation")
        func(a,b)
        print('addition operation comopleted')

    return inner

@outer
def add(a,b):
    print(a+b)

add(5,7)
"""

# ===========================================
# Use single decorator to wait for 5 secs before executing given 3 fns

"""
import time
def outer(func):
    def inner(a,b,op_name):
        print(f"{op_name} operation")
        func(a,b,op_name)
        print("waintin 5 sec")
        time.sleep(5)
    return inner

@outer
def add(a,b,op_name):
    print(a+b)

@outer
def sub(a,b,op_name):
    print(a+b)

@outer
def mul(a,b,op_name):
    print(a+b)


add(5,7,'addition')
add(50,7,'substraction')
add(34,98,'multiplication')
"""

# ======================================
# Wap to find EXECUTION TIME of a program

"""
import time 
def outer(func):
    def inner(a,b):
        start_time = time.time()
        func(a,b)
        end_time = time.time()
        print('Execution time: ', end_time - start_time)

    return inner

@outer
def add(a,b):
    time.sleep(2)     # WITHOUT THIS IT'S GIVING 0.0 SEC
    print(a+b)

add(5,7)
"""

# ==============================================
# Before execution of main fn, print main fn name

"""
def outer(func):
    def inner(a,b):
        print("addition operation")
        print(f'Function name is: {func.__name__}')
        func(a,b)

    return inner

@outer
def add(a,b):
    print(a+b)

add(5,7)
"""

# =======================================
# Use multiple decorators before executing the main function

"""
def outer1(func):
    def inner():
        print("pyspider")
        func()
    return inner

def outer2(func):
    def inner():
        print("qspider")
        func()
    return inner

@outer1
@outer2
def add():
    print("welcome to python session")

add()
"""

# =================================
# decorator which prints the name of the called fn along with if the no is even or odd

"""
def print_name(func):
    def inner(no):
        print(f'Function name is: {func.__name__}')
        func(no)
    return inner

@print_name
def check_even_odd(no):
    print(f'{no} is even') if no%2==0 else print(f'{no} is odd')

check_even_odd(77)
check_even_odd(10)
"""

# =================================
# decorator to return only +ve output from any substraction

def outer(func):
    def inner(a,b):
        res = func(a,b)
        return abs(res)
    return inner 

@outer 
def pos_output(a,b):
    return a-b 

print(pos_output(1,3))