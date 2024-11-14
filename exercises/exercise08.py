# Python program to print the pattern
"""
                  *
            *     *     *
      *     *     *     *     *
"""

# def printPattern():
#     rows = int(input("Enter the number of rows: "))
#     k = 2 * rows - 2

#     for i in range(0, rows):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 2
#         for j in range(0, 2 * i - 1):
#             print("*", end=" ")
#         print(" ")

# printPattern()

# print("*")


def patternPrint():
    rows = int(input("Enter the number of rows: "))
    # rows = 5
    for i in range(1, rows + 1):
        # print the spaces
        for j in range(rows - i):
            print(" ", end=" ")

        # print the numbers
        for j in range(i, 2 * i):
            print(j, end=" ")
        for j in range(2 * i - 2, i - 1, -1):
            print(j, end=" ")
        print("")


# function call
patternPrint()
