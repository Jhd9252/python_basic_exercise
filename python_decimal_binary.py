# -*- coding: utf-8 -*-
"""

Problem: Decimal to Binary
    a. take input. assume int. validate >= 0. 
    b. use conversion process 
        b1. utilize strings to hold the data
    c. display results
"""

# grab original user input. Assume int. Validate greater >= 0
while True:
    original = int(input('Enter a number greater than or equal to 0: '))
    if original < 0:
        print('Invalid, try again.')
    else:
        break

# create var for binary representation, use str type for concatenation
binary_rep = ''

# create new var, point to same object as original. For end result display
a = original

while True:    
    if a % 2 == 1:
        binary_rep = '1' + binary_rep
        print('{} % 2 = {} --- {}'.format(a, a % 2, binary_rep))
    else:
        binary_rep = '0' + binary_rep
        print('{} % 2 = {} --- {}'.format(a, a % 2, binary_rep))    
    print('{} / 2 = {}'.format(a, a // 2))
    a = a // 2    
    if a == 0:
        print()
        print('{} in binary is {}'. format(original, binary_rep))
        break
    else:
        continue


    



