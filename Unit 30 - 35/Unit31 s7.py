# Displaying Information 
"""how to combine a custom function using def along with the already built in print function. 
In order to show something to the user that actually displays like a board game """

# if we want to print mutiple line
print ([1,2,3],'\n',[4,5,6],'\n',[7,8,9])

# we could make a function for the display
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1 = [1,2,3]
row2 = [4,5,6]
row3 = [7,8,9]
display(row1,row2,row3)

# make the inside of the row as emty string and reassign the one of the string to 'x' 
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
row2[1]='x'
display(row1,row2,row3)
