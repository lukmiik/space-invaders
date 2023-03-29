import pygame
import sys
from settings import Settings
import asyncio

class Menu:
    def __init__(self):
        self.settings = Settings(None)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
    def create_buttons(self):
        #create
        btn_width = self.settings.screen_width/4
        btn_height = self.settings.screen_height/8
        left = self.settings.screen_width*3/32
        gap = self.settings.screen_width*1/32
        font = pygame.font.SysFont(self.settings.font, self.settings.font_size)
        self.text = font.render("Choose difficulty", True, self.settings.font_color)
        self.text_rect = self.text.get_rect()
        self.easy_rect = pygame.Rect(left, 4*self.settings.screen_height/8, btn_width, btn_height)
        self.easy_text = font.render("Easy", True, self.settings.font_color)
        self.medium_rect = pygame.Rect(left + btn_width + gap, 4*self.settings.screen_height/8, btn_width, btn_height)
        self.medium_text = font.render("Medium", True, self.settings.font_color)
        self.hard_rect = pygame.Rect(left + 2*btn_width + 2*gap, 4*self.settings.screen_height/8, btn_width, btn_height)
        self.hard_text = font.render("Hard", True, self.settings.font_color)
        #draw
        self.screen.blit(self.text, (self.settings.screen_width/2-self.text.get_width()/2,2*self.settings.screen_height/8) )
        pygame.draw.rect(self.screen, self.settings.button_color, self.easy_rect, 50, 50)
        self.screen.blit(self.easy_text, (self.easy_rect.centerx - self.easy_text.get_width()/2,self.easy_rect.centery - self.easy_text.get_height()/2 ))
        pygame.draw.rect(self.screen, self.settings.button_color, self.medium_rect, 50, 50)
        self.screen.blit(self.medium_text, (self.medium_rect.centerx - self.medium_text.get_width()/2,self.medium_rect.centery - self.medium_text.get_height()/2 ))
        pygame.draw.rect(self.screen, self.settings.button_color, self.hard_rect, 50, 50)
        self.screen.blit(self.hard_text, (self.hard_rect.centerx - self.hard_text.get_width()/2,self.hard_rect.centery - self.hard_text.get_height()/2 ))

    async def main(self):
        self.screen.blit(self.settings.bg, (0,0))  
        self.create_buttons()     
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.easy_rect.collidepoint(event.pos):
                        return "easy"
                    elif self.medium_rect.collidepoint(event.pos):
                        return "medium"
                    elif self.hard_rect.collidepoint(event.pos):
                        return "hard"
            pygame.display.update()
            await asyncio.sleep(0)

            
