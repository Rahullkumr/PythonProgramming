"""
5. wap to search for character in a given string and return corresponding index
string="coding part is done"
"""
string="coding part is done"
print(string)
def find_my_index(str,find_me):
    l = []
    for index,element in enumerate(str):
        if element == find_me:
            l.append((element,index))
    return l
print(find_my_index(string, 'i'))