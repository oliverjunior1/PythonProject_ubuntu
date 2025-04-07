import pygame
import sys

screen = pygame.display.set_mode((500,500))

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            sys.exit()
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0]<=width/2+140 and height/2 <= mouse[1]<=height/2+40:
                pygame.quit()
    pygame.display.flip()