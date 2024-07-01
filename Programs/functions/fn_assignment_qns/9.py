# 9.wap to find square,cube,square root and cube root of a number

import math 
def operations(num):
    print(f'Square: {num*num}')
    print(f'Cube: {num*num*num}')
    print(f'Square Root: {math.sqrt(num)}')
    print(f'Cube Root: {math.pow(num,1/3)}')

num = int(input("Enter a no: "))
operations(num)