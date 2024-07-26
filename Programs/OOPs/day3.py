# CLASS METHODS

# in case of class method, we don't need to pass obj when calling, using class name

# class methods share hote hn ya nahi among objects?

# what is the use of class methods and why should we use it?
"""
class Election:
    date = '17/07/2024'

    @classmethod
    def Area1(cls):
        first = cls()
        first.date = '31/12/2099'
        print(f'my area election date: {first.date}')

    @classmethod
    def Area2(cls):
        x = cls()       # x = Election()
        x.date = '15/07/2024'
        print(f'my area election date: {x.date}')
        # print(f'my area election date: {cls.date}')

    @classmethod
    def Area3(cls):
        third = cls()
        third.date = '10/03/1988'
        print(f'my area election date: {third.date}')
        # print(f'my area election date: {cls.date}')

e = Election()
# Election.date = '20/07/2024'        # mdification in the class
e.Area1()
e.Area2()
e.Area3()
"""


"""STATIC METHODS"""

# NO MODIFICATION POSSIBLE IN STATIC METHODS BECAUSE THERE IS NO SELF OR CLS 


# class Gym:
#     trademill = '25km'

#     @classmethod
#     def men(cls):
#         print(f'total weight of trademill: {cls.trademill}')
    
#     @staticmethod
#     def women(o):
#         print(f'total weight of trademill: {o.trademill}')

# g = Gym()
# # g.women(g)

# # modification using class name
# # Gym.trademill = '333km'
# # g.men()
# # g.women(g)
# # Gym.men()
# # Gym.women(g)

# # modification using object g
# g.trademill = '0km'
# g.men()
# g.women(g)
# Gym.men()
# Gym.women(g)








class Test:
    name="abc"
    @classmethod
    def demo(cls):
        print(f'my name is {s.name}')


    @staticmethod
    def spam(t):
        print(f'my name is {t.name}')



s=Test()
print(id(Test))
print(id(Test.demo))
print(id(Test.spam))

prabhu = 'hello'
Test.name="xyz"
s.demo()
s.spam(prabhu)



# need attention