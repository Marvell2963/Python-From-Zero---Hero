# Touple unpacking with python
    # Functions and returning multiple items from a function with

stock_prices = [("appl",200),("goog",400),("msft",100)]

# For-loop
for item in stock_prices:
    print(item)

for thicker,price in stock_prices:
    print (price+(0.1*price))

# Function
work_hours = [('abby',100),("billy",400),("cassie",800)]
def employee_check(work_hours):
    current_max = 0
    employee_off_month = ""

    # Touple unpacking
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_off_month = employee
        else:
            pass
    # Retrun 
    return (employee_off_month,current_max)

employee_check(work_hours)
    # Return else
result = employee_check(work_hours)
name,hours = employee_check(work_hours)
result # ('cassie', 800)
name #"cassie"
hours # 800