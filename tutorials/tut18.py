# Errors and Exception Handling in Python 

# Syntax errors
# print("hello world") # normal
# print("hello world"

# Indentation errors
# if True:
# print("hello world")

# NameError
# a = 56
# print(b)

# TypeError
# a = 56
# b = 'Hello'
# result = b + a
# print(result)

# ValueError
# number = int("abc")
# print(number)

# Exception Handle

# try-except
# try:
#     result= 10/0
# except ZeroDivisionError as newRes:
#     print(f'Error: {newRes}')

# print('the result is', result)

#  try-except (multiple)
# try:
#     value = int('abc')
# except ValueError as ve:
#     print(f'Error: {ve}')
# except ZeroDivisionError as res:
#     print(f'Error: {res}')

# try except else
# try:
#     result= 10/0
# except ZeroDivisionError as newRes:
#     print(f'Error: {newRes}')
# else:
#     print('the result is', result)

# finally
# try:
#     result= 10/5
# except ZeroDivisionError as newRes:
#     print(f'Error: {newRes}')
# finally:
#     print('the result is', result)
#     print('this finally will always execute')

# custom
# class customError(Exception):
#     pass

# try:
#     raise customError("This is a custom exception")
# except customError as e:
#     print(f'Custom error: {e}')

