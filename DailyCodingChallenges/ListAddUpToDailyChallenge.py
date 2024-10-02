#problem 1
#true if 

def AddsToNum(k, nums):
    for index1, number1 in enumerate(nums):
        for index2, number2 in enumerate(nums):
            if ((number1 + number2) == k) and (index1 != index2):
                print(number1, " and ", number2, " add to ", k)
                return True
    return False

Numlist = [10, 11, 3, 4]

print(AddsToNum(20, Numlist))