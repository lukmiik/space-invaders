import pygame

class Settings:
    def __init__(self, difficulty):
        if difficulty == "easy":
            self.easy()
        elif difficulty == "medium":
            self.medium()
        elif difficulty == "hard":
            self.hard()
        #screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.fps = 60
        #images
        self.bg = pygame.transform.scale(pygame.image.load("assets/bg.jpg"), (self.screen_width, self.screen_height))
        self.heart = pygame.transform.scale(pygame.image.load("assets/heart.png"), ((self.screen_width//20, self.screen_height//20)))
        self.ship = pygame.transform.scale(pygame.image.load("assets/space_ship.png"), ((50,85)))
        self.bullet = pygame.image.load("assets/bullet.png")
        self.alien = pygame.transform.scale(pygame.image.load("assets/alien.png"),(50,55))
        #font
        pygame.font.init()
        self.font = 'Tahoma'
        self.font_size = 50
        self.font_color = (255,255,255)
        #sounds
        pygame.mixer.init()
        self.bullet_sound = pygame.mixer.Sound("assets/laser.ogg")
        pygame.mixer.Sound.set_volume(self.bullet_sound, 0.1)
        #ship
        self.ship_speed = 5
        self.bullet_speed = 5
        self.max_bullets = 3
        #stats
        self.lives = 3
        self.score = 0 
        self.level = 1
        #aliens
        self.alien_width = self.alien.get_width()
        self.alien_height = self.alien.get_height()
        self.number_of_aliens_rows = 4
        self.number_of_aliens_col = self.screen_width//(self.alien_width+20)
        self.fleet_direction =1
        self.aliens_lvl_up = 0.5
        #button
        self.button_color = (0,0,50)

    def easy(self):       
        self.alien_speed =1
        self.alien_drop_speed = 10

    def medium(self):       
        self.alien_speed =2
        self.alien_drop_speed = 10

    def hard(self):       
        self.alien_speed =3
        self.alien_drop_speed = 10

