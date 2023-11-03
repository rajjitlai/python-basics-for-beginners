# Python File methods and Directory methods

# File methods - rename()
# syntax - 
#     os.rename(old_filename, new_filename)

import os
# os.rename('tutorial15.txt', 'tut15.txt')
# print("File renamed")

# remove()
# syntax -
#     os.remove(Filename)
# os.remove('testfile.txt')

# Directory method - mkdir()
# syntax - 
#     os.mkdir(folder_name)
# os.mkdir('project')
# os.rename('project/project1.txt', 'project/newProject.txt')

#  getcwd()
# syntax - 
    # os.getcwd()
# print(os.getcwd())

# chdir()
# syntax - 
#     os.chdir("dirname")
# os.chdir("project")
# print(os.getcwd())

# rmdir()
# syntax -
#     os.rmdir("dirname")

# os.rmdir("project") # if not empty, it will give error

# makedirs()
# syntax -
# os.makedirs("ndir1\\ndir2\\ndir3\\ndir4")

# Extra
os.startfile("C:\\Windows\\explorer.exe")