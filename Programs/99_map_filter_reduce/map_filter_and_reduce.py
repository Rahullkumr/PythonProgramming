# """MAP()"""

"""
map() is an inbuilt function, it will pass an element one by one from the iterable to the function.
(it can be a lambda function, normal function, inbuilt function)

syntax:
-------
map(function_name , iterable 1, iterable2, iterable3, ...)

*The output of map will be in object format, to get the correct output we should type caste or use for loop.
*Whenever we are writing "function_name" in a map we should not write function_name with brackets.
*when we are passing multiple iterables, the length of all iterables should be same else data will be lost.
*it will pass the same indices of multiple iterable to multiple arguments specified in the function.
*no. of iterables should be the same as no. of arguments specified in function.
*The function passed should not have parentheses when used inside map()

# example
a = [1,2,3,4,5]
def square_me(n):
    return n*n
print(list(map(square_me,a)))  # [1,4,9,16,25]
"""





# """FILTER()"""

"""
filter() is an inbuilt function which is used to filter elements from an iterable based on a condition provided by a function.

syntax:
-------
filter(function_name, iterable)

*it will accept only 2 arguments i.e "function and iterable".
*The function used with filter() must return a boolean value (True or False).
*It will pass each element of the iterable to the function.
*If the function returns True, the element is included in the final output; otherwise, it is filtered out.
*Similar to map(), the output of filter() is an object. To get the actual output, you can type cast it or use for loop.
The function passed should not have parentheses when used inside filter().

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
def is_even(n):
    return n % 2 == 0

# Filter even numbers
result = filter(is_even, numbers)
print(list(result))  # Output: [2, 4, 6, 8]
"""





# """FILTER()"""

"""
The reduce() function, unlike map() and filter(), is not a built-in function; it is available in the functools module. It applies a rolling computation to pairs of elements in an iterable and reduces them to a single cumulative value.

Syntax:
-------
from functools import reduce
reduce(function_name, iterable)

*The function used in reduce() must take two arguments, i.e "function_name and iterable"
*It starts with the first two elements and reduces the iterable until only one value remains.
*You can optionally provide an initializer (a third argument) for reduce().

# Example
from functools import reduce
numbers = [1, 2, 3, 4, 5]


def multiply(x, y):
    return x * y


# Multiply all numbers together
result = reduce(multiply, numbers)
print(result)  # 120
"""
