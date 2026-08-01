import pygame

black = (0,0,0)
white = (255,255,255)

def render_font(text: str, size: int = 28, italic: bool = False, color: tuple[int, int, int] = (0,0,0)) -> pygame.Surface:
    font = pygame.font.SysFont(None, size, italic=italic)
    return font.render(text, True, color)

