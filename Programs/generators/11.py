# wap to generate a list if it is individual data type reverse it else keep it as it is

a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]

def generate():
    l2 = []
    for i in a:
        if isinstance(i, (int, float, complex, bool)):
           yield str(i)[::-1]
        else:
           yield i
    # yield l2
  
out = generate()
print(next(out))