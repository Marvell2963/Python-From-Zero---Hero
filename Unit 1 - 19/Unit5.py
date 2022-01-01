# String properties and methods
    # You can't change the string because string is immutable
        # Example: 
name = "sam"
        # if you want to change sam to pam
        # you can't make it like this name[0] = 'p'
name[1:3]
"p"+name[1:3]

    # string combine with another string 
x = 'hello world'
x + ' today is a beautifulday'

    # you can make string to multiple
word = 'hello '
word*3

    # NOTE:
        # Special things in python you can combine two or more number without calculate the numbers by make it as a string 
        # 2 + 3 = 5
        # '2' + '3' = '23'

    # The attributes and methods that are available on string object
    # Build-in Functions in python are only give you the result without changing the original function

    # using .upper and become 'HELLO WORLD'
x = 'hello world'
x.upper()
    # using .lower and become 'hello world'
z = 'HELLO WORLD'
z.lower()
    # using .split and become ['hello','world'] You can split the in the word l
y = 'Hello World'
y.split()
    # Split in some words
y = 'Hello World'
y.split('l')