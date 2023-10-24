import pygame

class Hero():
    def __init__(self, screen):
        '''инициалиция главного героя - космического корабля'''
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()

