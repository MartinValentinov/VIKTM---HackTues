from constants import *


def player_movement(depth, player_look):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        if depth - PLAYER_SPEED > 500:
            for fish in fishes_left:
                fish.y += PLAYER_SPEED
            for fish in fishes_right:
                fish.y += PLAYER_SPEED

            for hostile_fish in hostile_fishes_left:
                hostile_fish.y += PLAYER_SPEED
            for hostile_fish in hostile_fishes_right:
                hostile_fish.y += PLAYER_SPEED
            
            for fish in special_fish_left:
                fish.y += PLAYER_SPEED
            for fish in special_fish_right:
                fish.y += PLAYER_SPEED

            for fish in unspecial_fish_left:
                fish.y += PLAYER_SPEED
            for fish in unspecial_fish_right:
                fish.y += PLAYER_SPEED

            depth -= 3

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        for fish in fishes_left:
            fish.y -= PLAYER_SPEED
        for fish in fishes_right:
            fish.y -= PLAYER_SPEED

        for hostile_fish in hostile_fishes_left:
            hostile_fish.y -= PLAYER_SPEED
        for hostile_fish in hostile_fishes_right:
            hostile_fish.y -= PLAYER_SPEED

        for fish in special_fish_left:
            fish.y -= PLAYER_SPEED
        for fish in special_fish_right:
            fish.y -= PLAYER_SPEED

        for fish in unspecial_fish_left:
            fish.y -= PLAYER_SPEED
        for fish in unspecial_fish_right:
            fish.y -= PLAYER_SPEED

        depth += 3

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        for fish in fishes_left:
            fish.x += PLAYER_SPEED
        for fish in fishes_right:
            fish.x += PLAYER_SPEED

        for hostile_fish in hostile_fishes_left:
            hostile_fish.x += PLAYER_SPEED
        for hostile_fish in hostile_fishes_right:
            hostile_fish.x += PLAYER_SPEED

        for fish in special_fish_left:
            fish.x += PLAYER_SPEED
        for fish in special_fish_right:
            fish.x += PLAYER_SPEED
        
        for fish in unspecial_fish_left:
            fish.x += PLAYER_SPEED
        for fish in unspecial_fish_right:
            fish.x += PLAYER_SPEED

        player_look = 2

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        for fish in fishes_left:
            fish.x -= PLAYER_SPEED
        for fish in fishes_right:
            fish.x -= PLAYER_SPEED

        for hostile_fish in hostile_fishes_left:
            hostile_fish.x -= PLAYER_SPEED
        for hostile_fish in hostile_fishes_right:
            hostile_fish.x -= PLAYER_SPEED

        for fish in special_fish_left:
            fish.x -= PLAYER_SPEED
        for fish in special_fish_right:
            fish.x -= PLAYER_SPEED

        for fish in unspecial_fish_left:
            fish.x -= PLAYER_SPEED
        for fish in unspecial_fish_right:
            fish.x -= PLAYER_SPEED

        player_look = 1
            
    return depth, player_look
