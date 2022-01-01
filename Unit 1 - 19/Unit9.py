# Tuples
    # Tuples are SIMILAR to list. However they have one key difference - IMMUTABILITY.
    # Once an element is inside a tuple, it can not be reassigned.
    # Tuples use parenthesis: (1,2,3)

    # Type of the function 
tup = (1,2,3)
type(tup)
mylist = [1,2,3]
type(mylist)

    # Can count the lenght
len(tup)

    # Index
t = ('one','two','three')
t[0]
t[-1]

    # Count how many specific item in tuple
t= ('a','a','b')
t.count('a')

        # the index will only return back the index location that it appears
t.index('a')
t.index('b')

    # Showing tuples is immutable
mylist[0]='one'
mylist
t[0]='one'