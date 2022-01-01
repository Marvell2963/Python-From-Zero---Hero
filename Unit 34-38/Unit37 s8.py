# Inheritance and Polymorphism

# Inheritance
    # it's a way to form new classes using classes that have already been defined.
    # Benefits of inheritance  the ability to reuse code that you've already worked the ability to reuse code that you've already worked on and to reduce the complexity of a program.
from typing import ClassVar


class Animal():
    def __init__(self):
        print ("ANIMAL CREATED") 
    def who_am_i(self):
        print("I AM AN ANIMAL")
    def eat(self):
        print("I AM EATING")

class Dog(Animal):  # this is know as a derived class because I'm deriving some of my features from this space class
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    # you are able to overwrit the previous methods 
    def who_am_i(self):
        print("I am a dog!")

    def BArk(self):
        print("woof!")

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.BArk()
myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()


# Polymorphism
# Polymorphism refers to the way in which different object classes can share the same method name,
 # and then those methods can be called from the same place, even though a variety of different objects might be passed in.

class Dog():
    def __init__(self,name):
        self.name = name
    def speak (self):
        return self.name +" says woof!"
class Cat():
    def __init__(self,name):
        self.name = name
    def speak (self):
        return self.name +" says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

#  There's a few different ways to demonstrate polymorphism.
    
    # first, using forloop
for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

    # second, abstract classes and inheritance
class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

        # this is what you should do 
class Dog(Animal):
    def speak(self):
        return self.name +"says woof!"
class Cat(Animal):
    def speak(self):
        return self.name +"says meow!"
fido = Dog("Fido")
isis = Cat("Isis")
print(fido.speak())
print(isis.speak())

        # if you do this it would give me an error because in the base class itself, it doesn't actually do anything
         # It's expecting you to inherit the animal class and then overwrite the speak method.
myanimal = Animal("fred")
myanimal.speak()



""" polymorphism basic idea is you have these two separate classes that happen to share the same method name,
 allowing you to then call those same method names without needing to worry about the specific class that's being passed in."""