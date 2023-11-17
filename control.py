import pygame
import sys
import os
from  bullet import Bullet
from  enemy import Enemy

def events(hero, screen, bullets):
    
    for event in pygame.event.get():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        hero.move_right = True
                    if event.key == pygame.K_LEFT:
                        hero.move_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        hero.move_right = False
                    if event.key == pygame.K_LEFT:
                        hero.move_left = False


def update(screen, hero, bullets, enemys):
    screen.blit(pygame.image.load(os.path.join('img/space.jpg')), (-100, 100))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.output_hero()
    enemys.output_enemy()
    pygame.display.flip()
    
def moving_bullets(screen, bullets, enemys):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisious = pygame.sprite.groupcollide(bullets, enemys, True, True) 

def create_army(screen):
    enemy = Enemy(screen)
    enemy_wight = enemy.rect.width

    num_enemy_x = int(600)