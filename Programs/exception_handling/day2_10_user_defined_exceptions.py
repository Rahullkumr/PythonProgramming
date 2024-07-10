
# 10 USER DEFINED ERRORS

# 1.
class PaliError(Exception):
    pass
def check(a):
    if a == a[::-1]:
        print('palindrome')
    else:
        raise PaliError
# check("madam")
check('hello')



# 2.
class NegativeDivisionError(Exception):
    pass
def divide(a, b):
    if b < 0:
        raise NegativeDivisionError("Cannot divide by a negative number")
    return a / b
try:
    result = divide(10, -2)
except NegativeDivisionError as e:
    print("Error:", e)



# 3.
class InvalidAgeError(Exception):
    pass
def set_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age provided")
    return age
try:
    age = set_age(-5)
except InvalidAgeError as e:
    print("Error:", e)



# 4.
class InvalidOperationError(Exception):
    pass
def operate(a, b, operation):
    if operation not in ['+', '-', '*', '/']:
        raise InvalidOperationError("Invalid operation provided")
    return eval(f"{a} {operation} {b}")
try:
    result = operate(10, 5, '%')
except InvalidOperationError as e:
    print("Error:", e)



# 5.
class EmptyListError(Exception):
    pass
def get_first_element(my_list):
    if not my_list:
        raise EmptyListError("The list is empty")
    return my_list[0]
try:
    element = get_first_element([])
except EmptyListError as e:
    print("Error:", e)



# 6.
class InvalidScoreError(Exception):
    pass
def set_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100")
    return score
try:
    score = set_score(105)
except InvalidScoreError as e:
    print("Error:", e)



# 7.
class UnauthorizedAccessError(Exception):
    pass
def access_resource(user):
    authorized_users = ['admin', 'manager']
    if user not in authorized_users:
        raise UnauthorizedAccessError("User is not authorized")
    return "Access granted"
try:
    access = access_resource('guest')
except UnauthorizedAccessError as e:
    print("Error:", e)



# 8.
class InvalidEmailError(Exception):
    pass
def validate_email(email):
    if '@' not in email or '.' not in email:
        raise InvalidEmailError("Invalid email address")
    return email
try:
    email = validate_email("invalid-email")
except InvalidEmailError as e:
    print("Error:", e)



# 9.
class InvalidDateError(Exception):
    pass
def set_date(day, month, year):
    if month < 1 or month > 12 or day < 1 or day > 31:
        raise InvalidDateError("Invalid date provided")
    return f"{day}/{month}/{year}"
try:
    date = set_date(32, 13, 2021)
except InvalidDateError as e:
    print("Error:", e)



# 10.
class GeneratorFailedError(Exception):
    pass

def limited_generator(limit):
    count = 0
    while count < limit:
        yield count
        count += 1
    raise GeneratorExhaustedError("Generator has been exhausted")

# Using the generator
gen = limited_generator(3)

try:
    print(next(gen))  # Output: 0
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    print(next(gen))  # This will raise GeneratorExhaustedError
except GeneratorExhaustedError as e:
    print("Error:", e)
