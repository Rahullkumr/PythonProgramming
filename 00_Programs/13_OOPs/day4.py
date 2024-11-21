# CONSTRUCTOR

# Accessing constructor:
    # 1. using object
    # 2. using class name
"""
class Student:
    def __init__(self):
        print("I am constructor")

x = Student()       #automatically it will call constructor during its creation
Student.__init__(x)     # manually we are calling constructor using class name
"""

# ==================

# class Test:
#     def __init__(self):
#         print('Hi')

#     def spam(self):
#         print('spam')

# t = Test()
# t.spam()

# Test.__init__(t)
# Test.spam(t)

# ==============
class Exam:
    def __init__(self):
        print('Hi')

    def __int__(self):
        print('spam')

t = Exam()



# need attention