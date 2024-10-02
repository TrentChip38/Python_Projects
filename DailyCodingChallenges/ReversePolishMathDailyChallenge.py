# Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
# The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
# For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

# Use a list to create a stack that we can push and pop from
# Read and write to stack if value or operand
def polish(list):
    stack = []
    for item in list:
        if isinstance(item, str):
            #pop last two values
            num1 = stack.pop()
            num2 = stack.pop()
            #and push operation result to the stack
            match item:
                case '+':
                    stack.append(num1 + num2)
                case '-':
                    stack.append(num2 - num1)
                case '/':
                    stack.append(num2/num1)
                case '*':
                    stack.append(num1*num2)
            print(stack)
        else:
            #add numbers to the stack
            stack.append(item)
    #return final value when no more items
    return stack.pop()
            
#now i'll test with their lists
print("Test polish function")
list = [5, 3, '+']
print("List: ", list)
print("Result: ", polish(list))
list = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
print("List: ", list)
print("Result: ", polish(list))