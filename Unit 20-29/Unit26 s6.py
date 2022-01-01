# Interactions between python functions
    # Typically a python script or notebook contains several functions interating with each other. 

# Make a game
""" you start off with three cups and underneath one of them is hit in a red ball.
Then, we're going to do is shuffle these cups around, have the user guess where the red ball is, and then they're either right or wrong."""

# Our game would not show the cups or ball, instead we will mimic the effect with python list.
# Our version also not show the shuffle to the user, so the guess is completely rando.


example = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
example

# The game 3 cups 1 ball
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
result

mylist = [' ','o',' ']
shuffle_list(mylist)
def player_guess():
    guess =''
    while guess not in ['0','1','2']:
        guess = input("Pick number: 0,1, or 2 ")        
    return int(guess)

player_guess()

myindex = player_guess()
myindex

def check_guess(mylist,guess):
    if mylist[guess] == 'o':
        print ("correct!")
    else:
        print ("wrong guess!")
        print (mylist)

# Intial list
mylist = [' ','o',' ']
# Shuffle list
mixedup_list = shuffle_list(mylist)
# User guess
guess=player_guess()
# Check guess
check_guess(mixedup_list,guess)