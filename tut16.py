# read(), readline(), readlines(), write(), writelines(), seek(), tell()
# python file commands

# a = open('tut15.txt', 'r') # read
# a = open('tut15.txt', 'a') # append
# a = open('tut15.txt', 'w') # write
# a = open('tut15.txt', 'x') # create
# a = open('tut15.txt', 'w+') # write
# a.write('This is the Python Basics for Beginners Course by RJ Coding Tips')# this will point at the end of the file
# a.seek(0)# without this, it will not show the contents - it will point to the top part of the content if 0
# content = a.read() 
# print(content)


# readline() - used to read a single line
# a = open('tut15.txt', 'r') 
# # content = a.readline()
# # readlines() - used to read all the lines
# content = a.readlines()
# print(content)
# a.close()

# writelines
names = ["Rajjit", "Tomba", "Chaoba", "Sigma"]
with open('tut15.txt', 'w') as a:
    a.writelines([name + "\n" for name in names])
a.close()