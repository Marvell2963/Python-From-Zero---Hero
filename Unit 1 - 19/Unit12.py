# I/O with basic Files 

# From Internet
    # How to OPEN a text file
        # To open a file, we need to use the build-in open function.
        # Open file function returns a file object that contains methods and attributes to perform various operations for opening files in Python.

file_object = open("filename","mode")
# filename: gives name of the file that the file object has opened.
# mode: attribute of a file object tells you which mode a file was opened in.

    # How to CREATE a text file in python
        # we can create a .txt files (practiceTxt.txt)

f = open("practicetxt.txt","w+")
# We declared the variable f to open a file named practiceTxt.txt.
    # Open takes 2 arguments, the file that we want to open and a string that represents the kinds of permission or operation we want to do on the file
# Here, we used "w" letter in our argument, which indicates Python write to file and it will create a file if it does not exist in library
# Plus sign indicates both read and write for Python create file operation.

for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
# We have a for loop that runs over a range of 10 numbers.
# Using the write function to enter data into the file.
# The output we want to iterate in the file is "this is line number", which we declare with Python write to text file function and then percent d (displays integer)
# So basically we are putting in the line number that we are writing, then putting it in a carriage return and a new line character

f.close()
# This will close the instance of the file practicetxt.txt stored


# Full Coding 
def main():
    f = open("practicetxt.txt","w+")
    for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
    f.close()

if __name__=="__main__":
    main()

# How to READ files
    # Open the file in Read mode
f=open("practicetxt.txt", "r")
    # We use the mode function in the code to check that the file is in open mode. If yes, we proceed ahead
if f.mode == 'r':
    # Use f.read to read file data and store it in variable content for reading files in Python
    contents= f.read()
    #Print contents for Python read text file
def main():
    pass

#NOTE:
# You don not need to focus on text file because there are a lot of type of it. There are docs file, axle file.