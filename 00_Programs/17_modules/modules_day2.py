import random
import math
import calendar as c

print("==========================")
print("RANDOM MODULE")
print("==========================")

# '''
print('random decimal value between 0-1: ', random.random())
print('random integer in range [2, 5]: ', random.randint(2, 5))  # [2,5]
print('random integer in range [2, 5): ', random.randrange(2, 5))  # [2,5)
print('random decimal value between [3,7]: ', random.uniform(3, 7))  # [3,7] decimal form
print('Choose a random element from [1, 2, 3, 4, 5]: ', random.choice([1, 2, 3, 4, 5]))
# '''


# wap to generate 4 digit basic otp

# """
def create_otp():
    otp = ''
    for _ in range(4):
        otp = otp + str(random.randint(0, 9))
    print('Four digit basic otp = ', otp)


create_otp()
# """


# wap to generate otp containing 2 lower case, 2 upper case and 2 numbers

# """
def generate_otp():
    otp = ''
    for _ in range(2):
        otp = otp + str(random.randint(0, 9))

    for _ in range(2):
        otp = otp + chr(random.randint(65, 90))

    for _ in range(2):
        otp = otp + chr(random.randint(97, 122))

    print('Six digit otp = ', otp)


generate_otp()
# """


print("==========================")
print("MATH MODULE")
print("==========================")

# """
print('always positive value using math.fabs: ', math.fabs(-23))
print('Floor value of 3.1234: ', math.floor(3.1234))
print('Ceil value of 2.345: ', math.ceil(2.345))
print('Sum of [1,2,3,4,5]: ', math.fsum([1, 2, 3, 4, 5]))
print('2 raised to the power 4 (2^4): ', math.pow(2, 4))
print('cube root of 27: ', math.cbrt(27))
print('square root of 121: ', math.sqrt(121))
print('100 modulus 6: ', math.fmod(100, 6))
print('value of PIE: ', math.pi)
# """


print("==========================")
print("CALENDAR MODULE")
print("==========================")

# """
print("let's print calendar of 2024")
print(c.calendar(2024))

print("let's print August month of 2024: ")
print(c.month(2024, 8))

print("let's print full month names of 2024 in a list: ")
print(list(c.month_name))

print()
print("name of weekdays only first character: ", c.weekheader(1))
print("name of weekdays first two characters: ", c.weekheader(2))
print("name of weekdays first three character: ", c.weekheader(3))
print("name of weekdays first 20 character: 😒", c.weekheader(20))
c.setfirstweekday(6)    # 0:mon, 1:tue, 2:wed, 3:thu, 4:fri, 5:sat, 6:sun
print("name of weekdays only first character: ", c.weekheader(1))
print("name of weekdays first two characters: ", c.weekheader(2))
print("name of weekdays first three character: ", c.weekheader(3))
print("name of weekdays first 20 character: 😒", c.weekheader(20))
# """
