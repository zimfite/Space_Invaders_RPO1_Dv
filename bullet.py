import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self, screen, hero,):
        super(bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.rect(0,0,4,12)
        self.color = 0, 255, 255
        self.speed = 4.5
        self.rect.centerx = hero.rect.centrex
        self.y = float(self.rect.y)

    def update_bullet(self):
        pygame.draw_bullet.rect(self.screen, self.color, self.rect)
        self.y-=self.speed
        self.rect.y=self.y