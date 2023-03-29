import pygame
import sys
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
import asyncio

class Game:
    def __init__(self, difficulty):
        self.settings = Settings(difficulty)       
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.fleet = []

    def create_fleet(self):
        for i in range(self.settings.number_of_aliens_rows):
            for j in range(self.settings.number_of_aliens_col):
                self.fleet.append(Alien(self, 20 + 20*j + self.settings.alien_width*j, 80 + 20*i + self.settings.alien_height*i ))

    def draw_fleet(self):
        for alien in self.fleet:
            alien.draw_alien()

    def drop_fleet(self):
        for alien in self.fleet:
            alien.y += self.settings.alien_drop_speed

    def check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self.settings.fleet_direction *=-1
                self.drop_fleet()
                return
    
    def move_fleet(self):
        for alien in self.fleet:
            alien.move_alien()

    def check_collision(self, img1, img2):
        offset_x = img2.x - img1.x
        offset_y = img2.y - img1.y
        return img1.mask.overlap(img2.mask, (int(offset_x), int(offset_y))) != None
    
    def check_ship_alien_col(self):
        for alien in self.fleet:
            if self.check_collision(self.ship, alien) or (alien.y 
                + self.settings.alien_height)>self.settings.screen_height:
                self.settings.lives -=1
                self.fleet.remove(alien)
            if self.settings.lives == 0:
                return True
            
    def check_bullet_alien_col(self):
        for alien in self.fleet:
            for bullet in self.ship.bullets:
                if self.check_collision( alien, bullet) or bullet.y<0:
                    self.ship.bullets.remove(bullet)
                    self.fleet.remove(alien)
                    self.settings.score +=1
            
    # draw the lives that are left
    def draw_lives(self):
        for i in range(self.settings.lives):
            self.screen.blit(self.settings.heart, (10+ 10*i+self.settings.heart.get_width()*i,15))

    def draw_score(self):
        font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        score = font.render(f"Score: {self.settings.score}", True, self.settings.font_color)
        self.screen.blit(score, (self.settings.screen_width - score.get_width()-50, 5))

    def draw_level(self):
        font = pygame.font.SysFont(self.settings.font, self.settings.font_size, bold=True)
        level = font.render(f"{self.settings.level}", True, self.settings.font_color)
        self.screen.blit(level, (self.settings.screen_width/2 - level.get_width()/2, 5))
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    
            #shoot bullet
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(self.ship.bullets)<self.settings.max_bullets:
                    self.ship.bullets.append(Bullet(self, self.ship.x+ self.ship.ship_width/2, self.ship.y)) 
                    pygame.mixer.Sound.play(self.settings.bullet_sound)

    def check_fleet_is_empty(self):
        if not self.fleet:
            self.create_fleet()  
            self.ship.bullets.clear()
            self.settings.alien_speed += self.settings.aliens_lvl_up 
            self.settings.level +=1

    def draw_stats(self):
        self.screen.blit(self.settings.bg, (0,0))  
        self.draw_lives()
        self.draw_score()
        self.draw_level()

    def fleet_functions(self):
        self.draw_fleet()
        self.move_fleet() 
        self.check_fleet_edges()

    def check_collisions(self):
        self.check_bullet_alien_col()                                      
        if self.check_ship_alien_col():
            return True

    async def main(self):
        running = True
        clock = pygame.time.Clock()
        self.create_fleet()
        while running:
            clock.tick(self.settings.fps)
            self.check_events()
            self.check_fleet_is_empty()
            self.draw_stats()
            self.fleet_functions()
            self.ship.main() 
            if self.check_collisions():
                running = False
            pygame.display.update()
            await asyncio.sleep(0)
  