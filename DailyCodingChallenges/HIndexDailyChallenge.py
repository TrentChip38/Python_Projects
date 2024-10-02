#In academia, the h-index is a metric used to calculate the impact of a researcher's papers. 
#It is calculated as follows:A researcher has index h 
#if at least h of her N papers have h citations each. 
#If there are multiple h satisfying this formula, the maximum is chosen.

#For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.
#Given a list of paper citations of a researcher, calculate their h-index.

def IndexH(citations):
    h = 0
    i = 0
    length = len(citations)
    for i in range(1, length):
        count = 0
        #print("Item:", i)
        for citation in citations:
            if (citation >= i):
                count += 1
        if (count >= i):
            h = i
        else:
            return h

#test/use function
arr = [4, 3, 0, 1, 5]
print(IndexH(arr))
arr = [4, 3, 0, 1, 5, 5, 5, 5]
print(IndexH(arr))
arr = [4, 3, 0, 1, 5, 5, 5, 5, 6]
print(IndexH(arr))