# 5. WAP to print all numeric values in a list

l = ['apple', 123, 'google', '45.6','yahoo', [1,2,3],True, (1,3,7), 6+3j]

for element in l:
    if isinstance(element, (int, float, complex, bool)):
        print(element)