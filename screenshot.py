from constants import *


def capture_fish():
    ret = 0
    mouse_pos = pygame.mouse.get_pos()
    for fish in special_fish_left:
        if fish.collidepoint(mouse_pos):
            ret = 1
            unspecial_fish_left.append(fish)
            special_fish_left.remove(fish)
        
    for fish in special_fish_right:
        if fish.collidepoint(mouse_pos):
            ret = 1
            unspecial_fish_right.append(fish)
            special_fish_right.remove(fish)

    return ret
