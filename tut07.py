# basic loop structures or iterative statements

# while loop

'''
syntax: 
    statement x
    while (condition):
        statement block
    statement y  
'''

# Example 1:
# i = 0
# while(i<100):
#     print(i, end=" ")
#     i = i+1

# Example 2
i = 0
sumN = 0
user_input = int(input("Enter a number: "))
while i <= user_input:
    sumN = sumN + i
    i = i + 1
print(f'The sum of fist {user_input} is', sumN)