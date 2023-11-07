import pygame, control
from hero import Hero
from pygame.sprite import Group


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Самая лучшая игра")

    hero = Hero(screen)
    
    bullets = Group()
    enemys = Group()
    
    flag = True
    while flag:
        control.events(screen, hero, bullets)
        hero.moving_hero(screen)
        
        control.moving_bullets(screen, bullets)
        #control.create_army(screen)
        control.update(screen, hero, bullets, enemys)

start_game()