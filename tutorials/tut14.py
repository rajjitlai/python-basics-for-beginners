# open and closing functions with commands

# fileCon = open("file.txt", "rt") # in read mode - by default
#fileCon = open("file.txt", "rb") # in binary - by default

#print(fileCon.read())  # using read function

f = open("file.txt", "rt")
content = f.read()
print(content)
f.close()