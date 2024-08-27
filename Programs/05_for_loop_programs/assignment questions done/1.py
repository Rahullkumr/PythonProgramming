# 1.wap to Sum the numbers

s = 'Sony12India567pvt21ltd'
sum = 0
n = ''

for i in s:
    if i.isnumeric():
        sum += int(i)
print(f'Sum of digits is: {sum}')