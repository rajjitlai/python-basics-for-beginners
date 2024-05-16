# Class Methods

class Number:
    evens = [] # lists of even numbers
    odds = [] # lists of odd numbers

    # construct
    def __init__(self, num):
        self.num = num
        if num % 2 == 0:
            print(f"The number {num} is even")
            Number.evens.append(num)
        else:
            print(f"The number {num} is odd")
            Number.odds.append(num)

    # delete
    def __del__(self):
        print(f'The number {self.num} is deleted')

# calling the class
n1 = Number(12)
n2 = Number(14)
n3 = Number(10)
n4 = Number(15)
n5 = Number(21)
n6 = Number(45)

print("The even numbers are: ", Number.evens)
print("The odd numbers are: ", Number.odds)

# del n2

# print("Instance/attribute n2 is deleted")
