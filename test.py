import pygame
from random import randint
pygame.init()

screen = pygame.display.set_mode((500, 500))


color = (255, 255, 255)
trigger = False

run = True
while run:

    K = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    if K[pygame.K_SPACE] and not trigger:
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        trigger = True
    if not K[pygame.K_SPACE]:
        trigger = False
    
    screen.fill(color)

    pygame.display.update()
pygame.quit()