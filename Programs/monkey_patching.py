"""MONKEY PATCHING"""

# def spam():
#     print('spam method')

# spam()
# print(spam)

# display = spam
# print(display)
# spam()
# display()

# 
# """
class Test:
    def __init__(self, x) -> None:
        self.x = x

    def get_data(self):
        print("taking the data from the sourc code")

    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()

y = Test(100)
y.get_data()
y.f1()
y.f2()

def new_get_data(self):
    print('taking the data from the TEST class')

Test.get_data = new_get_data

y.f1()
y.f2()
    
# """