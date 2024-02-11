# TUPLE
new_Tup = (1, 2, 3, 4,5 ,6, 7, 8, 9, 10)
# print(type(new_Tup))
# access + slicing
# print("First:", new_Tup[0])
# print("Slicing [3:6]: ", new_Tup[3:6])
# print("[:8]", new_Tup[:8])

# update or concatenation
new_Tup2 = (31, 34, 56, 77)
# new_Tup3 = new_Tup + new_Tup2
# print(new_Tup)

# delete
# try:
#     del new_Tup
#     print("new_Tup deleted successfully")
# except NameError as e:
#     print(e)
# print(new_Tup)

# nested tuple
# nested_tup = (1, 2, 3, 4, ("hello", "mister"), (3.6, 88.08), "Welcome to RJ Coding Tips")
# print(nested_tup)

# len, repetition, concatenation, membership, iteration, comparison, max, min, conversion to tuple

# lenOfTup = len(new_Tup)
# print(lenOfTup)

# new_Tup2 = ("Hello"*2, "Programmers"*3)
# print(new_Tup2)

# check_mem = 5 in new_Tup
# print(check_mem)

# for i in new_Tup:
#     print(i)

# new_Tup2 = (1, 2,3, 4, 5, 6, 7, 8, 9, 10)
# print(new_Tup == new_Tup2) # <, > , ==

# maxTup = max(new_Tup2)
# maxTup = min(new_Tup2)
# print(maxTup)

newString = "Welcome to RJ Coding tips. Hit that Subscribe Button"
newTup = tuple(newString)
print(newTup)