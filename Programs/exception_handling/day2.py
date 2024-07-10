# Exception Handling
"""
a = [1,2,3,4]

try:
    a[5]

except IndexError:
    print('index error')

except ZeroDivisionError:
    print('zero error')

except TypeError:
    print('type error')

finally:
    print("always enters here whether there is error or not")

# method 2

try:
    a[5]

except (IndexError, ZeroDivisionError, TypeError):
    print("handle the error")

finally:
    print("always enters here whether there is error or not")
"""
# Nested try and except

# a = [1,2,3,4]
# try:
#     a[2]
#     try:
#         a[7]
#     except:
#         print('error')
# except:
#     print("no error")

# example

# try:
#     a = open('hello.py', 'r')
#     try:
#         a[7]
#     except:
#         print('error')
# except:
#     print("error opening file")

# USING else BLOCK
# try:
#     a = open('readme.md', 'r')
# except:
#     print("error opening file")
# else:
#     print('there is no error else block executes')
# finally:
#     print("finally always executes")

# user defined error

# WAP to print positive if it is > 0 else RAISE METROERROR

"""
syntax:
class user_defined_exception_name(Exception/BaseException):
    pass
"""

# class MetroError(Exception):
#     pass

# def check(a):
#     if a > 0:
#         print('positive')
#     else:
#         raise MetroError
    
# # check(7)
# check(-7)

# if not palindrome raise error

class PaliError(Exception):
    print("error")

def check(a):
    if a == a[::-1]:
        print('palindrome')
    else:
        raise PaliError
    
# check("madam")
check('hello')

# DGREED (DATA ANALYST)

# hw: 10 user defined exceptions