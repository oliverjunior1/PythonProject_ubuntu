import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))

# draw
draw = pygame.draw.rect(screen, 'red', (50,50,40,40))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the light of the World!', True, 'pink')
text_rect = text.get_rect()
text_rect.center=(250,250)

while True:
    screen.blit(text, text_rect)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_0:
                screen.fill('lightblue')
            if event.key==pygame.K_1:
                screen.fill('white')
    pygame.display.flip()