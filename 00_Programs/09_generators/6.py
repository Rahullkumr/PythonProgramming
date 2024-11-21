# wap to generate a list; if it is individual data type: reverse it else return as it is


l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

def generate():
    l2 = []
    for i in l:
        if isinstance(i, (int, float, complex, bool)):
           l2.append(str(i)[::-1])
        else:
           l2.append(i)
    yield l2
  
out = generate()
print(next(out))