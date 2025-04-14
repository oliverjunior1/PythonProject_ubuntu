import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Moving Rectangle')
x = 200
y = 220
width = 100
height = 50
vel = 10

# text

font = pygame.font.SysFont('Times New Roman', 25)
text = font.render('Exit', 'True', 'red')
text_rect = text.get_rect()
text_rect.center=(250,250)

# rect
rect = pygame.draw.rect(screen, 'blue', (x, y, width, height))

while True:
    screen.blit(text, text_rect)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel

    pygame.display.flip()