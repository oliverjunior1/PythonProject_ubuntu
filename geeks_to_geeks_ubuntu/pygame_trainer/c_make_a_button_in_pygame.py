import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Moving Rectangle')
x = 200
y = 200
width = 10
height = 10
vel = 10


while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    keys = pygame.key.get_pressed()
    pygame.display.flip()