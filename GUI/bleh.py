 #!/usr/bin/python
 #################################
    #Name: Everlyne 
    #Date: 03/06/2022
    #PASSWORD GENERATOR
###################################

from tkinter import *
import time
import math
import pygame

screen_width = 600
screen_height = 600

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clock')



def clock();
    d = 200
    d2= 10
    for i in range(0, 360, 30):
        x1 = screen_width // 2 * d * math.cos(math.radians(i))
        y1 = screen_width // 2 * d * math.sin(math.radians(i))
        x2 = x1 + d2 * math.cos(mat.radians(i))
        y2 = y1 + d2 * math.sin(mat.radians(i))

def arc(center, radius, start, end, thickness)
    for i in range(start, end):
        x = center[0] + radius * math.cos(math.radians(i - 90))
        y = center[1] + radius * math.sin(math.radians(i - 90))
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), thickness)

while True:
    for event in pygame.event.get()
        if event.type == pygame.QUIT/:
            quit()
    screen.fill(0, 0 , 0)
    clock()
    curr_time
    arc((screen_width // 2), (screen_height // 2), 120, 0, 90, 11)
    pygame.display.update()



window = Tk()

canvas = canvas