"""
class A:
    def spam(self):
        print("spam")

class B:
    def spam(self):
        print("demo")

class C(A,B):
    def cool(self):
        print("spam and demo")

x= C()
# x.cool()
# x.spam()
print(C.__mro__)        # classname.__mro__ == method resolution order




# ====================

class class1:
    a = 10
    b = 'hello'
    print(f'value of a = {a}, b = {b}')

class class2:
    arr = [2,43,5,7]
    a = 'class2'
    print(f'value of arr = {arr} and a = {a}')
class class3(class2, class1):
    a = 10
    b = {1:'di', 2:'ctionary'}
    print(f'value of  a: {a} and b = {b}')

x= class3()
print(class3.__mro__)        # classname.__mro__ == method resolution order

# NESTED CLASS

class Test:
    def A(self):
        print("A class")

    class Sample:
        def B(self):
            print("Sample class")
        
        class Demo:
            def C(self):
                print('C class')

t = Test()
s = t.Sample()
d = s.Demo()

t.A()
s.B()
d.C()

# hw: use constructor and constructor overloading in above program
"""

# python is dynamic type of language so method overloading is not possible 100%
# but partially using default parameters


# need attention