# wap to return an iterator having tuples of word and its len pair and typecast into dictionary


l=["instagram","facebook","whatsapp","meta","oracle"]

def gen():
    d = {}
    for i in l:
        d[i] = (i, len(i))

    yield d

output = gen()
print(next(output))