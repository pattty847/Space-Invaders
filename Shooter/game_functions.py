import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
            print("System exit")

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
            print("Right")
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
            print("Left")
        elif event.key == pygame.K_UP:
            ship.moving_up = True
            print("Up")
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
            print("Down")
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
        elif event.key == pygame.KMOD_ALT:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
            bullets.check_gun_state = True

def check_keyup_events(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
            print("Left")
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
            print("Right")
        elif event.key == pygame.K_UP:
            ship.moving_up = False
            print("Up")
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False
            print("Down")


def check_events(ai_settings, screen, ship, bullet):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullet)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.color)
    ship.blitm()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # make the most recently drawn screen visible.
    pygame.display.flip()