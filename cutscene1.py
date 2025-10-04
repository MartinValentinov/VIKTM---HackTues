import os

import pygame

from constants import *

welcome_text = pygame.font.Font('Font/PixelScriptRegular-4B83W.ttf', 75)
welcome_surf = welcome_text.render('Secrets of The Deep', False, 'Black')
welcome_rect = welcome_surf.get_rect(center=(WIDTH/2, HEIGHT/2))

background_cutscene1_surf = pygame.transform.scale(
    pygame.image.load(os.path.join('images', 'ocean_background.png')), (WIDTH, HEIGHT))

boat_serf = pygame.image.load(
    os.path.join('images', 'boat.png'))

player_cutscene_down_surf = pygame.image.load('Player/vodolaz2.webp').convert_alpha()
player_cutscene_down_surf = pygame.transform.rotozoom(player_cutscene_down_surf, 0, 0.6)
player_cutscene_up_surf = pygame.image.load('Player/vodolaz1.webp').convert_alpha()
player_cutscene_up_surf = pygame.transform.rotozoom(player_cutscene_up_surf, 0, 0.6)

screen_fade = pygame.Surface((WIDTH, HEIGHT))
screen_fade.fill(BACKGROUND_COLOR)

clock2 = pygame.time.Clock()


def fade(window):
    for alpha in range(0, 300):
        window.fill((255, 255, 255))
        screen_fade.set_alpha(alpha)
        window.blit(screen_fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)


def draw_cutscene1(window):
    boat_width = -200
    while boat_width < WIDTH // 2 - 250:
        clock2.tick(FPS)

        window.blit(background_cutscene1_surf, (0, 0))

        boat_width += BOAT_VEL

        window.blit(boat_serf, (boat_width, HEIGHT - 150))
        window.blit(player_cutscene_down_surf, (boat_width + 70, HEIGHT - 180))

        pygame.display.update()

    player_x = boat_width + 70
    player_y = HEIGHT - 180
    up = True

    while True:
        clock2.tick(FPS)

        window.blit(background_cutscene1_surf, (0, 0))

        if player_y > HEIGHT - 250 and up:
            player_y -= 4
        else:
            up = False
            player_y += 4

        if player_x <= boat_width + 250:
            player_x += 6

        window.blit(boat_serf, (boat_width, HEIGHT - 150))

        if player_x < WIDTH/2:
            window.blit(player_cutscene_up_surf, (player_x, player_y))

        elif player_x >= WIDTH/2:
            window.blit(pygame.transform.flip(player_cutscene_up_surf, 1, 1), (player_x, player_y))

        if player_y > HEIGHT + 150:
            window.blit(welcome_surf, welcome_rect)

        pygame.display.update()

        if player_y > HEIGHT + 1000:
            fade(window)
            break
