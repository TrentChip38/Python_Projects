#212
#Spreadsheets often use this alphabetical encoding for its columns: 
# "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

#Given a column number, return its alphabetical column id. 
# For example, given 1, return "A". Given 27, return "AA".
import math


#this is not a very good way to do this, but I started it and then
#wanted to see if I could figure out the correct math with dividing,
#remainders and manipulation etc.
def NumToEncoding(num):
    letters = ""
    if(num < 27):
        #If first 26 then just single character
        letters = chr(num + 64)#+64 converts to correct ascii value
    elif (num <= 27*26):
        #If 2 letter encoding first set first digit
        letters = chr(math.ceil(num / 26) + 63)
        remainder = num%26
        #then modulo 26 and remainder 0 is z
        if(remainder == 0):
            letters = letters + 'Z'
        else:#else remainder + 64
            letters = letters + chr(num%26 + 64)
    elif (num <= 27*26*26):
        #for all 3 digit encodings
        #print(num//(26*26))
        #divide to find first number
        letters = chr((num // (26*26)) + 64)
        #Then second number is remainder divided by 26 rounding up
        remainder = num%(26*26)
        #print(remainder)
        div = math.ceil(remainder/26)
        #print(div)
        #and same logic for Z
        if(div == 1):
            letters = letters + 'Z'
        else:
            letters = letters + chr(div + 63)
        #then 3rd digit is also just modulo 26
        remainder = num%(26)
        if(remainder == 0):
            #with logic for remainder 0 = Z
            letters = letters + 'Z'
        else:#else add 64 to get to ascii character value
            letters = letters + chr(remainder + 64)
    return letters

#Test
#print(chr(64+27))
#(NumToEncoding((27*26)+1+(26*1)))
print(NumToEncoding((27*26)+1))


#If I re-wrote this, I would have funcitons to increment for each digit,
#with logic to roll over and add digits to next place,
#Would roll around 1-26 for as many digits as neaded,
#and then convert all to chars in the right order


def RollAroundEncoding(num):
    encoding = [0]
    #function to increment one digit rolling over to next recursively
    def incrementEncoding(digit):
        if(encoding[digit] < 26):
            encoding[digit] += 1
        else:
            #reset this digit and increment next
            encoding[digit] = 1
            #add next digit if it doesn't exist
            if(len(encoding) < digit+2):
                encoding.append(0)
            #call increment on that digit
            incrementEncoding(digit+1)
            #also increment any previouse digits
            i = 0
            while(i < digit):
                encoding[i] = 1
                i += 1
    #Then call that function to increment as many as your number
    for i in range(num):
        incrementEncoding(0)
    #Next convert into characters and flip forwards
    LetterEncoded = ""
    for val in encoding:
        LetterEncoded =  chr(val + 64) + LetterEncoded
    return LetterEncoded

#test with any range of values
for val in range(1500):
    print(RollAroundEncoding(val))