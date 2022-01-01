# useful operators 
    # mylist = [1,2,3]
    # this is common task and python has build-in operator for this task:
        # 2 ways to do it :
            # 1.iterate through it
            # 2.enumerate 

# 1. iterate 
for num in range(10):
    print (num)
for num in range(2,10):
    print(num)
for num in range(0,10,1):
    print(num)
# this is similar to slicing syntex from previous unit
# range(starting point,end,stepsize)

list(range(0,10,2))

# 2. enumerate 
word = 'abcde' #return as a touple
for item in enumerate(word):
    print(item)
word = 'abcde' # we can seperate the index and the letter by using touple unpacking
for index,letter in enumerate(word): #return as a touple
    print(index)
    print(letter)
    print("\n")

# Zip sunction
# We can put as many list as you can in zip
# NOTE: ZIP is only to be able to go and zip together as far as the lish, which is the shorthest
mylist1 = [1,2,3,4]
mylist2 = ['a','b','c','d','e']
for item in zip(mylist1,mylist2):
    print(item)

list(zip(mylist1,mylist2))

# end operator (quickly check if the character is in the list
    # end operator can work in list, string, dictionary 
        # list
'x' in [1,2,3] #return False 
2 in [1,2,3] # return True
'x' in ['x','y','z'] # return True
        # string 
'l' in 'hello world'
        # dictionary
'mykey' in {"mykey":345} # what happend is the mykey is in dic

d = {"mykey":345}
345 in d.values()

mylist = [1,10,100,1000,10000]
min(mylist)
max(mylist)



# random library
from random import shuffle #shuffle is it randomly shuffles around any sort of list
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
mylist

# Grabing a random integer 
from random import randint
randint(0,100)

mynum = randint(0,100) # we can save it to generate random number
mynum

# user input
# NOTE: input always accepts anything that's passed into it as a string 
result = input('enter a number here: ')

result = input('what is your name: ')
result

