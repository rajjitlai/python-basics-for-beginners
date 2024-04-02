# Some basic functions of python sets are as follows: 
# update
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

# add
set1.add(6)
print(set1)

# remove
set1.remove(3)
print(set1)

# discard
set1.discard(7)

# pop
popped_element = set1.pop()
print(popped_element)

# clear
set1.clear()
print(set1)

# length
length = len(set1)
print(length)

# in and not in
print(2 in set1)
print(3 not in set1)

# issubset or s≤ t
set2 = {4, 5}
print(set2.issubset(set1))

# issuperset or s≥ t
print(set1.issuperset(set2))

# union(t) or s|t
union_set = set1.union(set2)

# intersection(t) or s&t
intersection_set = set1.intersection(set2)

# intersection_update(t)
set1.intersection_update(set2)

# difference(t) or s-t
difference_set = set1.difference(set2)

# difference_update(t)
set1.difference_update(set2)

# symmetric_difference(t)  or s^t
symmetric_difference_set = set1.symmetric_difference(set2)

# copy()
copied_set = set1.copy()

# isdisjoint(t)
disjoint = set1.isdisjoint(set2)

# all(s)
all_true = all(set1)
for x in set1:
    print(x)

# enumerate(s)
enum_set = enumerate(set1)

# max(s)
max_element = max(set1)

# min(s)
min_element = min(set1)

# sum(s)
sum_of_elements = sum(set1)

# sorted(s)
sorted_list = sorted(set1)

# s==t and s≠t
equal = set1 == set2
not_equal = set1 != set2

