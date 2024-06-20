# Inheritance in Python Programming
"""
# class - parent(base)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} is barking")

# class - child(derived)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def breed_know(self):
        print(f"{self.name} is a {self.breed}")

# creating instance for parent
# animal = Animal("Tiger")
# animal.speak()
#  Tiger is barking

# for child
dog = Dog("Rocky", "German Shepherd")
dog.speak()
dog.breed_know()
"""

# single +  multiple
# class Parent1:
#     def display1(self):
#         print("This is parent1 class")

# class Parent2: 
#     def display2(self):
#         print("This is parent2 class")

# class Child1(Parent1, Parent2):
#     def show(self):
#         print("This is a child class")
    
# newChild = Child1()
# function call

# multilevel
# class Parent1:
#     def display1(self):
#         print("This is parent1 class")

# class Parent2(Parent1): 
#     def display2(self):
#         print("This is parent2 class")

# class Child1(Parent2):
#     def show(self):
#         print("This is a child class")
    
# newChild = Child1()
# newChild.display1()
# newChild.display2()
# newChild.show()

# hierarchical

# class Parent1:
#     def display1(self):
#         print("This is parent1 class")

# class Child1(Parent1):
#     def show1(self):
#         print("This is a child1 class")

# class Child2(Parent1):
#     def show2(self):
#         print("This is a child2 class")

# newChild1 = Child1()
# newChild2 = Child2()

# newChild1.display1()
# newChild1.show1()

# newChild2.display1()
# newChild2.show2()

# hybrid 
class Parent1:
    def display1(self):
        print("This is parent1 class")

class Parent2: 
    def display2(self):
        print("This is parent2 class")

class Child1(Parent1):
    def show1(self):
        print("This is a child1 class")

class Child2(Parent2):
    def show2(self):
        print("This is a child2 class")

class GrandChild(Child1, Child2):
    def last(self):
        print("I am the last grandchild")

grandChild = GrandChild()
grandChild.display1()
grandChild.display2()
grandChild.show1()
grandChild.show2()
grandChild.last()

# Subscribe
    