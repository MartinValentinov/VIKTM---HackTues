from constants import *

clock3 = pygame.time.Clock()

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)

player_surf = pygame.image.load('Player/vodolaz1.webp').convert_alpha()
player_surf = pygame.transform.rotozoom(player_surf, 0, 0.8)
player_rect = player_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
player_diving_surf = pygame.image.load('Player/diver.webp').convert_alpha()
player_diving_surf = pygame.transform.rotozoom(player_diving_surf, 0, 0.8)
player_diving_rect = player_diving_surf.get_rect()


def draw_cutscene2(window):
    golden_fish_surf = pygame.image.load('Golden_fish/golden_fish.png').convert_alpha()
    golden_fish_surf = pygame.transform.rotozoom(golden_fish_surf, 0, 0.5)
    golden_fish_surf = pygame.transform.rotate(golden_fish_surf, 90)
    yes = True

    player_y = -100
    golden_fish_y = 100

    while True:
        clock3.tick(FPS)

        window.blit(background_surf, (0, 0))

        if player_y < HEIGHT/2:
            player_y += PLAYER_SPEED
        else:
            if yes:
                golden_fish_surf = pygame.transform.rotate(golden_fish_surf, 180)
                yes = False
            golden_fish_y += SPECIAL_FISH_VEL

        if player_y < HEIGHT/4 + HEIGHT/8 - HEIGHT/16:
            window.blit(pygame.transform.flip(player_surf, 1, 1),
                        (WIDTH/2 - player_rect.width/2, player_y - PLAYER_SPEED/2))
        else:
            window.blit(player_diving_surf, (WIDTH/2 - player_diving_rect.width/2, player_y - PLAYER_SPEED/2))

        window.blit(golden_fish_surf, (WIDTH/2 - GOLDEN_FISH_WIDTH/2 - 30, HEIGHT / 2 + golden_fish_y))

        if golden_fish_y >= HEIGHT + 100:
            break

        pygame.display.update()
