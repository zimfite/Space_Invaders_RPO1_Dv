import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/m.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y += self.speed  