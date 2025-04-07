import pygame
import sys

screen = pygame.display.set_mode((500,500))

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            sys.exit()
            pygame.quit()
    pygame.display.flip()