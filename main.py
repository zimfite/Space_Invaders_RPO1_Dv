import pygame
import sys
import os
from hero import Hero

def start_game():
    pygame.init()
    w = 600
    h = 600
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((w,h))
    pygame.display.set_caption('Самая лучшая игра')

    left_wall = pygame.Rect(0, 0, 10, h)
    right_wall = pygame.Rect(w - 10, 0, 10, h)

    hero = Hero(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.blit(pygame.image.load(os.path.join('img/o.jpg')), (-50, 0))

        pygame.draw.rect(screen, (0, 0, 0), left_wall)
        pygame.draw.rect(screen, (0, 0, 0), right_wall)
        hero.output_hero()
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            hero.rect.centerx -= 5
        elif keys[pygame.K_d]:
            hero.rect.centerx += 5
        
        if hero.rect.centerx < left_wall.right:
            hero.rect.centerx = left_wall.right
        elif hero.rect.centerx > right_wall.left:
            hero.rect.centerx = right_wall.left

        clock.tick(60)

start_game()
