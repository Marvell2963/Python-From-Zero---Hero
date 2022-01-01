# While loop
    # while loops will continue to execute a block of code while some conditon remains True.

# Syntax of a while loop
"""while some_boolean_condition:
        # do something
    # we can combine with a statement with an else statement, if we want
    else: 
        # do somthing different """

x=0
while x<5:
    print(f'The current value of x is {x}')
    x = x+1 #same as x+=1

# BREAK, CONTINUE, PASS
    # We can use break, continue, pass statements in our loops to add addictional functionalitiy for varius cases,the statement are defined by: 
    # break : Breaks out of the current closest enclosing loop.
    # continue: Goes to the top of the closest enclosing loop.
    # pass: Does nothing at all.

# pass
x= [1,2,3]
for item in x:
    #comment
    pass
print ("end of my script")

# the function is continue at letter equal to a, but didn't print the letter a 
mystring = "Sammy"
for letter in mystring:
    if letter == 'a':
        continue
    print (letter)

# the function is break at letter equal to a
mystring = "Sammy"
for letter in mystring:
    if letter == 'a':
        break
    print (letter)



x = 0
while x <5:
    print(x)
    x+=1
    
x = 0
while x <5:
    if x == 2:
        break
    print(x)
    x+=1