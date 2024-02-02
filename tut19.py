# Lists in Python

# list slicing
'''
list_num =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("The list is: ", list_num)
# accessing the values
print("The first value is: ", list_num[0])
print("The fifth value is: ", list_num[5])
# slicing
print("The first five values are: ", list_num[0:5])
print("list between index 2:5", list_num[2:5])
# print("list of [::2]", list_num[::2])
# print("list of [::3]", list_num[::3])
print("list of [1:3]", list_num[1:3])'''

# Updating the values
# some_list = ["Happy", "Tomba", "Chaoba", "Thoiba"]
# print("the names are:", some_list)
# some_list[2] = "Tompok"
# print("After updating...")
# print("the names are:", some_list)


# nested list
# new_list = [1, 2, 3, 'a', ' ', [12, 13, 14, 15], [20, 21], "Tompok"]
# print("The list is: ", new_list)

# # beautify the print
# i = 0
# while i < len(new_list):
#     print("List [",i,"]", new_list[i])
#     i += 1

# basic operations
# len, repetition, in, not in, concatenation, max, min, sum, all, any, list, sorted
# new_list = [1, 2, 3]
# new_list2 = [11, 21, 31, 22, 768, 12,90, 100]
# output_len = len(new_list)
# print(output_len)
# print(new_list)
# check_list = [12, 13, 14, 15] in new_list
# check_listNot = 55 not in new_list
# print(check_list)
# print(check_listNot)
# outputCon = new_list + new_list2
# print(outputCon)
# max_output = max(new_list2)
# min_output = min(new_list2)
# print("The max output is: ", max_output, " and the min output is: ", min_output)
# list1 = [22.1, 45.2, 89.0]
# list2 = [22, 35, 67, 12]
# new_sum = sum(list1)
# print(new_sum)

# num_list = [0] # true if empty
# print(all(num_list))
# num_list = [] # false if empty
# print(any(num_list))

# listItem = list("HelloTomba") # only 1 argument
# print(listItem)

# sorted
# num_list = [4, 9, 10, 44, 77, 90, 1, 54]
# print(sorted(num_list))

# append, count, index, insert, pop,remove, reverse, sort, extend
# newList = ["Tomba", "Chaoba", "Thoiba"]
# newList.append("Henry")
# newList.insert(3, "Henry")
# newList.insert(3, 12)
# print(newList)

# newList = [1, 2, 3, 4, 56, 11, 7, 1, 67, 2, 3, 1, 3, 2, 2, 2, 9]
# print(newList.count(2))
# print(newList.index(31))
# newList.pop(4) # checks the index
# print(newList)
# newList.remove(6) # checks the value
# print(newList)
# newList.reverse()
# print(newList)
# newList.sort()
# print(newList)
# newList2 = [22, 45, 33]
# newList.extend(newList2)
# print(newList)
