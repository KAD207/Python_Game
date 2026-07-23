import pygame

black = (0,0,0)
white = (255,255,255)

def render_font(text: str, size: int = 38):
    font = pygame.font.Font(None, size)
    return font.render(text, True, black)
