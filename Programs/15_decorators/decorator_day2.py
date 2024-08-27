# 1.write a decorator function that prints "HELLO EVERYONE" message before execute any function
"""
def decorator_fn(func):
    def wrapper_fn():
        print("HELLO EVERYONE")
        func()
    return wrapper_fn

@decorator_fn
def any_fn():
    pass
any_fn()
"""



# 2.write a decorator function to print main function name before executing any decorator function
"""
def decorator_fn(func):
    def wrapper_fn():
        print(func.__name__)
        func()
    return wrapper_fn

@decorator_fn
def main_fn():
    pass
main_fn()
"""



# 3.write a decorator which inputs 5 seconds of delay before executing any decorator function
"""
import time 
def decorator_fn(func):
    def wrapper_fn(sec):
        time.sleep(sec)
        func(sec)
    return wrapper_fn

@decorator_fn
def main_fn(sec):
    print('Executed after 5 sec delay')
main_fn(5)
"""



# 4.write a decorator function to calculate the execution time of any function
"""
import time 
def decorator_fn(func):
    def wrapper_fn():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time-1} sec to execute')
    return wrapper_fn

@decorator_fn
def main_fn():
    time.sleep(1)
    print('find execution time')
main_fn()
"""



# 5.wadf to check if the 1st arguments is lesser than 2nd argument; if true then swap them and perform division without modifying the original function
"""
def decorator_fn(func):
    def wrapper_fn(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return wrapper_fn

@decorator_fn
def div(a,b):
    return a/b
print(div(3,9))
print(div(9,3))
"""



# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after performing print the message "addition operation is done"

# o/p--->i am doing addition operation"
#        value
#      "addition operation is done

"""
def decorator_fn(func):
    def wrapper_fn(a,b):
        print("i am doing addition operation")
        print(f'sum = {func(a,b)}')
        print("addition operation is done")
    return wrapper_fn

@decorator_fn
def addition(a,b):
    return a+b
addition(1,2)
"""



# 7.create a decorator to return only positive output from any subtraction
"""
print('Always positive difference')
def decorator_fn(func):
    def wrapper_fn(a,b):
        print(f'subtraction of {a} and {b} = {abs(func(a,b))}')
    return wrapper_fn

@decorator_fn
def always_positive_difference(a,b):
    return a-b
always_positive_difference(1,3)
always_positive_difference(9,3)
"""



# 8.create a decorator which counts the number of function calls
"""
count = 0
def decorator_fn(func):
    def wrapper_fn():
        global count
        count += 1
    return wrapper_fn

@decorator_fn
def any_fn():
    pass
any_fn()
any_fn()
any_fn()
print(f'any_fn() is called {count} times')
"""



# 9.wap to sum the positional arguments and get the length of the keywords arguments 
"""
def decorator_fn(func):
    def wrapper_fn(*args,**kwargs):
        print(f'sum of positional args i.e {args} = {sum(args)}')
        print(f'Length of keyword args i.e {kwargs} = {len(kwargs)}')
    return wrapper_fn

@decorator_fn
def any_fn(*args,**kwargs):
    pass
any_fn(1,2,3,4,5, city = 'Pune', pin_code = 411052) 
""" 



# 10.write a decorator function to print the type of datatype before performing the action
"""
def decorator_fn(func):
    def wrapper_fn(data):
        print(type(data))
        func(data)
    return wrapper_fn

@decorator_fn
def any_fn(data):
    print(data)
any_fn(6)
any_fn(6.7)
any_fn('hello')
any_fn(3+2j)
any_fn([3,4])
"""



# 11.write a decorator to perform following:  if given number A>B then perform multiplication in decorator function else cube it in decorator
"""
def decorator_fn(func):
    def wrapper_fn(a,b):
        print(f'{a} * {b} = {a*b}') if a>b else print(f'cube of {a} : {a**3} and cube of {b} : {b**3}')
    return wrapper_fn

@decorator_fn
def any_fn(a,b):
    pass
any_fn(11,3)
any_fn(3,10)
"""



# 12. create a decorator which prints name of called function and counts the function calls
"""
count = 0
def decorator_fn(func):
    def wrapper_fn():
        global count
        count += 1
        print(f'{func.__name__} is called: {count} times')
    return wrapper_fn

@decorator_fn
def main_fn():
    pass
main_fn()
main_fn()
main_fn()
"""



# 13.create a decorator which prints name of called 08_functions and checks the number is even or odd
"""
def decorator_fn(func):
    def wrapper_fn(a):
        print(f'{func.__name__}')
        print(f'{a} is even') if a%2==0 else print(f'{a} is odd')
    return wrapper_fn

@decorator_fn
def main_hun_function(n):
    pass
main_hun_function(50)
"""



# 14.create a decorator which delays its execution as per user input
"""
import time 
def decorator_fn(func):
    def wrapper_fn(secs):
        time.sleep(secs)
        func()
    return wrapper_fn

@decorator_fn
def wait_till_infinity():
    print('still waiting')
wait_till_infinity(2)       # user input => 2sec
"""



# 15. write a multilevel decorator to log some message
"""
import time
def assign_time(func):
    def wrapper_fn(r):
        local_time = time.ctime()
        print(local_time)
        func(r)
    return wrapper_fn

def save_user_name(func):
    def wrapper_fn(r):
        print("User name: ",r)
        func(r)
    return wrapper_fn

@assign_time
@save_user_name
def its_me_logger(r):
    print('secret message logged')
its_me_logger('James Bond')
""" 



# 16.write a multilevel decorator to accept username and register number of the employee 
# """ 
def check_username(func):
    def wrapper_fn(uname, m_no):
        if isinstance(uname,str) and uname.isalpha():
            print('valid username')
        else:
            raise ValueError('username should be string and alphabets only')
        func(uname, m_no)
    return wrapper_fn


def check_mobile(func):
    def wrapper_fn(uname, m_no):
        def is_valid_mno(m_no):
            import re 
            return True if re.match(r'^[789]\d{9}$', str(m_no)) else False 
            
        if is_valid_mno(m_no):
            print('valid mobile number')
        else:
            raise ValueError('Invalid mobile number. It must be a 10-digit number starting with 7, 8, or 9 only')
        func(uname, m_no)
    return wrapper_fn


@check_username
@check_mobile
def registeration(uname, m_no):
    print(f'Registration successful for user {uname} with mobile number {m_no}')

registeration('Rahul', 9711223311)        
# registeration('R@hul', 9711223311)        # invalid username
# registeration('Rahul', 1711223311)        # invalid mobile number
# """



# 17.WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR 3 SECONDS AND DISPLAY EMAIL ADDRESS , DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER
"""
import time 
def decorator_fn(func):
    def wrapper_fn(name, address, ph):
        time.sleep(3)
        print(f'Name : {name}')
        time.sleep(3)
        print(f'Address : {address}')
        time.sleep(3)
        print(f'Phone : {ph}')
        func(name, address, ph)
    return wrapper_fn

@decorator_fn
def late_latif_fn(name, address, ph):
    print('Details displayed successfully')
late_latif_fn('Rahul', 'Moon South Pole', 9007007007) 
"""



# 18 using 3 15_decorators show me one example
"""
def decorator1(func):
    def wrapper_fn():
        print("accessing decorator1")
        func()
    return wrapper_fn

def decorator2(func):
    def wrapper_fn():
        print("accessing decorator2")
        func()
    return wrapper_fn

def decorator3(func):
    def wrapper_fn():
        print("accessing decorator3")
        func()
    return wrapper_fn

@decorator1
@decorator2
@decorator3
def any_fn():
    print('printing main fn')
any_fn()
"""

# SUCCESSFULLY DONE 