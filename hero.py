import pygame
class Hero:
  def __init__(self, screen):
    '''инициализация главного героя'''
    self.image = pygame.image.load("img/hero.png")
    self.rect = self.image.get_rect()
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.rect.bottom = self.screen_rect.bottom
    self.rect.centerx = self.screen_rect.centerx
    self.lives = 3
    
  def output_hero(self):
    self.screen.blit(self.image, self.rect)
  def remove_life(self):
      self.lives -= 1

  def get_lives(self):
      return self.lives