import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((700,700))

image = pygame.image.load("SONIC.jpeg")
screen.blit(image, (250,250))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()