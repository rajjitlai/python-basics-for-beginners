# Password generator

# use random for generating random elements
# use string for generating letters, digits, punctuation 

import random
import string

# using a function
def generatePassword(len):
    char =  string.ascii_letters + string.digits + string.punctuation
    
    # minimum length check
    if len < 4: 
        raise ValueError("Password cannot be less than 4 characters!")
    # maximum length check
    elif len > 30:
        raise ValueError("Password cannot be more than 30 characters!")
    # else:
    #     raise ValueError("Something bad happened! Please try again!")
    
    password = ''.join(random.choice(char) for i in range(len)) 
    return password

userInput = int(input("Enter the password length: "))
callFunc = generatePassword(userInput)
print(callFunc)