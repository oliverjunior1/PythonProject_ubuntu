# two screens

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'red', (50,50,30,30))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()