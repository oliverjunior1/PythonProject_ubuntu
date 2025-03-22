import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200,500))

# draw
draw = pygame.draw.rect(screen, 'red', (50,50,30,30))

# text
font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Jesus is the Lord of the lords, and the king of the kings!', True, 'pink')
text_rect = text.get_rect()
text_rect.center=(600,200)

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
                screen.fill('gray')
    pygame.display.flip()
