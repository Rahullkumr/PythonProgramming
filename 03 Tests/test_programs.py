import re
#31
"""
import re
s = "The python class starts at 7:00 am in the morning and 19:00 pm in the evening."
time_pattern = r'\d{1,2}:\d{2} [aApP][mM]'
matches = re.findall(time_pattern, s)
m = []
for i,v in enumerate(matches):
    hr = int(v.split(':')[0])
    if hr >= 12:
        hr = hr - 12
        m.insert(i,f'{hr}:{v.split(':')[1]}')
    else:
        m.insert(i, v)
print(', '.join(m))
"""





#32
files = ['demo.txt', 'loops.py', 'for_loop.py', 'data.xlx', 'pres.ppt', 'spam.txt', 'document.doc', 'spam.py', 'python.xlx', 'methods.ppt', 'string.ppt', 'lst.doc']

# normal way
d = {}
v = []
for file in files:
    value, key = file.split('.')
    if value not in v:
        v.append(value)

    # print(v)
    d[key] = v

print(d)




#33


#34


#35


#36


#37


#38


#39


#40


