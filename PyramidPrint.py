import math

def PrintPyramid(rows):
    #Set offset for everything
    start_space = "    "
    #Calculate length of last row
    if rows < 10:
        end_length = rows*2
    elif rows < 100:
        end_length = rows*3
    elif rows < 1000:
        end_length = rows*4
    else:
        print("Too big for programmed length")
        return 0
    #print("Row Length: ", end_length)
    #Loop through each row
    for row in range(rows):
        #Print space before row
        print(start_space, end="")
        add_space = ""
        #Calc this rows length
        if row < 10:
            row_length = row*2
        elif row < 100:
            row_length = row*3
        elif row < 1000:
            row_length = row*4
        #Add space to align with middle of row 
        add_amount = math.ceil((end_length - row_length)/2)
        for j in range(add_amount):
            add_space += " "
        print(add_space, end="")
        #Each row print that many of that number
        for j in range(row):
            #Add space between all characters
            line = str(row) + " "
            print(line, end="")
        #Print new line
        print()

#Test run code for any number of rows
PrintPyramid(60)