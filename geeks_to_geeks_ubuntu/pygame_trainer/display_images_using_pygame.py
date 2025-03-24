import pygame
import sys

import pygame

screen = pygame.display.set_mode((600,600))
img = pygame.image.load('SONIC.jpeg').convert()
screen.blit(img,(0,0))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()