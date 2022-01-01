# *args and **kwargs

# *args
    # args return a touple 
    # if we want more result we need editing the paramiter 
def myfunc(a,b,c=0):
    # return 5% of the sum of a and b.
    return sum ((a,b,c))*0.05
myfunc(40,60,20)
    
    # Can put the input as much as the parameter that you put
def myfunc(*args):
    return sum(args)
myfunc(30,40,60) 

def myfunc(*args):
    return sum(args)*0.05
myfunc(30,40,60) 

    # As long as there is a star in the parameter, but to make it clear for other person use args
def myfunc(*spam):
    return sum(spam)
print(type(myfunc(30,40,60)))

# **kwargs 2
    # kwargs return a dictionary 
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print ('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit = 'apple', veggie = 'lettuce')

# Use *args and **kwargs at same function
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print ('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')
