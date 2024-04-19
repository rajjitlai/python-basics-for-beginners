# Introduction to Object Oriented Programming

# Classes and Objects

# Defining a class
# Syntax
'''
class className:
    statement_1
    statement_2
    .
    .
    .
    statement_n
    newvar = 100 # class member
    here, newvar is class variable and 100 is class methods
'''

# creating an instance or object
# objectName = className() # class instantiation

# accessing the members
# objectName.newvar

# Example
class Teacher:
    tName = "Rajjit"

subject = Teacher()
printVar = subject.tName

# print("RJ Coding Tips teaches python programming and it is taught by ", subject.tName)
print("RJ Coding Tips teaches python programming and it is taught by ", printVar)