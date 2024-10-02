#Given a string and a pattern, 
# find the starting indices of all occurrences 
# of the pattern in the string. For example, 
# given the string "abracadabra" 
# and the pattern "abr", 
# you should return [0, 7].

def FindStringPattern(Word, substring):
    Length = len(substring)
    Spots = []
    for i in range(len(Word)):
        #print("Index: ", i)
        #print(Word[i:i+Length])
        if(i+Length <= len(Word)):
            if(Word[i:i+Length] == substring):
                #print("True")
                Spots.append(i)
    return Spots

print(FindStringPattern("abracadabra", "abra"))