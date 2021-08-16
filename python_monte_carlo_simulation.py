# -*- coding: utf-8 -*-
"""


Created on Wed Sep 30 21:44:07 2020


Modern Art Monte Carlo Simulation
    a. playing field is 800 wide and 500 high. origin is top left.
    b. get user input on total throws. validate positive
    b. generate random point
    c. if in red, if yellow, if green, if blue, if green and blue, if black or miss
    d. count results, format, display
"""
# imports
import math
import random
import time

# initialize/assign vars
start = time.perf_counter()
total_throws = 0
red = 0
green = 0
blue = 0
grey = 0
black = 0
yellow = 0
misses = 0


def in_circle(x1, y1, x2, y2, radius):
    """in_circle func for repeated use with green, blue, grey, black"""
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2) < radius


def distance(x1, y1, x2, y2):
    """distance func for use with black circle"""
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# red area point range
redx = [50, 100]
redy = [50, 450]

# yellow area (split into 3) point ranges
y1x = [600, 650]
y1y = [50, 400]
y2x = [650, 750]
y2y = [50, 100]
y3x = [700, 750]
y3y = [100, 400]

# grey is in green and blue, elif green, elif blue
# green area. center is (300,150), radius is 100
# blue area. center is (450,150), radius of circle is 100
# if dist of rand(x,y) to center(x,y) < radius, then in circle
green_x = 300
green_y = 150
green_radius = 100
blue_x = 450
blue_y = 150
blue_radius = 100

# black center is (375,375), full radius is 75, white  radius is 25
# if dist rand(x,y) to white center < black radius
# if dist greater than 25:
# then black +=1
black_x = 375
black_y = 375
black_radius = 75
white_radius = 25

# get input on number of throws
while True:
    total_throws = int(input('Number of throws: '))
    if total_throws > 0:
        break
    else:
        print('Invalid, try again!', end='')
        continue

# for loop (known # of iterations), generate random(x,y), determine hit/miss
for num in range(1, total_throws + 1):
    pointx = random.uniform(0, 800)
    pointy = random.uniform(0, 500)

    if (pointx >= redx[0] and pointx <= redx[1]) and (pointy >= redy[0] and pointy <= redy[1]):
        red += 1

    elif (pointx >= y1x[0] and pointx <= y1x[1]) and (pointy >= y1y[0] and pointy <= y1y[1]):
        yellow += 1

    elif (pointx >= y2x[0] and pointx <= y2x[1]) and (pointy >= y2y[0] and pointy <= y2y[1]):
        yellow += 1

    elif (pointx >= y3x[0] and pointx <= y3x[1]) and (pointy >= y3y[0] and pointy <= y3y[1]):
        yellow += 1

    elif in_circle(pointx, pointy, green_x, green_y, green_radius) and in_circle(pointx, pointy, blue_x, blue_y, blue_radius):
        grey += 1

    elif in_circle(pointx, pointy, green_x, green_y, green_radius):
        green += 1

    elif in_circle(pointx, pointy, blue_x, blue_y, blue_radius):
        blue += 1

    elif in_circle(pointx, pointy, black_x, black_y, black_radius):

        if distance(pointx, pointy, black_x, black_y) > 25:
            black += 1

    else:
        misses += 1

end = time.perf_counter()
print('Total time elapsed: {:.2f} seconds'.format(end - start), end='\n' * 2)

# format results and display
colors = ['Red:', 'Green:', 'Blue:', 'Grey:', 'Black:', 'Yellow:', 'Misses:']
results = [red, green, blue, grey, black, yellow, misses]
percent_results = [format(x / total_throws, '.2%') for x in results]
for x, y, z in zip(colors, results, percent_results):
    print('{:<15}'.format(x), '{:>10,}'.format(y), '({})'.format(z))









