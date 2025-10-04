import pygame
from draw_function import *

mouse_pos = pygame.mouse.getpos()

def start_menu():
    if mouse_pos.collidepoint():
        if pygame.mouse.get_pressed() == {True, False, False}:
            pass