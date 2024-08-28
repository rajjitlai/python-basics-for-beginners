# Exercise 04 - Check the user's input is Palindrome or not

# using a function (like a switch case)

# string reverse
'''
userInput = input("Enter a word to be checked: ")
reverseWord = userInput[::-1]
# print(reverseWord)
if userInput == reverseWord:
    print("Palindrome")
else:
    print("Not palindrome")
'''

def isPalindrome():
    print("Checking using isPalindrome")
    userInput = input("Enter a word to be checked: ")
    reverseWord = userInput[::-1]
    # reverseWord = ''.join(reversed(userInput)) # built in reversed function
    print(f"The reverse of {userInput} is {reverseWord}")
    if userInput == reverseWord:
        print(f"{userInput} is Palindrome")
    else:
        print(f"{userInput} is not Palindrome")

# using array indexing
def checking(word):
    checkWord = word.lower()
    left_index = 0
    right_index = len(checkWord) - 1

    while left_index < right_index:
        if checkWord[left_index] != checkWord[right_index]:
            return False
        left_index += 1
        right_index -= 1

    return True

def checkIsPalindrome():
    print("Checking using checkIsPalindrome")
    word = input("Enter a word to be checked: ")
    if checking(word):
        print(f"{word} is Palindrome")
    else:
        print(f"{word} is not Palindrome")

# main function
def main():
    print("PALINDROME CHECKER")
    while True:
        print("1. Check using reverse")
        print("2. Check using indexing")
        print("3. Exit")

        userChoice = input("Enter your choice (1-3): ")
        if(userChoice == "1"):
            isPalindrome()
        elif(userChoice == "2"):
            checkIsPalindrome()
        elif(userChoice == "3"):
            break
        else:
            print("Invalid option. Please select another option from 1 to 3!")

if __name__ == "__main__":
    main()

