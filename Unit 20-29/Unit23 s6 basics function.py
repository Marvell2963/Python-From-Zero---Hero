# Functions 

    # Can print as many 
def say_hello():
    print("hello")
    print("good")
    print("morning")
say_hello()
        ## If you called without parentheses, it would not going to execute the function. Python will just report back that say hello is a function.


    # Can use fstring 
def say_hello(name):
    print(f"hello {name}")
say_hello("Marvell")
        ## The function would give you an eror if you called without input inside parentheses, because in order to print the fstring needs the name input. 
    
        # To solve it we can make like this: 
def say_hello(name = 'Default'):
    print(f"hello {name}")
say_hello()


    # Multiple input:
def add_num(num1,num2):
    return num1+num2
add_num(10,20)
result = add_num(10,20)
result
    
    

    # INPORTANT NOTE: 
        # return : insted of just printing out the result, is actually going to allow you to save them as a variable

    # COMPARISON BETWEEN PRINT AND RETURN 
def print_result (a,b):
    print(a+b)

def return_result(a,b):
    return a+b

print_result(10,20)
result = print_result(10,20)
result
        # the python would not returning anything because it is not saved. 
        # printing out the output without save it

return_result(10,20)
result = return_result(10,20)
result

        # you can use print and rreturn at the same time but it is not cummon
def myfunc(a,b):
    print(a+b)
    return a+b
result= myfunc(10,20)
result
            ## it is usefull to debugging for bigginer

    # bugs
def sum_numbers(num1,num2):
    return num1+num2
sum_numbers(10,20)
# output 30
sum_numbers("10","20")
# output '1020'
    ## make sure to check the type of the data before returning the result 

