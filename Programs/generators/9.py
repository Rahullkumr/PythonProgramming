# wap to return a list; if words is of even length reverse it

l=["hello","world","python","apple","google","walmart"]

def generate():
    l2 = []
    for i in l:
        if len(i) % 2 == 0:
            l2.append(i[::-1])
    yield l2
  
out = generate()
print(next(out))