# functions

# user-defined functions

# '''function definition'''
# def function_name():
#     pass
# '''function call'''
# function_name()
# print("this is a statement")

# parameter - variables to be used in the function
# def newFunc(x, y):
#     return x - y
# a = 10
# b = 5
# callFunc = newFunc(a, b)
# print("the value is", callFunc)

# def func():
#     for i in range(4):
#         print("Hello world")
# func()
'''
def newFuncs(x, y):
    return x * y

# newFuncs(5)  will give error because the argument and the parameter do not match
printValue = newFuncs(5, 10)
print(printValue)
'''
# default argument
# def display(name, course="BCA"):
#     print("Name:", name)
#     print("Course:", course)
# my_name = "Rajjit"
# display(my_name)

# lambda function
'''
syntax: lambda argument: expression
'''
# def sum(x, y):
#     print(x + y)
# sum(12, 8)

# sum2 = lambda x, y : x + y
# print(sum2(12, 12))

# Q. write a program to check whether two number are equal or not

def check(a, b):
    if(a == b):
        print("a and b are equal")
    elif (a > b):
        print("a is greater than b")
    else:
        print("a is lesser than b")

check(5, 12)
