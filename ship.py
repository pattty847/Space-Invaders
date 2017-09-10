import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('/Users/Pat/Downloads/space ship.png')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        # Self moving flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Store decimal values for the ship's center. Due to value being a float and rect attributes
        # store int values
        self.center = float(self.rect.centerx)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self, screen):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_fac
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_fac
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= self.ai_settings.ship_speed_fac
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.ai_settings.ship_speed_fac

    def blitme(self):
        """Draw the ship at the its current location"""
        self.screen.blit(self.image, self.rect)
