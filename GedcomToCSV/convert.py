#How to open GEDCOM file
file_path = 'your_family_tree.ged'

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Process each line here
        print(line.strip()) # Use .strip() to remove leading/trailing whitespace and newlines

#Could then parse and split each line looking for the categories
#Create new object when you find a new individual and name
#Store all the next data under them in an object
#Make the objects into a csv table with grouped columns