from constants import *

player_x = WIDTH // 2
player_y = HEIGHT // 2


def detect_collision(player_health, player_rect):
    ret = 1

    for fish in fishes_left:
        if player_rect.colliderect(fish):
            player_health -= 1
            fishes_left.remove(fish)
            if player_health <= 0:
                ret = 3
    
    for fish in fishes_right:
        if player_rect.colliderect(fish):
            player_health -= 1
            fishes_right.remove(fish)
            if player_health <= 0:
                ret = 3

    for hostile_fish in hostile_fishes_left:
        if player_rect.colliderect(hostile_fish):
            player_health -= 2
            hostile_fishes_left.remove(hostile_fish)
            if player_health <= 0:
                ret = 3

    for hostile_fish in hostile_fishes_right:
        if player_rect.colliderect(hostile_fish):
            player_health -= 2
            hostile_fishes_right.remove(hostile_fish)
            if player_health <= 0:
                ret = 3

    for fish in unspecial_fish_left:
        if player_rect.colliderect(fish):
            player_health -= 1
            unspecial_fish_left.remove(fish)
            if player_health <= 0:
                ret = 3
    
    for fish in unspecial_fish_right:
        if player_rect.colliderect(fish):
            player_health -= 1
            unspecial_fish_right.remove(fish)
            if player_health <= 0:
                ret = 3
    
    return player_health, ret

