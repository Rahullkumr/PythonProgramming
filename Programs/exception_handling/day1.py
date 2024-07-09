a = 10
b = 0

# default block; when we don't know what kind error it is
try:
    print(a/b)

except:
    print('handling the error')

# specific block; when we know the specific error name
try:
    print(a/b)

except ZeroDivisionError:
    print("handling Zero division error")

# generic except block; have to use alias 

s = 'hello'
try:
    s.append('hi')
except BaseException as msg:
    print("what error is there using BaseException: ",msg)


print()
try:
    s.append('hi')
except Exception as msg:
    print("what error is there Exception: ",msg)
