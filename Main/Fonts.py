import pygame

black = (0,0,0)
white = (255,255,255)

def render_font(text: str):
    font = pygame.font.Font(None, 50)
    return font.render(text, True, black)
