# Accepting User Input
    # the input function is simply the key word input.

input("Please enter a value: ")
# save it as a variable 
result = input("Please enter a value: ")
result
type(result) # the input function is always return a string 

# to change the output of the input
change = int(result)
change
    # or what you can do 
result = int(input("Please enter a value: "))
result

## Input Function is always going to return a string, which means you may need to convert it.


row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
position_index = int(input("Choose an index position: "))
row2[position_index]


# NOTE: make sure that the input has to be a legitimate input
    # meaning it likes a normal integer
    
# NOTE : the code would pending if some of these things happen
    # can not get the last codde because the program is watiting for the inut
result = input("enter a number: ")
2+2 
    # double click enter
input("Enter Number: ")
    # first enter and it is work, but when you accidentally click on this cell again and the code is not working
    # this is because I accidentally try to overwrite that input cell.But that initial input is still waiting for its interaction, its value.