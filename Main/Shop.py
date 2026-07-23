import pygame
import Settings as st

sidebar_width: int = 400
sidebar_x: int = -sidebar_width
sidebar_open: bool = False
sidebar_color: tuple[int, int, int] = (229, 228, 226)

def toggle_sidebar():
    global sidebar_open
    sidebar_open = not sidebar_open

def update():
    global sidebar_x
    target_x = 0 if sidebar_open else -sidebar_width
    sidebar_x += (target_x - sidebar_x) * 0.15

def draw(screen):
    pygame.draw.rect(screen, sidebar_color, (sidebar_x, 0, sidebar_width, st.DISPLAY_HEIGHT))

