# chaining comparison operators in python with logical operators
    # we can use logical operators to combine comparisons: 
        # and / or / not

# and   need both of them to be true else false
1<2<3
1<2 and 2<3 

1<2>3
1<2 and 2>3

'h' == 'h' and 2==2 and ('h' == 'h') and (2==2)
'h' == 'H' and 2==3 and ('h' == 'H') and (2==3)

# or    only need one of them is true 
1 < 2 or 2>3
1 > 2 or 2>3

10 == 1 or 2==2
10 == 1 or 2==20

# not   return the opposite boolean
not 1==2 and not (1==2)
not 1==1 and not (1==1)

not 'hi' == 'world' 

# NOTE:
    # recommend to use comparison operators insted of direct code
        # 1<2 and 2<3  ---> good 
        # 1<2<3        ---> bad 
    # we always want to stress readability in our code, we want to be able to easily read the code.