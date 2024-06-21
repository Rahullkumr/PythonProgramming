# 21. wap to create a dictionary with words and its length pair and ends with vowel

s="Today is Tuesday and attending python session"

d = dict()

for i in s.split():
    if i.endswith(('a', 'e', 'i', 'o', 'u')):
        d[i] = len(i)

print(d)