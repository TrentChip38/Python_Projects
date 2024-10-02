# Given a list of words, 
# find all pairs of unique indices 
# such that the concatenation 
# of the two words is a palindrome.
# For example, given the list 
# ["code", "edoc", "da", "d"]
# return [(0, 1), (1, 0), (2, 3)]

#find all word palindrom combos in a list
def palicombos(list):
    setList = []
    #For each word, loop through each word
    for index1, word1 in enumerate(list):
        for index2, word2 in enumerate(list):
            #check if those words added in order are palindrome
            if palindrome(word1 + word2) and (index1 != index2):
                #add if they are, and are not the same word index
                setList.append((index1, index2))
    return setList

#check if a single word is a palindrome
def palindrome(word):
    print("Word: ", word)
    i = 0
    length = len(word)
    #by looping through forwards and backwards at same time
    #and checking each front and back going in to be same
    while i < length:
        if word[i] != word[length - i - 1]:
            #if any diffrent then not a palindrome
            return 0
        i +=1
    print("Palindrome")
    return 1

#Run and test
list = ["code", "edoc", "da", "d"]
print(list)
print(palicombos(list))