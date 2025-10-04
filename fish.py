import random
from constants import *


def fish_generator():
    for i in range(0, 3):
        fish_y = random.randint(0, 4*HEIGHT)

        side = random.randint(1, 2)
        # 1 is left, 2 is right

        if side == 1:
            fish_x = random.randint(-FISH_WIDTH-100, -FISH_WIDTH)
            fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH, FISH_HEIGHT)
            fishes_left.append(fish)
        else:
            fish_x = random.randint(WIDTH, WIDTH+100)
            fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH, FISH_HEIGHT)
            fishes_right.append(fish)


def fish_movement():
    for fish in fishes_left:
        fish.x += FISH_VEL
        if fish.x > WIDTH and fish:
            fishes_left.remove(fish)
    for fish in fishes_right:
        fish.x -= FISH_VEL
        if fish.x < -100 and fish:
            fishes_right.remove(fish)
