# list comprehensions / one line for loop
# list comprehensions are a unique way od quickly creating a list with python

# comparison one line and couple line in retrun string in list
mystring='hello'
mylist =[]
for letter in mystring:
    mylist.append(letter)
mylist

mylist = [letter for letter in mystring]
print(mylist)


# 
mylist = [num for num in range(0,11)]
mylist
    # make the result in to power of two 
mylist = [num**2 for num in range(0,11)]
mylist
    # one line forloop-if
mylist = [num for num in range(0,11) if num%2==0]
mylist


# comparison one line and multiple line
celcius = [0,10,20,34.5]
fahrenheit = [(9/5*temp +32)for temp in celcius]
fahrenheit

fahrenheit = []
for temp in celcius:
    fahrenheit.append((9/5)*temp+32)
fahrenheit

# if else in list comprihention
results = [x if x%2==0 else "ODD" for x in range(0,11)]
results

# nest loops in list comprihention
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
mylist 
 