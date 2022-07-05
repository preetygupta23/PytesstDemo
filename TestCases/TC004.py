"""
Examples of One liner code in python.
"""

# to swap two numbers a and b
a, b = 10, 5
print("Before swapping :", a, b)
a, b = b, a
print("After swapping :", a, b)

# To print even numbers

evenNumbers = [x for x in range(11) if x % 2 == 0]
print("The even numbers are :", evenNumbers)


# To reverse a list

lis = [1, 2, 3]
reversed_list = lis[::-1]

print("The reversed list is :" , reversed_list)
