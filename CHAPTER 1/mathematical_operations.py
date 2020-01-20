#operators in python
''' +,-,*./,% '''

print(4+5+6)
print(3/6) # floating point division
print(6/3)
print(6//3) #integer division
print(3//6)
print(2**3) # power of a number
print(2**0.5) # sqrt of a number
print(round(2**0.5, 4)) # rounding off a number
print(3%2) # Gives reminder
print(2**3/2*6-4*(3-4/2)) 
# precedence rule  $$        ASSOCIATIVITY RULE 
''' 1. PARENTHESE                highest
    2. EXPONENT                  RIGHT to Left
    3. *,/,//.%                  LEFT to RIGHT
    4. +,-                       LEFT to RIGHT
    '''

print((2+5) /2)
# 2+5= 7/2
print((2+3)*5/2%6) # here / and % has same precedence 
#5 * 5 / 2 % 6
# ASSOCIATIVITY RULE is used ---->> Check above table
#25 / 2 % 6
#12.5 % 6
# EXPONENTS
print(2**3**2)  # left to right
# 2**9