import random
from constants import *
import math


def special_fish_generator():
    fish_y = random.randint(0, 4*HEIGHT)

    side = random.randint(1, 2)
    # 1 is left, 2 is right

    if side == 1:
        fish_x = random.randint(-SPECIAL_FISH_WIDTH - 100, -SPECIAL_FISH_WIDTH)
        fish = pygame.Rect(fish_x, fish_y, SPECIAL_FISH_WIDTH, SPECIAL_FISH_HEIGHT)
        special_fish_left.append(fish)

    else:
        fish_x = random.randint(WIDTH, WIDTH+100)
        fish = pygame.Rect(fish_x, fish_y, SPECIAL_FISH_WIDTH, SPECIAL_FISH_HEIGHT)
        special_fish_right.append(fish)


def special_fish_movement():
    for fish in special_fish_left:
        if calculate_radius_special_fish(fish):
            fish.x += SPECIAL_VEL_PLAYER_SPOTTED
            if fish.y > HEIGHT / 2:
                fish.y += SPECIAL_VEL_PLAYER_SPOTTED
            else:
                fish.y -= SPECIAL_VEL_PLAYER_SPOTTED
        fish.x += SPECIAL_FISH_VEL
        if fish.x > WIDTH + 50:
            special_fish_left.remove(fish)
    for fish in special_fish_right:
        if calculate_radius_special_fish(fish):
            fish.x -= SPECIAL_VEL_PLAYER_SPOTTED
            if fish.y > HEIGHT / 2:
                fish.y += SPECIAL_VEL_PLAYER_SPOTTED
            else:
                fish.y -= SPECIAL_VEL_PLAYER_SPOTTED
        fish.x += SPECIAL_FISH_VEL
        if fish.x < -50:
            special_fish_right.remove(fish)


def calculate_radius_special_fish(special_fish):
    x = abs(special_fish.x - WIDTH/2)
    y = abs(special_fish.y - HEIGHT/2)
    r = math.sqrt(x*x + y*y)
    if r <= SPECIAL_FISH_RADIUS:
        return True
    else:
        return False