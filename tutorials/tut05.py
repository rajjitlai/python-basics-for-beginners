# Python Strings and Its Method

myString = "Learning Python from RJ Coding Tips"

# 1. Accessing the characters in Python Strings
# firstChar = myString[0]
# secondChar = myString[1]
# eightChar = myString[8]
# lastChar = myString[-1]
# print(firstChar)
# print(lastChar)
# print(secondChar)
# print(eightChar)

# 2. Reversing a string
# reversedString = myString[::-1]
# reversedString = "".join(reversed(myString))
# print(myString)
# print(reversedString)

# 3. String Slicing - using the colon (:)
# strRange = myString[20:30]
# strRange = myString[20:-1]
# print(strRange)

# 4. updating a string
# print(myString)
# myString = "Learning python is fun"
# print(myString)
# updatedString = myString[0:2] + 'A' + myString[3:]
# print(updatedString)

# 5. Deleting a string
# deletedString = myString[0:5] + myString[7:]
# print(deletedString)
# del myString
# print(myString)

# 6. Escape Sequence

# newString = "We'll learn \t \"python\""
# print(newString)

# 7. formatting a string
string1 = "{} {} {}".format("Learn", "Python", "Programming")
string2 = "{2} {0} {1}".format("Learn", "Python", "Programming")
string3 = "{L} {P} {p2}".format(P="Programming", L="Learn", p2="Python")
print(string3)