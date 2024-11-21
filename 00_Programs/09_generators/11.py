# wap to generate a list if it is individual data type reverse it else keep it as it is

a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]

def generate():
    l2 = []
    for i in a:
        if isinstance(i, (int, float, complex, bool)):
           reversed_no = str(i)[::-1]
           yield reversed_no
        else:
           yield i
  
out = generate()
print(next(out))
print(next(out))
print(next(out))