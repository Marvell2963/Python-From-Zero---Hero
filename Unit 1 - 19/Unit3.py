# Variable assignments
    # Rules for varialble names: 
        # 1. Names can't start with a number
1#111='this is wrong'
        # 2. There can be no spaces in the name, use underline(_) instead 
#hi world = 'this wrong is wrong'
hi_world = 'hi'
        # 3. Can't use any of this symbols ' " , < > / ? \ | ( )! @ # $ % ^ & * _ + :
#/]! = ' this wrong is wrong'
        # 4. It's considered best practice (PEP8) that names are lowercase 
hello='this is correct'
        # 5. Avoid using words that have special meaning in Python like "list" and "str"
list= 'can not do this'
Arr= 'acceptable'
    # Python use Dynamic Typing.
        # It means you can reassign variable to different data types and make python very flexible in assigning data types
        # the other languages use "Statically-typed"

    # in python you can do like this, but eror in other languages 
        # my_dogs = 2
        # my_dogs = ["Sammy","Frankie"]

    # Pros and Cons of Dynamic Typing:
        # pros: very easy to work with, faster development time 
        # Cons: many result in bugs for unexpected data types, you need to be aware of type() 
