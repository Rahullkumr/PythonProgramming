# 10.wap to group fruit name and country pair only if a fruit is even length
from itertools import zip_longest
d={"apple":45,"mango":67,"cherry":90,"berry":23}

p={"India":"Kashmir","America":"us","UK":"Toronto","Africa":"Uganda"}

for i in zip(d,p):
    if len(i[0]) % 2 == 0:
        print(i)