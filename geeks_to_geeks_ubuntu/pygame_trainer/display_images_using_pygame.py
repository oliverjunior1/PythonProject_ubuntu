# image (125,125)
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))
image = pygame.image.load('SONIC.jpeg')

while True:
    screen.blit(image,(125,125))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()