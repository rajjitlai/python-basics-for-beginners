# TUPLE ASSIGNMENT
'''
1.
'''
# (val1, val2, val3) = (45, 21, 18) # assign
# print(val1, val2, val3)
'''
2.
'''
# tup_new = (45, 9, 88, 18, 54)
# (val1, val2, val3, val4, val5) = tup_new
# print(val1, val2, val3, val4, val5)
'''
3.
'''
# (val1, val2, val3) = (2+10, 88//11, 45*2)
# print(val1, val2, val3)

# TUPLE Methods
'''index'''
# newTup = ("Hello", "Mayambu", "RJ", "Coding", "Tips", "Ta", "Taramna", "Okchari")
# print(newTup.index("Hello"))
'''count'''
# newTup = (10, 23, 10, 22, 56, 10, 78, 10, 44, 10)
# newTup2 = ("Hello", "This", "is", "RJ", "Hello")
# newTup3 = "xabnkuetgdyudaxxlxokoperwtuy8utydtgqwyuehte4rtiyubvbxx"
# print("10 appears ", newTup.count(10), " times in ", newTup)
# print("Hello appears", newTup2.count("Hello"), " times in ", newTup2)
# print("b appears", newTup3.count('b'), " times in", newTup3)
'''
zip function
'''
a = ("John", "Charles", "Mike")
b = ["Jenny", "Christy", "Monica"]

x = zip(a, b)
print(x) # memory address
print(tuple(x)) # access list/tuple