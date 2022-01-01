# Lists / Array(Java language)
    # List ar ordered sequences that can hold a variety of object types.
    # They can use [] brackets and commas to seperate objects in the list.
        # [1,2,3]
    # List support indexing and slicing. 
    # List can be nested and also have a variety of useful methods that can be called off of them.
    
my_list = [1,2,3]
my_list = ['STRING',100,32.2]

    # len() is to count how long is the list or count the index
len(my_list)

    # Indexing
my_list = ['one','two','three']
        # Get all of the item in list including the breakets
my_list
        # Get the item in the first index
my_list[0]
        # Get the item start from second index 
my_list[1:]
        # Combine another list
mylist = ['four','five']
new_list = my_list+mylist

    # Buildin function in the list
        # 1.add and dele.
new_list.append('six')
new_list
new_list.append('seven')
new_list
new_list.pop()
new_list
        # 2.make the list in order.

list1 = ['a','c','g','b','e']
list1.sort()
list1
        # 3.reverse the list.
a = [1,2,3,4,5]
a.reverse()
a