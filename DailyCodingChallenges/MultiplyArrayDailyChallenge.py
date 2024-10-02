#Given an array of integers, 
# return a new array such that each element 
# at index i of the new array 
# is the product of all the numbers 
# in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].

def Multiply(Listnums):
    Products = []
    product = 1
    for number in Listnums:
        product = product * number
    print(product)
    print("Length: ", len(Listnums))
    for index in range(len(Listnums)):
        print("Index: ", index)
        print("Number: ", Listnums[index])
        Products.append(int(product/Listnums[index]))
        print(Products)

ExampleArray = [1, 2, 3, 4, 5]

Multiply(ExampleArray)