from animations import *
from sys import exit

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)

text_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
text_surf = text_font.render('Health: ', False, 'White')

max_heart_surf = pygame.image.load('Hearts/7 hearts.png').convert_alpha()
max_heart_surf = pygame.transform.rotozoom(max_heart_surf, 0, 0.3)
broken_heart_surf = pygame.image.load('Hearts/broken heart.png').convert_alpha()
broken_heart_surf = pygame.transform.rotozoom(broken_heart_surf, 0, 0.3)

new_cursor = pygame.image.load('Cursor/noun-viewfinder-92699.png').convert_alpha()
new_cursor = pygame.transform.rotozoom(new_cursor, 0, 0.1)
newer_cursor = pygame.image.load('Cursor/Cursor_2_blue.png').convert_alpha()
newer_cursor = pygame.transform.rotozoom(newer_cursor, 0, 0.1)
pygame.mouse.set_visible(False)

depth_text = text_font.render('You want to go deeper to find the GOLDEN FISH', False, 'White')
depth_text_rect = depth_text.get_rect(center=(WIDTH/2, HEIGHT - 30))

depth_meter_1 = pygame.image.load('Depth/meter_counter-1.webp').convert_alpha()
depth_meter_1 = pygame.transform.rotozoom(depth_meter_1, 0, 0.3)

depth_meter_2 = pygame.image.load('Depth/meter_counter-2.webp').convert_alpha()
depth_meter_2 = pygame.transform.rotozoom(depth_meter_2, 0, 0.3)

depth_meter_3 = pygame.image.load('Depth/meter_counter-3.webp').convert_alpha()
depth_meter_3 = pygame.transform.rotozoom(depth_meter_3, 0, 0.3)

blue_fish = pygame.transform.scale(
    pygame.image.load('Normal_fishes/fish_blue.png').convert_alpha(), (3*FISH_WIDTH, 3*FISH_HEIGHT))
blue_fish = pygame.transform.flip(blue_fish, 1, 0)
blue_fish = pygame.transform.rotozoom(blue_fish, 0, 0.5)

green_fish = pygame.transform.scale(
    pygame.image.load('Normal_fishes/fish_green.png').convert_alpha(), (3*FISH_WIDTH, 3*FISH_HEIGHT))
green_fish = pygame.transform.rotozoom(green_fish, 0, 0.5)


def draw(window, player_health, depth, score, player_surf, player_rect, player_look_left, temp_x=0):
    # Draw everything on screen

    background_color = BACKGROUND_COLOR
    if depth < 30:
        background_color = [RED, GREEN, BLUE]

    background_surf_draw = pygame.Surface((WIDTH, HEIGHT))
    background_surf_draw.fill(background_color)

    key = pygame.key.get_pressed()

    if key[pygame.K_UP] or key[pygame.K_w] and depth >= 30:
        background_color[0] += 0.0125
        background_color[1] += 0.0125
        background_color[2] += 0.0125

    if key[pygame.K_DOWN] or key[pygame.K_s] and depth >= 30:
        background_color[0] -= 0.0125
        background_color[1] -= 0.0125
        background_color[2] -= 0.0125

    if background_color[0] <= 0.5:
        background_color[0] = 0
    if background_color[1] <= 0.5:
        background_color[1] = 0
    if background_color[2] <= 0.5:
        background_color[2] = 0

    window.blit(background_surf_draw, (0, 0))

    # pygame.draw.circle(window, 'red', (WIDTH/2, HEIGHT/2), HOSTILE_RADIUS, 5)
    # pygame.draw.circle(window, 'red', (WIDTH / 2, HEIGHT / 2), SPECIAL_FISH_RADIUS, 5)

    if player_look_left == 2:
        player_surf = pygame.transform.flip(player_surf, 1, 0)

    window.blit(player_surf, player_rect)

    window.blit(text_surf, (5, 5))

    for fish in fishes_left:
        window.blit(green_fish, (fish.x, fish.y))
    for fish in fishes_right:
        window.blit(blue_fish, (fish.x, fish.y))

    for hostile_fish in hostile_fishes_left:
        hostile_fish_surf = shark_animations()
        window.blit(hostile_fish_surf, (hostile_fish.x, hostile_fish.y))
    for hostile_fish in hostile_fishes_right:
        hostile_fish_surf = shark_animations()
        hostile_fish_surf = pygame.transform.flip(hostile_fish_surf, 1, 0)
        window.blit(hostile_fish_surf, (hostile_fish.x, hostile_fish.y))

    for fish in special_fish_left:
        fish_surf = medusa_animations()
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in special_fish_right:
        fish_surf = medusa_animations()
        window.blit(fish_surf, (fish.x, fish.y))

    for fish in unspecial_fish_left:
        fish_surf = medusa_animations()
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in unspecial_fish_right:
        fish_surf = medusa_animations()
        window.blit(fish_surf, (fish.x, fish.y))

    if depth == 10:
        window.blit(depth_text, depth_text_rect)

    cursor_rect = new_cursor.get_rect(center=pygame.mouse.get_pos())
    WINDOW.blit(new_cursor, cursor_rect)

    for i in range(player_health):
        if i <= 0:
            temp_x = 90
        elif i == 1:
            temp_x = 105
        elif i == 2:
            temp_x = 120
        elif i == 3:
            temp_x = 135
        elif i == 4:
            temp_x = 150
        elif i == 5:
            temp_x = 165
        elif i == 6:
            temp_x = 180
        window.blit(max_heart_surf, (temp_x, -7))
        temp_x = 0

    if player_health < 1:
        window.blit(broken_heart_surf, (70, -45))
    if player_health < 2:
        window.blit(broken_heart_surf, (85, -45))
    if player_health < 3:
        window.blit(broken_heart_surf, (100, -45))
    if player_health < 4:
        window.blit(broken_heart_surf, (115, -45))
    if player_health < 5:
        window.blit(broken_heart_surf, (130, -45))
    if player_health < 6:
        window.blit(broken_heart_surf, (145, -45))
    if player_health < 7:
        window.blit(broken_heart_surf, (160, -45))

    # depth_text = pygame.font.Font('Font/Pixeltype.ttf', 35)
    # depth_text_surf = depth_text.render(f'{depth}', 0, 'White')
    depth_text_surf = text_font.render(f'{depth}', 0, 'White')
    depth_rect = depth_text_surf.get_rect(midleft=(50, HEIGHT - 27))

    score_text_surf = text_font.render(f'Score: {score}', 0, 'White')
    score_rect = score_text_surf.get_rect(midright=(WIDTH - 10, 25))
    window.blit(score_text_surf, score_rect)

    if depth <= 60:
        window.blit(depth_meter_1, (12, HEIGHT - 50))
    elif depth <= 110:
        window.blit(depth_meter_2, (12, HEIGHT - 50))
    else:
        window.blit(depth_meter_3, (12, HEIGHT - 50))
    window.blit(depth_text_surf, depth_rect)

    pygame.display.update()


def start_screen(window):
    start_surf = pygame.Surface((200, 65))

    # cntrbutoton_text = pygame.font.Font('Font/Pixeltype.ttf', 65)
    # cntrbutton_text_surf = cntrbutoton_text.render('Controls', False, 'Black')
    cntrbutton_text_surf = text_font.render('Controls', False, 'Black')

    # quitbutton_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
    # quitbutton_text_surf = quitbutton_text.render('Quit', False, 'Black')
    quitbutton_text_surf = text_font.render('Quit', False, 'Black')

    # start_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
    # start_text_surf = start_text.render('START', False, 'Black')
    start_text_surf = text_font.render('START', False, 'Black')

    control_surf = pygame.Surface((200, 65))
    control_rect = control_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
    control_surf.fill('white')

    quit_surf = pygame.Surface((200, 65))
    quit_rect = quit_surf.get_rect(center=(WIDTH/2, HEIGHT/2 + HEIGHT/4))
    quit_surf.fill('white')

    start_surf.fill('white')
    start_rect = start_surf.get_rect(center=(WIDTH/2, HEIGHT/2 - HEIGHT/4))

    # start_screen_surf = pygame.image.load('Background/Underwater BG Blank.png').convert_alpha()

    window.blit(background_surf, (0, 0))
    window.blit(start_surf, start_rect)
    window.blit(control_surf, control_rect)
    window.blit(quit_surf, quit_rect)

    start_text_rect = start_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 - HEIGHT/4))

    window.blit(start_text_surf, start_text_rect)

    quitbutton_text_rect = quitbutton_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 + HEIGHT/4))
    window.blit(quitbutton_text_surf,quitbutton_text_rect)

    cntrbutoton_text_rect = cntrbutton_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
    window.blit(cntrbutton_text_surf, cntrbutoton_text_rect)

    cursor_rect = new_cursor.get_rect(center=pygame.mouse.get_pos())
    window.blit(new_cursor, cursor_rect)

    pygame.display.update()

    ret = 0

    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret = 1

    if control_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret = 2

    if quit_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            exit()

    return ret


def controls_menu(window):
    window.blit(background_surf, (0, 0))

    # controls_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
    # controls_text_surf = controls_text.render('Controls:', False, 'Black')
    controls_text_surf = text_font.render('Controls:', False, 'Black')

    # moving_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
    # moving_text_surf = moving_text.render('Moving - WASD or Arrow keys', False, 'Black')
    moving_text_surf = text_font.render('Moving - WASD or Arrow keys', False, 'Black')

    # jellyfish_text = pygame.font.Font('Font/Pixeltype.ttf', 65)
    # jellyfish_text_surf = jellyfish_text.render('(Jellyfish)', False, 'black')
    jellyfish_text_surf = text_font.render('(Take photos of yellow Jellyfish)', False, 'black')

    # photo_text = pygame.font.Font('Font/Pixeltype.ttf', 65)
    # photo_text_surf = photo_text.render('Taking photos - Left Mouse Button Click', False, 'Black')
    photo_text_surf = text_font.render('Taking photos - Left Mouse Button Click', False, 'Black')

    # backbutton_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
    # backbutton_text_surf = backbutton_text.render('Back', False, 'Black')
    backbutton_text_surf = text_font.render('Back', False, 'Black')

    controls_text_rect = controls_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 - HEIGHT/4 - HEIGHT/8))
    window.blit(controls_text_surf, controls_text_rect)

    jellyfish_text_rect = jellyfish_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 + HEIGHT/8 - HEIGHT/16))
    window.blit(jellyfish_text_surf, jellyfish_text_rect)

    moving_text_rect = moving_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 - HEIGHT/4 + HEIGHT/8))
    window.blit(moving_text_surf, moving_text_rect)

    photo_text_rect = photo_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
    window.blit(photo_text_surf, photo_text_rect)

    back_surf = pygame.Surface((200, 65))
    back_rect = back_surf.get_rect(center=(WIDTH/2 - WIDTH/4, HEIGHT/2 + HEIGHT/4 + HEIGHT/8))
    back_surf.fill('white')
    window.blit(back_surf, back_rect)

    backbutton_text_rect = backbutton_text_surf.get_rect(center=(WIDTH/2 - WIDTH/4, HEIGHT/2 + HEIGHT/4 + HEIGHT/8))
    window.blit(backbutton_text_surf, backbutton_text_rect)

    cursor_rect = new_cursor.get_rect(center=pygame.mouse.get_pos())
    window.blit(new_cursor, cursor_rect)

    ret_2 = 2
    mouse_pos = pygame.mouse.get_pos()
    if back_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret_2 = 0

    pygame.display.update()

    return ret_2


def death_screen(window, depth, score):
    background_surf_2 = pygame.surface.Surface((WIDTH, HEIGHT))
    background_surf_2.fill('black')
    window.blit(background_surf_2, (0, 0))

    # depth_text = pygame.font.Font('Font/Pixeltype.ttf', 60)
    # depth_text_surf = depth_text.render(f'{depth} m', False, BACKGROUND_COLOR)
    # depth_text_surf = text_font.render(f'{depth}', False, BACKGROUND_COLOR)

    # depth_text_rect = depth_text_surf.get_rect(center=(WIDTH/2 - WIDTH/4, HEIGHT/2 + HEIGHT/4))
    # window.blit(depth_text_surf, depth_text_rect)

    # score_text = pygame.font.Font('Font/Pixeltype.ttf', 60)
    # score_text_surf = score_text.render(f'{score}', False, BACKGROUND_COLOR)
    # score_text_surf = text_font.render(f'{score}', False, BACKGROUND_COLOR)

    # score_text_rect = score_text_surf.get_rect(center=(WIDTH/2 - WIDTH/4, HEIGHT/2))
    # window.blit(score_text_surf, score_text_rect)

    # endscreen_text = pygame.font.Font('Font/Pixeltype.ttf', 70)
    # endscreen_text_surf = endscreen_text.render('You Lose 💀     to pay respects', False, BACKGROUND_COLOR)
    endscreen_text_surf = text_font.render('You DIED', False, 'red')

    # endres_text = pygame.font.Font('Font/Pixeltype.ttf', 50)
    # endres_text_surf = endres_text.render('Restart', False, BACKGROUND_COLOR)
    endres_text_surf = text_font.render('Restart', False, BACKGROUND_COLOR)

    # endmenu_text = pygame.font.Font('Font/Pixeltype.ttf', 45)
    # endmenu_text_surf = endmenu_text.render('Main Menu', False, BACKGROUND_COLOR)
    endmenu_text_surf = text_font.render('Main Menu', False, BACKGROUND_COLOR)

    # endscore_text = pygame.font.Font('Font/Pixeltype.ttf', 60)
    # endscore_text_surf = endscore_text.render('Score:', False, BACKGROUND_COLOR)
    endscore_text_surf = text_font.render(f'Score: {score}', False, BACKGROUND_COLOR)

    # endmeters_text = pygame.font.Font('Font/Pixeltype.ttf', 60)
    # endmeters_text_surf = endmeters_text.render('Meters:', False, BACKGROUND_COLOR)
    endmeters_text_surf = text_font.render(f'Meters: {depth}', False, BACKGROUND_COLOR)

    menubutton_surf = pygame.Surface((150, 60))
    menubutton_surf.fill('White')
    menubutton_rect = menubutton_surf.get_rect(center=(WIDTH/2 + WIDTH/4, HEIGHT/2 + HEIGHT/4))
    window.blit(menubutton_surf, menubutton_rect)

    resbutton_surf = pygame.Surface((150, 60))
    resbutton_surf.fill('white')
    resbutton_rect = resbutton_surf.get_rect(center=(WIDTH/2 + WIDTH/4, HEIGHT/2))
    window.blit(resbutton_surf, resbutton_rect)

    endscreen_text_rect = endscreen_text_surf.get_rect(center=(WIDTH/2, HEIGHT/2 - HEIGHT/4))
    window.blit(endscreen_text_surf, endscreen_text_rect)

    endmenu_text_rect = endmenu_text_surf.get_rect(center=(WIDTH/2 + WIDTH/4, HEIGHT/2 + HEIGHT/4))
    window.blit(endmenu_text_surf, endmenu_text_rect)

    endres_text_rect = endres_text_surf.get_rect(center=(WIDTH/2 + WIDTH/4, HEIGHT/2))
    window.blit(endres_text_surf, endres_text_rect)

    endscore_text_rect = endscore_text_surf.get_rect(center=(WIDTH/2 - WIDTH/4, HEIGHT/2))
    window.blit(endscore_text_surf, endscore_text_rect)

    endmeters_text_rect = endmeters_text_surf.get_rect(center=(WIDTH/2 - WIDTH/4, HEIGHT/2 + HEIGHT/4))
    window.blit(endmeters_text_surf, endmeters_text_rect)

    mouse_pos = pygame.mouse.get_pos()
    ret_3 = 3

    cursor_rect = newer_cursor.get_rect(center=pygame.mouse.get_pos())
    window.blit(newer_cursor, cursor_rect)

    if resbutton_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret_3 = 4

    if menubutton_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret_3 = 5

    pygame.display.update()

    return ret_3
