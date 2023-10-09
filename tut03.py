# Python Indentation
def sample():
    new = "Hello" # indented with 4 spaces
    print(new)
sample()

Python Keywords
continue = "Coding" # will give error
print(yield)

Python Operators
1 Arithmetic Operators - +, -, *, /, %, //, **
num1 = 20
num2 = 3
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1//num2)
print(num1**num2)


Assignment Operators - =, +=, -=, *=, /=, //=, %=, **=, &=, >>=, <<=
num1 = 20
num1 += 3
print(num1)

Comparison operators - ==, !=, <, >, <=, >=
num1 = 20
num2 = 5
print(num1<=num2) 

Logical Operators - and, or, not
num1 = 20
num2 = 5
print(num1<30 and num2>3) # and means both conditions must be true for getting True
print(num1==30 or num2>3) # or means either one must be true to get True
print(not(num1!=num2))

Identity Operators - is, is not
num1 = ['a', 'b']
num2 = ['a', 'b']
num3 = num1
print(num1 is num3)
print(num1 is num2)
print(num1 is not num3)
print(num1 is not num2)

Membership operator - in, not in 
num1 = [1, 2, 3, 4, 5]
print(5 not in num1)

Bitwise operator - &, |, >>, <<, ~, ^
num1 = 5
num2 = 6
print(num1>>2)

Operator Precedence

Test - solve 5*4+4-5/6(3**2)**3