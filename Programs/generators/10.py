# wap to generate the first letter of the word as key and words starting with letter as value

s="python is a programming language and programming is part of life"


# output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]

def generate():
    d = {}
    words = s.split()
    for i in words:
        key = i[0]
        if key not in d:
            d[key] = [i]
        else:
            d[key] += [i]
    yield d 
out = generate()
print(next(out))
