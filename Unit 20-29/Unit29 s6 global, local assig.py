# Nested statements and Scope

"""Important to understand how Python deals with the variable names you assign when you create a variable name in Python.
That name is stored in what's called the namespace, and variable names also have a scope.
The scope determines the visibility of that variable name to other parts of your code."""

x = 25
def printer():
    x = 50 
    return x
print (x) #Return 25
print (printer()) #Return 50 
    
# The idea of scope allows Python to understand and have a set of rules to decide which variables you're referencing in your code.
# The rules are L.E.G.B Rule:
    # L : Local - Names assigned in any way within a function (def or lambda), and not declared global in that function.
    # E : Enclosing function locals - Names in the local scope of any and all enclosing function locals (def of lambda), from inner to outer.
    # G : Global (Module) - Names assigned at the top-level of a module file, or declared global in a def within the file.
    # B : Build-in (Python) - Names preassigned in the build-in names module: open,range, syntaxError,...

# lambda num: num**2
    # first num is local dor this function


name = 'THIS IS A GLOBAL STRING' # Global
def greet():
    name = 'Sammy' # Endclosing
    def hello():
        name = 'I AM LOCAL' # Local
        print('Hello '+ name) 
    hello()
greet()

# local variables as well as the global keyword.
x=50
def func():
    global x 
    print (f'x is {x}')
    
    # LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x = 'NEW VALUE' 
    print (f'I JUST CHANGED GLOBAL X TO {x}')

print(x) 
func()
print(x)