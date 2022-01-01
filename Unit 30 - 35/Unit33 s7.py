# Validating User Input
    # we already learn about input(), now explore how to further validate user inut to avoid errors for invalid conversions.

# this is one of the problem 
def user_choice():
    choice = input("Please enter a number (0-10): ")
    return int(choice)
user_choice()

    # There is Two problems of this right now:
        # First, if I put any other input like "nine", and the program going to give you an error
        # Second, the code is specifically asking for the numbers, zero through 10, but if we put 100, it would give you 100 not error.
    
    # one of the ways to solve the problem
def user_choice():
    choice= "Wrong"
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")
    return int(choice) 
user_choice()
        # the function would return the question input until the user give the true input
    
    # if the input is wrong print something else
def user_choice():
    choice= "Wrong"
    while choice.isdigit() == False:
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == False:
            print("sorry that is not a digit")
    return int(choice) 
user_choice()

    # make the input is in the range from 0-10
def user_choice():
    choice= "Wrong"
    acceptable_range = range(0,10)
    within_range = False
    # two contditions to check 
    # digit or within_range==False
    while choice.isdigit() == False or within_range == False:

        choice = input("Please enter a number (0-10): ")
        
        # Digit check 
        if choice.isdigit() == False:
            print("sorry that is not a digit")
        
        # Range Check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
    return int(choice) 
user_choice()
