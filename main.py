from draw_function import *
from collision import *
from camera_movement import *
from cutscene1 import *
from cutscene2 import *
from fish import *
from hostile_fish import *
from screenshot import *
from unspecial_fish import *
# from constants import *
from sys import exit

pygame.init()

pygame.display.set_caption('Secrets of The Deep')

clock = pygame.time.Clock()

player_surf = pygame.transform.scale(
    pygame.image.load('Player/diver.webp').convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))


def main():
    player_look = 1

    fish_timer = 0
    hostile_fish_timer = 0
    special_fish_timer = 0

    add_fish = 500
    add_hostile_fish = 2000
    add_special_fish = 500

    player_health = 7

    points = 0

    game_active = 0
    # 0 - main menu
    # 1 - gameplay
    # 2 - controls
    # 3 - death menu

    depth_pixels = 500  # 50 pixels = 1 meter

    # draw_cutscene1(WINDOW)
    # draw_cutscene2(WINDOW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                points += capture_fish()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_active == 1:
            h = clock.tick(FPS)
            fish_timer += h
            hostile_fish_timer += h
            special_fish_timer += h

            if fish_timer > add_fish:
                fish_generator()
                fish_timer = 0

            if hostile_fish_timer > add_hostile_fish:
                hostile_fish_generator()
                hostile_fish_timer = 0

            if special_fish_timer > add_special_fish:
                special_fish_generator()
                special_fish_timer = 0

            fish_movement()
            hostile_fish_movement()
            special_fish_movement()
            unspecial_fish_movement()

            depth_pixels, player_look = player_movement(depth_pixels, player_look)

            player_health, game_active = detect_collision(player_health, player_rect)

            draw(WINDOW, player_health, round(depth_pixels/50), points, player_surf, player_rect, player_look)

        elif game_active == 0:
            game_active = start_screen(WINDOW)

        elif game_active == 2:
            game_active = controls_menu(WINDOW)

        elif game_active == 3:
            game_active = death_screen(WINDOW, round(depth_pixels/50), points)

        elif game_active >= 4:
            fishes_right.clear()
            fishes_left.clear()

            special_fish_right.clear()
            special_fish_left.clear()

            unspecial_fish_left.clear()
            unspecial_fish_right.clear()

            hostile_fishes_right.clear()
            hostile_fishes_left.clear()

            fish_timer = 0
            hostile_fish_timer = 0
            special_fish_timer = 0

            add_fish = 500
            add_hostile_fish = 2000
            add_special_fish = 500

            player_health = 7

            points = 0

            if game_active == 5:
                game_active = 0
            else:
                game_active = 1

            depth_pixels = 500


if __name__ == '__main__':
    main()
