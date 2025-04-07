import pygame
import sys

screen = pygame.display.set_mode((500,500))
width = screen.get_width()
height = screen.get_height()
color_dark =  'black'
color_light = 'white'

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            sys.exit()
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0]<=width/2+140 and height/2 <= mouse[1]<=height/2+40:
                pygame.quit()
    screen.fill((60,25,60))
    mouse = pygame.mouse.get_pos()

    if width/2 <= mouse[0]<=width/2+140 and height/2 <= mouse[1] <= height/2+40:
        pygame.draw.rect(screen, color_light,[width/2,140,40])
    else:
        pygame.draw.rect(screen, color_dark,[width/2,140,40])

    screen.blit(text, (width/2+50, height/2))

    pygame.display.flip()