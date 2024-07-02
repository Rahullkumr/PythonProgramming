# wap to create a list of numbers if number are even square it else cube it

l=[2,3,4,5,6,7]
def generate():
    l2 = []
    for i in l:
        if i % 2 == 0:
            l2.append(i**2)
        else:
            l2.append(i**3)
    yield l2
  
out = generate()
print(next(out))