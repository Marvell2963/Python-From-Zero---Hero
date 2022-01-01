# if elif and else 
    # control flow is the order in which the program's code executes
    # to control flow of logic we use some keywords: 
        # if elif else 
    # control flow syntax makes use of colons and indentation (whitespace).
        # the indentation is crucial to python and other programming languages.
        # an indentation allows python code to be easily readable and very quick to prototype.

# if statement
"""if some_condition:
        # execute some code"""
# elif statement
""""elif some_other_contion:
        # do something different"""
# NOTE: you can have elif as many as you want 
# else statement
"""else:
        # do something else"""

# if statement EXAMPLE 
if True:
    print("IT IS TRUE!")

if 3>2:
    print("IT IS TRUE!")

hungry = True
if hungry:
    print('FEED ME!')

# else statement EXAMPLE

hungry = True
if hungry:
    print('FEED ME!')
else:
    print('I am not hungry')
# NOTE: if some condition and happened to be false, the code is not execute.

loc = 'Bank'
if loc == ' auto shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'store':
    print('Wellcom to the store')
else:
    print('I do not know much.')