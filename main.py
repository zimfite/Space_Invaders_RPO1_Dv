import pygame
import sys
from hero import Hero

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Самая лучшая игра")

    #объекты классов
    hero = Hero(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hero.rect.centerx += 10
                if event.key == pygame.K_a:
                    hero.rect.centerx -= 10

        pygame.display.flip()
        screen.fill(0)
        hero.output_hero()

start_game()
