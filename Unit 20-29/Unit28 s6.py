# Lambda Expression, Map,and Filter
    # Lambda expressions are a way to quickly create what are known as anonymous functions, basically just one time use functions

def square(num):
    return num**2

# Map
    # map is you pass in The function that you want to map to every single element or item in this list.
my_nums = [1,2,3,4,5]
map(square,my_nums) # Return location on your computer as a memory
        # The return is not super usefull

    # What you can do is actually iterate through this.
my_nums = [1,2,3,4,5]
for item in map(square,my_nums):
    print (item)
        # What this does is it generates applying this square function to every single item

    # Another way to use this 
list(map(square,my_nums))

    # def work with map 
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']
list(map(splicer,names))
        # when using map we are not calling them to execute of inside map like this : map(slicer(),names)
            # this is because map by itself is later on going to execute them.


# Filter function
    # return iterator eather Ture or false 
    
    # filter function is going to filter based of the function's condition.
def check_even(num):
    return num%2 ==0

mynums = [1,2,3,4,5,6,7,8]
list(filter(check_even,mynums))

    # OR 
for n in filter(check_even,mynums):
    print(n)
    
# lambda expressions
square = lambda num: num**2
square(5)

    # by using map so now we can make it more short
    #map
mynums = [1,2,3,4,5,6,7,8]
list (map(lambda num:num**2,mynums))
    #filter
list(filter (lambda num: num%2 == 0, mynums))

    # onther usefull use lambda expression
names = ['Andy', 'Eve', 'Sally']
list(map(lambda x:x[::-1],names))