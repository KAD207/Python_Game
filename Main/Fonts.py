import pygame

black = (0,0,0)
white = (255,255,255)

def render_font(text: str, size: int = 40, italic: bool = False):
    font = pygame.font.Font(None, size)
    if not italic:
        return font.render(text, True, black)
    else:
        return font.render(text, True, black)

