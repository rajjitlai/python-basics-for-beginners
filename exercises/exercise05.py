# Word Counter

def userInputCounter():
    userInput = input("Please write a sentence about yourself: ")
    
    words_split = userInput.split() # remove the white space
    # words_num = len(userInput) # but it will also include white space
    words_num = len(words_split)
    print(f"The number of words in your input is: {words_num}")

def fileContentCounter(file_name):
    try:
        with open (file_name, 'r') as file:
            file_content = file.read()

        file_words_split = file_content.split()
        file_words_num  = len(file_words_split)

        print(f"The number of words in your file is: {file_words_num}")

    except FileNotFoundError:
        print(f"The file {file_name} cannot be found")

# userInputCounter()

# fileContentCounter('to-be-counted.txt') # this will give errors, file path must be added
fileContentCounter("D:\\Programming\\python\\exercises\\exercise04.py")