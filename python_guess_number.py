#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Wed Sep 23 14:59:17 2020


Problem: Guess the number with 3 Attempts
    a. guess integer between 1-10. Randomly seleted.
    b. allowed to guess 3 times. 
    c. if guessed correctly, they win and game ends.
    d. if the guess incorrectly - declare too high or too low
    e. at then end, display the secret number and the number of guesses it took. 
    *** using only if/elif/else statements. no while or for loops***

"""

# set imports
import random

# set vars
secret_num = random.randint(1,10)
win = False
counter = 0

# print header
print("I'm thinking of a number between 1 and 10!")

# using only if/elif/else statements, create the game


if win == False and counter != 3:
    guess = int(input('What\'s your guess? '))
    if guess == secret_num:
        counter += 1
        win = True
        print('You got it!')
        print('The secret number was {}.'.format(secret_num))
        if counter == 1:
            print('It took you 1 try to guess the number.')
        else:
            print('It took you {} tries to gues the number.'.format(counter))
    elif guess > secret_num:
        counter += 1
        print('Too high, try again.')
    else:
        counter += 1
        print('Too low, try again.')
       

if win == False and counter != 3:
    guess = int(input('What\'s your guess? '))
    if guess == secret_num:
        counter += 1
        win = True
        print('You got it!')
        print('The secret number was {}.'.format(secret_num))
        if counter == 1:
            print('It took you 1 try to guess the number.')
        else:
            print('It took you {} tries to gues the number.'.format(counter))
    elif guess > secret_num:
        counter += 1
        print('Too high, try again.')
    else:
        counter += 1
        print('Too low, try again.')
        

if win == False and counter != 3:
    guess = int(input('What\'s your guess? '))
    if guess == secret_num:
        counter += 1
        win = True
        print('You got it!')
        print('The secret number was {}.'.format(secret_num))
        if counter == 1:
            print('It took you 1 try to guess the number.')
        else:
            print('It took you {} tries to gues the number.'.format(counter))
    else:
        print('The secret number was {}.'.format(secret_num))
        print('You didn\'t guess the number.')
                


        