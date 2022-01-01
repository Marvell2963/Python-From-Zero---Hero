# for loop 
    # many object in python are "iterable", meaning we can iterate over every element in the object.
        # such as every element in a list or every character in a string.
    # for loop can execute a block of code for every iteration.

    # the term iterable means you can "iterate" over the object.
    # For example you can iterate over every character in a string, iterate over every item in a list iterate over every key in a dictionary.

# syntax of the for loop:
    # List-forloop
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    print('Hello')

mylist = [1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    if i%2 == 0:
        print (i)
    else :
        print(f'odd number: {i}')

mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for i in mylist:
    list_sum = list_sum + i
    print(list_sum) # Print the result of the forloop and back to the for loop until the final answer.
print(list_sum)  # Only print the last number the result
#NOTE: Indentation matter !!!

    # String-forloop
mystring = 'Hello World'
for letter in mystring:
    print(letter)

for letter in 'Hello World':
    print(letter)

    # Toople-forloop
tup = (1,2,3)
for item in tup:
    print(item)
    print(tup)

    # Tuple unpacking - forloop
mylist = [(1,2),(3,4),(5,6),(7,8)]
for item in mylist:
    print(item)

for (a,b) in mylist: #this is tuple unpacking
    print(a)
    print(b)

    # Dictionary-forloop
d ={'k1': 1, 'k2': 2, 'k3':3}
for i in d:
    print(i)

d ={'k1': 1, 'k2': 2, 'k3':3}
for i in d.items(): # print the key and value in toople this is same as touple unpacking.
    print(i)
for k,v in d.items(): # only print the key
    print(k)
for k,v in d.items(): # only print the value
    print(v)
