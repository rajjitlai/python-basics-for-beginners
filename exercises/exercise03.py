# number guessing game

# i = 0
# while True:
#     if i < 100:
#         i = i + 1
#         print("Yes", end= '')
#         if i == 10:
#             break

# Basic
# while True:
#     userInput = int(input("Enter a number: "))

#     if userInput > 50:
#         print("Congrats, you have entered a number greater than 50\n")
#         break
#     else:
#         print("Try again\n")
#         continue

# level 2
# import random
# secretNumber = random.randint(1, 100)
# print("Welcome to the number guessing game:")
# while True:
#     userInput = int(input("Enter a number between 1 to 100: "))

#     if userInput == secretNumber:
#         print("Congrats, you have guessed the correct number. Well done!\n")
#         break
#     elif userInput > secretNumber:
#         print("Hint: Too high! Try a lower number.\n")
#     else:
#         print("Hint: Too low! Try a higher number.\n")

# level 3
import random
secretNumber = random.randint(1, 20)
attempts = 5
print("Welcome to the number guessing game:")
print(f"You have {attempts} attempts")
while attempts > 0:
    userInput = int(input("Enter a number between 1 to 20: "))
    if userInput == secretNumber:
        print("Congrats, you have guessed the correct number. Well done!\n")
        break
    elif userInput > secretNumber:
        print("Hint: Too high! Try a lower number.\n")
    else:
        print("Hint: Too low! Try a higher number.\n")

    # attempts = attempts - 1 
    attempts -= 1 
    print(f"You have {attempts} {'attempts' if attempts != 1 else 'attempt'} left")

if attempts == 0:
    print(f"Sorry, you've run out of attempts. The correct number was {secretNumber}. Better luck next time!\n")