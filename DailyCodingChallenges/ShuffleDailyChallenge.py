#Given a stack of N elements, 
# interleave the first half of the stack with the second half 
# reversed using only one other queue. This should be done in-place.
# Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.
# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
# If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].
# Hint: Try working backwards from the end state.
import math
def shuffle(stack):
    #queue to create
    queue = []
    length = len(stack)
    #know length and half length rounded up
    half_len = math.ceil(length/2)
    print(half_len)
    i = 0
    #loop through going forward and backward at same time
    while i < half_len:
        #add front
        queue.append(stack[i])
        #and then add back
        if (i != (length - i - 1)):
            #unless odd and already added
            queue.append(stack[length - i - 1])
        i += 1
    return queue

#with given stack run code
stack = [1, 2, 3, 4, 5]
print(shuffle(stack))
stack = [1, 2, 3, 4]
print(shuffle(stack))
