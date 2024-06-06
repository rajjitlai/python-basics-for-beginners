# remaining class methods

class Example:
    def __init__(self, num):
        self.num = num

    # representation
    def __repr__(self):
        return f"{self.num}"
    
    # compare
    def __eq__(self, value):
        return self.num == value.num
    
    # length
    def __len__(self):
        return len(self.num)
    
# creating instance
obj1 = Example([1, 2, 3, 4, 5])
obj2 = Example([11, 22, 33, 44, 55, 67, 99, 100])
obj3 = Example([20, 40, 60, 80, 100])
obj4 = Example([1, 2, 3, 4, 5])

# printing the class methods 
# repr
# print("The data in example is ", obj1)
# eq / cmp
# print(obj1 == obj4)
# len
print(len(obj2))