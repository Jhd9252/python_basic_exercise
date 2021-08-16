#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Bouncing Ball Animation
Created on Sun Jun  7 01:01:37 2020
Purpose: learning PyGame
@author: Jonathan
"""
import sys 
import pygame
pygame.init()

size = width, height = 900,500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

peepa = pygame.image.load("peepa.png")
peeparect = peepa.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    peeparect = peeparect.move(speed)
    if peeparect.left < 0 or peeparect.right > width:
        speed[0] = -speed[0]
    if peeparect.top < 0 or peeparect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(peepa, peeparect)
    pygame.display.flip()
