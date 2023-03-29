import pygame
import sys
from settings import Settings
import asyncio

async def start_screen():
    pygame.init()
    settings = Settings(None)
    pygame.display.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    font = pygame.font.SysFont(settings.font, settings.font_size)
    text = font.render("Click to start", True, settings.font_color)
    screen.blit(text, (settings.screen_width/2-text.get_width()/2, settings.screen_height/2-text.get_height()))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            pygame.display.update()
            await asyncio.sleep(0)
        
          