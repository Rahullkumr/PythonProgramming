# wap to generate only numeric values in given list


l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

def generate():
    l2 = []
    for i in l:
       if isinstance(i, (int, float)):
           l2.append(i)
    yield l2
  
out = generate()
print(next(out))