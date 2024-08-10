# MODULES

# import tut28

# do_add = tut28.add(10, 20)

# print('Sum: ', do_add)

# PACKAGES
# from tut28package import *
from tut28package import simple, diff

do_add = simple.simpleAdd(45, 99)
print("Sum:", do_add)

findPower = diff.power(2, 8)
print("Number:", findPower)

