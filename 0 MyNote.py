## NOTE: regular expresion/ regex


#NOTE: Operators 
    # //=   purpose: divide,floor,and assign
num = 12
num //= 2
print(num)
    # **=   purpose: raise power and assign
num = 2
num **= 2
print (num)
    # |=    purpose: or and assign 
num = 5
num |= 3
print(num)
    # ^=    purpose: XOR and assign
num = 3
num ^= 6
print (num)
    # >>=   purpose: right-shift and assign
num = 6
num >>= 3
print (num)
    # <<=   purpose: left-shift and assign
num = 6
num <<= 3
print (num)

# operator  purpose  notation
# &	    Bitwise AND 	In-fix
# |	    Bitwise OR	    In-fix
# ^	    Bitwise XOR	    In-fix
# ~	    Bitwise NOT	    Prefix
# <<	Shift Bits Left	    In-fix
# >>	Shift Bits Right	In-fix

num1 = 10  # Binary value = 01010
num2 = 20  # Binary Value = 10100

print(num1 & num2)  # 00000
print(num1 | num2)  # 11110
print(num1 ^ num2)  # 11110
print(~num1)  # 1111 0101
print(num1 << 3)  # 0101 0000
print(num2 >> 3)  # 0010


# NOTE: you can't make 2 retrun in 1 def 
# def1 and def2 

# NOTE: Print and Retrun 
# Imagine 