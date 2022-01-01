# Class Objects Attributes and Methods


# when we use mylist. or myset. and it appers bunch of function that we can use
mylist = [1,2,3]
myset = set()
type(myset)
type(mylist)

# NOW, how we can use the class keyword to create a user defined object.
class Sample(): 
    pass #what is is this doing is basicly to create class and that's it. nothing else there.
my_sample = Sample()
type(my_sample) 
""" class is basically a blueprint that defines the nature of a future object from classes.
We can then construct an instance of the object and an instance is a specific object created from a particular class."""


# How to create attribute 
class Dog():
    def __init__(self,breed):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed

my_dog = Dog(breed='Huskie')
type(my_dog)

my_dog.breed
    # mybreed is was just the parameter name we choose for the argument


# Breakdown what is going on 
class Dog():
    def __init__(self,mybreed):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.my_attribute = mybreed

my_dog = Dog(mybreed='Huskie')
type(my_dog)

my_dog.my_attribute


# give it more atribute
class Dog():
    def __init__(self,breed,name,spots):
        # Expecting string
        self.breed = breed
        self.name = name
        # Expect boolean True/False
        self.spots = spots

my_dog = Dog(breed="lab",name='sammy',spots=False)
my_dog.breed


