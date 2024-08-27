# wap to return an iterator which is having square root of values present in the list

import math
l=[25,36,49,81,9,16] 

def s_root():
    l2 = []
    for i in l:
        l2.append(math.sqrt(i))

    yield l2

output = s_root()
print(next(output))