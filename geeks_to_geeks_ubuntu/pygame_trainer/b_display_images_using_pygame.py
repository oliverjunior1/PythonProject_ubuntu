# image (150,150)
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
image = pygame.image.load('SONIC.jpeg')

while True:
    screen.blit(image, (150,150))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()