# print formatting with string
    # Often we want to "inject/inseart" a variable into your string for printing. 
        # Exampel:
my_name =  "Marvell"
print ("hello" + my_name)
    # There're multiple ways to format strings for printing variables in them.
    # Known as string interpolation, basically just a fancy way of stick a variable into a string

    # Two methods for this:
        # .format()  method
            # "string here{} then also {}".format('something1','something2')
print ("this is a sttring {}".format('INSERTED'))
            # We can make an order the format based off the index position inside of this format call 
print ('the {2} {1} {0}'.format('fox','brown','quick'))
            # We can repeat the format
print ('the {0} {0} {0}'.format('fox','brown','quick'))
            # We can make a key word for the format that we put
print ('the {a} {b} {c}'.format(a='fox',b='brown',c='quick'))
            # Float formatting follows "{value:width.precision f}"
                # Passing the value
                # Width : add in some withspace if you have a really large value
                # Presition f:  decimal number  
result = 1/7
result
print ("The result was {r:1.4f}".format(r=result))
print ("The result was {r:10.4f}".format(r=result))
        # f-string(formatted string literals)
            # The simplest way of .format()
            # Basicly allows you to do is skip .format() and directly inside the string {}
name = 'Marrvell'
print(f'Hello, my name is {name}')
            # more function
name = 'Marvell'
age = 20
print(f'{name} is {age} years old')