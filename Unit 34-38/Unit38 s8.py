# Special(Magic/Dunder) Methods 


mylist = [1,2,3]
len(mylist) #Common ceck the lenght

#However, how we check the length of one of my own objects?
class Sample():
    pass
mysample = Sample()
len(mysample)  #You can't do this because object of type 'Sample' has no len(). 
print(mysample)  #Also, you can't do this to because it gives you the Sample object is located at your memory.

"""So, the question arises, how am I able to actually use builtin python functions
 such as length or print with my own user defined objects?"""

# THIS IS HOW YOU DO IT 
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages


    def __str__(self):
        return f"{self.title} by {self.author}"

    # What is this does, If there's ever any function that asks for the string representation of your book class, then it's
    def __len__(self):
        return self.pages

    # This is optional if you want to print out a report upon deleting the variable
    # def __del__(self):
        print("A book object has been deleted")

b = Book('Python rocks','Marvell',200)
print(b)
len(b)

    #If we want to delete a book
del b  #This thing would delete from the memory on the computer
b