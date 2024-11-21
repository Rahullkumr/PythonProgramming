# 8.wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number
def add_sub(n1,n2,n3):
    summ = n1 + n2
    return n3 - summ

n1 = int(input("enter first no: "))
n2 = int(input("enter second no: "))
n3 = int(input("enter third no: "))

print(add_sub(n1,n2,n3))