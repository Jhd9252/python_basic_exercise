# -*- coding: utf-8 -*-
"""
Problem: Roll the Dice
    a. input of dice sides [4,6,8,10,12,20]. Assume int. Validate.
    b. roll dice until snake eyes. Announce each result.
        b1. double roll (2,2)
        b2. high roll (6,6)
        b3. high/low roll (1,6)
        b4. even roll (2,4)
        b5. odd roll (3,5)
        b6. sum value (2 sides add to max side)
        b7. snake eyes
    c. announce how many tries til snake eyes
    d. determine average roll of each result as %. Two deci places.
    e. average roll of die # 1
    f. average roll of die # 2
"""

# imports
import random

# vars / aggregators
total_rolls = 0
total_die1 = 0
total_die2 = 0
dbls = 0
highs = 0
high_low = 0
evens = 0
odds = 0
sum_vals = 0

# Get inputs and validate.
while True:
    sides = int(input('How many sides on your dice (4, 6, 8, 10, 12 20)? '))
    if sides in [4, 6, 8, 10, 12, 20]:
        break
    else:
        print('Invalid size, try again.')
        continue

print()
print('Thanks, here we go!')


# main body. Keep rolling til snake eyes. Track results and aggregators.
while True:
    rand1 = random.randint(1, sides)
    rand2 = random.randint(1, sides)
    total_rolls += 1
    total_die1 += rand1
    total_die2 += rand2

    # if its even
    if rand1 % 2 == 0 and rand2 % 2 == 0:
        evens += 1
        # if its sum and dbl
        if rand1 + rand2 == sides and rand1 == rand2:
            sum_vals += 1
            dbls += 1
            print('Die #1 is *{}* and die #2 is *{}* Evens! Doubles! Sum value is size value!'.format(rand1, rand2))
        # elif sum
        elif rand1 + rand2 == sides:
            sum_vals += 1
            print('Die #1 is *{}* and die #2 is *{}* Evens! Sum value is size value!'.format(rand1, rand2))
        # elif dbl
        elif rand1 == rand2:
            dbls += 1
            # if highs
            if rand1 == sides and rand2 == sides:
                highs += 1
                print('Die #1 is *{}* and die #2 is *{}* Evens! Highs!'.format(rand1, rand2))
            else:
                print('Die #1 is *{}* and die #2 is *{}* Evens! Doubles!'.format(rand1, rand2))
        # else just even
        else:
            print('Die #1 is *{}* and die #2 is *{}* Evens!'.format(rand1, rand2))

    # if its odd
    if rand1 % 2 == 1 and rand2 % 2 == 1:
        odds += 1
        # if sum and dbl
        if rand1 + rand2 == sides and rand1 == rand2:
            sum_vals += 1
            dbls += 1
            print('Die #1 is *{}* and die #2 is *{}* Odds! Doubles! Sum value is size value!'.format(rand1, rand2))
        # elif sum
        elif rand1 + rand2 == sides:
            sum_vals += 1
            print('Die #1 is *{}* and die #2 is *{}* Odds! Sum value is size value!'.format(rand1, rand2))
        # elif dbl
        elif rand1 == rand2:
            dbls += 1
            # if snake eyes
            if rand1 == 1 and rand2 == 1:
                print('Die #1 is *{}* and die #2 is *{}* Odds! Doubles! Snake Eyes!'.format(rand1, rand2))
                break
            else:
                print('Die #1 is *{}* and die #2 is *{}* Odds! Doubles!'.format(rand1, rand2))
        else:
            print('Die #1 is *{}* and die #2 is *{}* Odds!'.format(rand1, rand2))
    # not evens, not odds
    if (rand1 == 1 and rand2 == sides) or (rand1 == sides and rand2 == 1):
        print('Die #1 is *{}* and die #2 is *{}* High / Low!'.format(rand1, rand2))
    else:  # not evens, odds or high and low, then print basic
        print('Die #1 is *{}* and die #2 is *{}*'.format(rand1, rand2))





# determine results
avg_dbls = format(round(dbls / total_rolls, 4), '.2%')
avg_highs = format(round(highs / total_rolls, 4), '.2%')
avg_evens = format(round(evens / total_rolls, 4), '.2%')
avg_odds = format(round(odds / total_rolls, 4), '.2%')
avg_high_lows = format(round(high_low / total_rolls, 4), '.2%')
avg_sum_vals = format(round(sum_vals / total_rolls, 4), '.2%')
avg_die1 = format(round(total_die1 / total_rolls, 2), ',.2f')
avg_die2 = format(round(total_die2 / total_rolls, 2), ',.2f')

# display results
print()
print('You finally got snake eyes on roll # {}'.format(total_rolls))
print('Along the way you rolled DOUBLES {} times. ({} of all rolls were '
      'doubles)'.format(dbls, avg_dbls))
print('Along the way you rolled TWO HIGH VALUES {} times. ({} of all rolls '
      'were two high values)'.format(highs, avg_highs))
print('Along the way you rolled TWO EVENS {} times. ({} of all rolls '
      'were two evens)'.format(evens, avg_evens))
print('Along the way you rolled TWO ODDS {} times. ({} of all rolls '
      'were two odds)'.format(odds, avg_odds))
print('Along the way you rolled TWO HIGH / LOW {} times. ({} of all rolls '
      'were two high / low)'.format(high_low, avg_high_lows))
print('Along the way you rolled A SUM VALUE {} times. ({} of all rolls '
      'were a sum value)'.format(sum_vals, avg_sum_vals))
print('Average roll for die #1: {}'.format(avg_die1))
print('Average roll for die #2: {}'.format(avg_die2))




