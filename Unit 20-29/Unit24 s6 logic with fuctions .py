# Logic with Python Functions
    
20%2 ==0
21%2 ==0
    # Make function that we can place any number insted of having to manually type in 20 and 21 or we called (brute force)
def even_check(num):
    result = num%2 ==0 # Or we can do like this. return num%2==0 
    return result
even_check(20)
        ## RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

    # Solve for multiple number in list 
def check_even_list(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass # If you put return False # it is WRONG!! 
check_even_list([1,3,5])
# print nothing
check_even_list([2,4,6])
# print True

        # HERE IS WHY IT IS WRONG!
def check_even_list(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            return False
check_even_list([1,2,5]) # It should return True 
# print False  
check_even_list([1,3,5])
# print False 
check_even_list([2,4,6])
# print True

            # To solve it
def check_even_list(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass
    return False
check_even_list([1,2,5]) # It should return True 
# print False  
check_even_list([1,3,5])
# print False 
check_even_list([2,4,6])
# print True


    # Return all the even numbers in a list 
def check_even_list(num_list):
    even_num = []
    for number in num_list:
        if number%2==0:
            even_num.append(number)
        else:
            pass
    return even_num
check_even_list([1,2,3,4,5,6,7,8,9])