import pygame
pygame.init()

WIDTH, HEIGHT = 1500, 750

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = [96, 126, 181]

RED = 96
GREEN = 126
BLUE = 181

FPS = 60

PLAYER_SPEED = 7

BOAT_VEL = 7

FISH_HEIGHT = 10
FISH_WIDTH = 20
FISH_VEL = 3

HOSTILE_HEIGHT = 50
HOSTILE_WIDTH = 150
HOSTILE_VEL = 6
HOSTILE_VEL_PLAYER_SPOTTED = 3
HOSTILE_RADIUS = 500

SPECIAL_FISH_RADIUS = 300
SPECIAL_FISH_VEL = 12
SPECIAL_VEL_PLAYER_SPOTTED = 4
SPECIAL_FISH_HEIGHT = 30
SPECIAL_FISH_WIDTH = 60

GOLDEN_FISH_HEIGHT = 10
GOLDEN_FISH_WIDTH = 20

fishes_right = []
fishes_left = []

special_fish_right = []
special_fish_left = []

unspecial_fish_left = []
unspecial_fish_right = []

hostile_fishes_right = []
hostile_fishes_left = []

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 50

# player_surf = pygame.Surface((100, 40))
# player_surf = pygame.transform.scale(pygame.image.load('Player/diver.webp').convert_alpha(), (100, 40))
# player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
