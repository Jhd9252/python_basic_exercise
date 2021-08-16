# -*- coding: utf-8 -*-
"""
Project Name: Python Addition Table
Created on Mon Oct 12 19:31:42 2020

"""
# prime_check func
def prime_check(num):
    prime = True
    for a in range(2, num):
        if num % a == 0:
            prime = False
    return prime

# grab user input for lowest num. validate
while True:
    a = int(input('Lowest Number: '))
    if a < 0:
        print('Lowest number must be 0 or greater.')
    else:
        break
 
# grab user input for higher num. validate > lower num 
while True:
    b = int(input('Highest Number: '))
    if b <= a:
        print('Highest number must be larger than lowest number!')
    else:
        break

# bool val for user choice
want_prime = False

# grab user input for if want prime. change bool accordingly
while True:
    answer = input('Would you like to identify Prime numbers in your table? (y/n): ').lower()
    if answer not in ['y','n']:
        print('Invalid command, try again.')
    elif answer == 'y':
        want_prime = True
        break
    else:
        want_prime = False
        break
    
# grab padding var    
pad = len(str(a+b)) + 3

# prefer containers for range(lower, higher)
a_list = [x for x in range(a,b + 1)]
b_list = [x for x in range(a,b + 1)]

print('+'.center(pad, ' '), end = ' ')

# print the x header
for i in a_list:
    print(format(i, '>{}'.format(pad)), end = '')
        
print()
print('-' * pad * (len(a_list) + 1) + '-')


for a in b_list:
    
    #print the y header
    print(format(a, '<{}'.format(pad)), end = '|')
    
    #per y row
    for b in a_list:
        if want_prime:
            result = a+b
            if result != 0 and result != 1:
                if prime_check(result):
                    result = str(result) + 'p'
                    print(format(result, '>{}'.format(pad)), end = '')
                else:
                    print(format(a+b, '>{}'.format(pad)), end = '')
            else:
                print(format(a+b, '>{}'.format(pad)), end = '')
        else:
            print(format(a+b, '>{}'.format(pad)), end = '')
    print()

