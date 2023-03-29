import pygame
from bullet import Bullet
import asyncio

class Ship:
    def __init__(self, m):
        self.screen = m.screen
        self.settings = m.settings
        self.ship = self.settings.ship
        self.ship_width = self.ship.get_width()
        self.ship_height = self.ship.get_height()
        self.x = self.settings.screen_width/2 - self.ship_width/2
        self.y = self.settings.screen_height - 20 - self.ship_height
        self.shot_bullets = 0
        self.bullets = []
        self.mask = pygame.mask.from_surface(self.ship)
        
    def draw_ship(self):
        self.screen.blit(self.ship, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw()

    def move_ship(self):
        #dictionary of all the pressed keys
        pressed_keys = pygame.key.get_pressed()
        if (pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]) and self.x - self.settings.ship_speed >0:
            self.x -= self.settings.ship_speed
        if (pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]) and self.x + self.settings.ship_speed +self.ship_width<self.settings.screen_width:
            self.x += self.settings.ship_speed

    def move_bullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.y <0:
                self.bullets.remove(bullet)

    def main(self):
        self.draw_ship()
        self.move_ship()
        self.move_bullet() 
    
        
