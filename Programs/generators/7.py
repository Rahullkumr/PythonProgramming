# wap to generate only the string with odd length in given list

l=["alexa","siri","google","cortrena"]

def generate():
    l2 = []
    for i in l:
        if len(i) % 2 == 1:
            l2.append(i)
    yield l2
  
out = generate()
print(next(out))