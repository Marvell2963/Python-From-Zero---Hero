# Introduction String
    # String(str) are sequences of characters. you can use either single quotes or double quotes
        # Ex: 'Hello' or "Hello"

    # Because strings are ordered sequences it means we can using indexing and slicing to grab sub-sections of the string
    # Indexing notation uses [] notation after the string (or variable assigned the string)
    # Indexing allows you to grab a single character from the string

    # Character     : h  e  l  l  o
    # Index         : 0  1  2  3  4
    # Reverse Index : 0 -1 -2 -3 -4

    # Note:
        # "Indexing" means referring to an element of an iterable by its position within the iterable.
        # "Slicing" means getting a subset of elements from an iterable based on their indices.

    # Indexing
mystr = ["a","b","c","d","e","f"]
print (mystr [0])

    # Slicing
mystr = ["a","b","c","d","e","f"]
print (mystr [0:3])

    # string[::] --> [begin:end:step size]
mystr = ["a","b","c","d","e","f"]
print (mystr [::2])

mystr = ["a","b","c","d","e","f"]
print (mystr [::-1])

    # \n = next line 
    # \t = tab 
print("hello \nworld")
print("hello \tworld")

    # len = how many index/indexing in the string  **note: space also count 
len("hello")
len("I am")
