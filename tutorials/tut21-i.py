# dictionary

# syntax
# dict_new = {key_1: val_1, key_2: val_2, key_3: val_3,...}

# create 
# empty_dict = []
# print("The dict empty_dict is an empty dictionary with the items ", empty_dict)
# new_dict = {"pilcrow": "a paragraph mark.", "vital": "important"}
# print("Meaning of vital is: ", new_dict["vital"]) # access
# access
stud_dict = {"Roll_no": "B120", "Name": "Jamesbond", "Course": "BTech"}
print("Before Course: ", stud_dict["Course"])
# print("Roll no of the student is: ", stud_dict["marks"]) # if no key is in the dictionary so, it will give keyerror

# add
# stud_dict["marks"] = 97
# print("Mark of the student is: ", stud_dict["marks"])

# modify
# stud_dict["Course"] = "BCA"
# print("New Course is:", stud_dict["Course"])

# delete - del keyword
# print("Before deleting:", stud_dict)
# del stud_dict['Course']
# print(stud_dict)
del stud_dict # delete the whole dictionary
print(stud_dict)