import random
import math
from constants import *

player_x = WIDTH // 2
player_y = HEIGHT // 2


def hostile_fish_generator():
    for i in range(0, 1):
        hostile_fish_y = random.randint(-50, 2*HEIGHT)

        side = random.randint(1, 2)
        # 1 is left, 2 is right

        if side == 1:
            hostile_fish_x = random.randint(-HOSTILE_WIDTH - 100, -HOSTILE_WIDTH)
            hostile_fish = pygame.Rect(hostile_fish_x, hostile_fish_y, HOSTILE_WIDTH, HOSTILE_HEIGHT)
            hostile_fishes_left.append(hostile_fish)

        else:
            hostile_fish_x = random.randint(WIDTH, WIDTH + 100)
            hostile_fish = pygame.Rect(hostile_fish_x, hostile_fish_y, HOSTILE_WIDTH, HOSTILE_HEIGHT)
            hostile_fishes_right.append(hostile_fish)


def calculate_radius(hostile_fish):
    x = abs(hostile_fish.x - WIDTH/2)
    y = abs(hostile_fish.y - HEIGHT/2)
    r = math.sqrt(x*x + y*y)
    if r <= HOSTILE_RADIUS:
        return True
    else:
        return False


def hostile_fish_movement():
    for hostile_fish in hostile_fishes_left:
        if calculate_radius(hostile_fish):
            if hostile_fish.x > WIDTH / 2:
                hostile_fish.x -= HOSTILE_VEL_PLAYER_SPOTTED
            else:
                hostile_fish.x += HOSTILE_VEL_PLAYER_SPOTTED

            if hostile_fish.y > HEIGHT / 2:
                hostile_fish.y -= HOSTILE_VEL_PLAYER_SPOTTED
            else:
                hostile_fish.y += HOSTILE_VEL_PLAYER_SPOTTED
        else:
            hostile_fish.x += HOSTILE_VEL
            if hostile_fish.x > WIDTH + HOSTILE_WIDTH*2 and hostile_fish in hostile_fishes_left:
                hostile_fishes_left.remove(hostile_fish)
            elif (hostile_fish.y < -300 or hostile_fish.y > HEIGHT + 300) and hostile_fish in hostile_fishes_left:
                hostile_fishes_left.remove(hostile_fish)

        if hostile_fish.x > WIDTH//2 and hostile_fish in hostile_fishes_left:
            hostile_fishes_right.append(hostile_fish)
            hostile_fishes_left.remove(hostile_fish)

    for hostile_fish in hostile_fishes_right:
        if calculate_radius(hostile_fish):
            if hostile_fish.x > WIDTH/2:
                hostile_fish.x -= HOSTILE_VEL_PLAYER_SPOTTED
            else:
                hostile_fish.x += HOSTILE_VEL_PLAYER_SPOTTED

            if hostile_fish.y > HEIGHT/2:
                hostile_fish.y -= HOSTILE_VEL_PLAYER_SPOTTED
            else:
                hostile_fish.y += HOSTILE_VEL_PLAYER_SPOTTED
        else:
            hostile_fish.x -= HOSTILE_VEL
            if hostile_fish.x < -HOSTILE_WIDTH*2 and hostile_fish in hostile_fishes_right:
                hostile_fishes_right.remove(hostile_fish)
            elif (hostile_fish.y < -300 or hostile_fish.y > HEIGHT + 300) and hostile_fish in hostile_fishes_right:
                hostile_fishes_right.remove(hostile_fish)

        if hostile_fish.x < WIDTH//2 and hostile_fish in hostile_fishes_right:
            hostile_fishes_left.append(hostile_fish)
            hostile_fishes_right.remove(hostile_fish)
