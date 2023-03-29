import pygame

class Alien:
    def __init__(self, m, x, y):
        self.settings = m.settings
        self.screen = m.screen
        self.alien = self.settings.alien
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.alien)

    def draw_alien(self):
        self.screen.blit(self.alien, (self.x, self.y))
    
    def move_alien(self):
        self.x += self.settings.alien_speed*self.settings.fleet_direction

    def check_edges(self):
        if self.x <=0 or self.x >= (self.settings.screen_width - self.settings.alien_width):
            return True

