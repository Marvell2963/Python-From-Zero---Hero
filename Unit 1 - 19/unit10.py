# Sets
    # Sets are unordered collections of UNIQUE elements.
        # Meaning there can only be one representative of the same objects.

    # Ex 1
mysets = set()
mysets
mysets.add(1)
mysets
mysets.add(2)
mysets
        # Can't make it like this {1,2,2} because sets has to be unique elements.
mysets.add(2)
    
    # Sets is really useful for casting a list to a set that we only get the unique values
        # Example
mylist = [0,1,1,2,2,2,3,3,3,3]
set(mylist)
    # NOTE sets don't technically have an order to them
        # Example 
myset = [0,'a','b',1,1,2,2,2,3,3,3,3]
set(myset)

