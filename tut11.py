# Python Recursive functions and main function
'''
-> Recursive function: a function that calls itself
-> 2 parts: base case, Recursive case
'''
# factorial : 5! = 5 * 4 * 3 * 2 * 1 = 120
# 0! = 1! = 1
# recursive function to find the factorial 

# def factorial(n):
#     # base case
#     if n == 0 or n == 1:
#         return 1
#     # recursive case
#     else:
#         return n * factorial(n - 1)

# output = factorial(10)
# print("The factorial of 10 is: ", output)

# main functions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def mainFunc():
    num = int(input("Enter a number: "))
    output = factorial(num)
    print(f"The factorial of {num} is:", output)

# main part
if __name__ == "__main__":
    mainFunc()
