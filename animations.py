from constants import *

medusa_1 = pygame.image.load('Medusa/jellyfish-large1.png').convert_alpha()
medusa_1 = pygame.transform.rotozoom(medusa_1, 0, 1.5)
medusa_2 = pygame.image.load('Medusa/jellyfish-large2.png').convert_alpha()
medusa_2 = pygame.transform.rotozoom(medusa_2, 0, 1.5)
medusa_3 = pygame.image.load('Medusa/jellyfish-large3.png').convert_alpha()
medusa_3 = pygame.transform.rotozoom(medusa_3, 0, 1.5)
medusa_4 = pygame.image.load('Medusa/jellyfish-large4.png').convert_alpha()
medusa_4 = pygame.transform.rotozoom(medusa_4, 0, 1.5)

medusa = [medusa_1, medusa_2, medusa_3, medusa_4]
medusa_index = 0
medusa_surf = medusa[medusa_index]


def medusa_animations():
    global medusa_surf, medusa_index

    medusa_index += 0.05
    if medusa_index >= len(medusa):
        medusa_index = 0
    medusa_surf = medusa[int(medusa_index)]
    return medusa_surf


shark_1 = pygame.transform.scale(
    pygame.image.load('Shark/32bit-shark-thresher1.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
shark_2 = pygame.transform.scale(
    pygame.image.load('Shark/32bit-shark-thresher2.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
shark_3 = pygame.transform.scale(
    pygame.image.load('Shark/32bit-shark-thresher3.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))
shark_4 = pygame.transform.scale(
    pygame.image.load('Shark/32bit-shark-thresher4.png').convert_alpha(), (HOSTILE_WIDTH, HOSTILE_HEIGHT))

shark = [shark_1, shark_2, shark_3, shark_4]
shark_index = 0
shark_surf = shark[shark_index]


def shark_animations():
    global shark_index, shark_surf

    shark_index += 0.05
    if shark_index >= len(shark):
        shark_index = 0
    shark_surf = shark[int(shark_index)]
    return shark_surf
