list = [-5,-3,0,1,2,3,5,7,8]
i = 0
num = 1
#loop through whole list
size = len(list)
while(i < size):
    #if int greater than 0 check against 1,2,3,4...
    if(list[i] > 0):
        if(list[i] != num):
            print("Missing: ", num)
            exit()
        num += 1
    i += 1