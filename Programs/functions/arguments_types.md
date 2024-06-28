<!-- def fn(parameter)
    pass
fn(argument) -->

1. positional arguments 
```py
def add(a,b):
    print(a+b)

add(1,2)
add(1,2,3,4,5,6)
```

2. variable positional args: *args(any name) return type ==> tupple
```py
def add(*args):
    print(args) # (1, 2, 3, 4, 5, 6)
add(1,2,3,4,5,6)
```

3. keyword arguments
```py
def add(x,y):
    print(x+y)
add(y=6, x=22)
```

4. variable keyword arguments: **kwargs; return type==> dictionary
```py
def disp(**kwargs):
    print(kwargs) # {'a': 4, 'b': 6, 'c': 11, 'd': 45}
disp(a=4,b=6,c=11,d=45)
```
5. combination of *args and **kwargs
```py
def combi(*args, **kwargs):
    print(args, kwargs) # 

combi(10, 22, 33, a=4,b=6,c=11,d='hello')
```

## positional always follows keyword argument

6. Positional only argument(/)
```py
def add(a,b,c,/,d):
    print(a+b+c+d)
add(1,2,3,4)
```

7. Keyword only argument(*)
```py
def add(*,a,b,c):
    print(a+b+c)
add(a=1,b=2,c=3) ✔
add(1,2,c=3) ❌❌
add(a=1, b=2, 99) ❌❌
```

8. combination of both(6 and 7)
<!-- * k baad keyword arguments pass krna jaruri hai -->
<!-- / k pehle positional hi chahiye -->
```py
def add(*,a,b,c):
    print(a+b+c)
add(a=1,b=2,c=3)
```

9. Default parameter
```py
def details(a=0, b=0, c=7):
    print(a*b*c)
details()
details(1)
details(1,2,3) # 1x2x3
```

################################################
