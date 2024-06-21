# 14.wap using below list and get the below output


l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']

# o/p:-->{'flower': ['sun', 'Lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}

d = {}
category_list = []

for i in l:
  category = i.split()[1] 
  
  if category not in d.keys():
    for j in l:
      if j.split()[1] ==  category:
        if j.split()[0] not in category_list:
          category_list.append(j.split()[0])
    
    d[category] = category_list
    category_list = []

print(d)