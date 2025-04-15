import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))
x = 300
y = 400

draw = pygame.draw.rect(screen, 'red', (x,y,30,30))


while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_0:
                x = 300
                y = 500
    pygame.display.flip()