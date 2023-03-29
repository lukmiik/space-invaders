import pygame

class Bullet:
    def __init__(self, m, x, y):
        self.settings = m.settings
        self.bullet = self.settings.bullet
        self.screen = m.screen
        self.x = x - self.bullet.get_width()/2
        self.y = y
        self.mask = pygame.mask.from_surface(self.bullet)
        
    def draw(self):
        self.screen.blit(self.bullet, (self.x, self.y))

    def move(self):
        self.y -= self.settings.bullet_speed