# Given an array of integers, 
# return a new array where 
# each element in the new array 
# is the number of smaller elements 
# to the right of that element 
# in the original input array.

def totheright(list):
    new_list = []
    i = 0
    length = len(list)
    while i < length:
        count = 0
        j = i + 1
        while j < length:
            if list[j] < list[i]:
                count += 1
            j += 1
        i += 1
        new_list.append(count)
    return new_list

list = [3, 4, 9, 6, 1]
list = [1, 9, 90, 6, 1]
print(list)
list2 = totheright(list)
print(list2)
list3 = totheright(list2)
print(list3)
list4 = totheright(list3)
print(list4)
