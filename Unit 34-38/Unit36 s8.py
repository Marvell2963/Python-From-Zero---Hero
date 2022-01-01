# Class objects Attributes and Methods
    # NOTE: Difference between a Function and a Method 
        # a method is a function that is inside of a class that will actually work with the object in some way. 

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = "mammal"

    def __init__(self,breed,name):
        # Expecting string
        self.breed = breed
        self.name = name

        # OPERATIONS/ACTIONS --> Methods
    def bark(self):
        print("WOOF!")
    
    def bark1(self):
        print(f"WOOF! My name is {self.name}")

    def bark2(self,number):
        print(f"WOOF! My name is {self.name} andthe number is {number}")

my_dog = Dog('Lab','Frankie')

type(my_dog)
my_dog.species  
my_dog.name

my_dog.bark()
my_dog.bark1()
my_dog.bark2(2)
# NOTE:
""" The attributes('.species') never had o/c parentheses, 
because attributes aren't really something that you execute.
Instead, it's just something that's a characteristic of the object that you call back.
"""


class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi
            # because this is a class object attribute, there is two ways to calling it.
             # First is self.pi 
             # Second is circle.pi
        self.area = radius*radius*Circle.pi
    # METHOD
    def get_circumference(self):
        return self.radius *self.pi*2

my_circle = Circle(30)

my_circle.pi

my_circle.radius

my_circle.area

my_circle.get_circumference()