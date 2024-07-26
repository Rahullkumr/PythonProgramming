# COMPOSITION (HAS-A RELATIONSHIP)

"""
# without using constructor
class Test:
    name = 'python'
    def spam(self):
        print('spam method')

class Sample:
    def demo(self):
        print('demo method')
        a = Test()
        print(a.name)
        a.spam()

s = Sample()
s.demo()


# with using constructor without parameters

class Car:
    loc = 'Pune'
    def __init__(self):
        print('Car class constructor')

    def m1(self):
        print('car class m1 method')

class Car2:
    def __init__(self):
        print('car2 class constructor ')
        self.y = Car()
        print(self.y.loc)
        self.y.m1()
c = Car2()




class Student:
    def __init__(self, rollno, name, section):
        self.rollno = rollno
        self.name = name
        self.section = section

    def display_stu_details(self):
        print(f'Student roll no: {self.rollno}\n Student name: {self.name}\n Section: {self.section}')
        print()


class Employee:
    def __init__(self, empno, ename, sal):
        self.empno = empno
        self.ename = ename
        self.sal = sal

        self.s = Student(rollno=195, name='Mr Padhaku', section='A')
        self.s.display_stu_details()
                        # or
        self.S = Student(102, 'Bhola Ram', 'B')
        self.S.display_stu_details()

    def display_emp_details(self):
        print(f'Employee no: {self.empno}\n Student ename: {self.ename}\n Salary: {self.sal}')

e = Employee('emp24-389', 'Raj Mistri', 3000)
e.display_emp_details()
"""




# INHERITANCE
# 1. SINGLE INHERITANCE / SINGLE LEVEL INHERITANCE
# 2. MULTI LEVEL INHERITANCE


# need attention