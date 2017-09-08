import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def runGame():
    pygame.init() #Initialize the screen and background
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion " + ai_settings.author + ai_settings.version)
    ship = Ship(ai_settings, screen)
    #Group/List to store bullets already fired
    bullets = Group()

    # Main loop for game
    while True:
        #Check every keystroke
        ship.update() #Updata the screen for
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        gf.check_events(ai_settings, screen, ship, bullets)
        for event in pygame.event.get():
            screen.fill(ai_settings.color)
            ship.blitm()
            pygame.display.flip()

runGame()