import pygame
import Fonts as fonts

class FloatingText:
    def __init__(self, text: str, color: tuple[int, int, int,], x: int, y: int, duration: int = 60) -> None:
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.timer = duration # frames, 60 = ~1 seconds at 60fps

    def update(self):
        self.timer -= 1
        self.y -= 1

    def is_alive(self) -> bool:
        return self.timer > 0

    def draw(self, screen: pygame.Surface) -> None:
        surf = fonts.render_font(self.text, 28, color=self.color)
        text_rect = surf.get_rect()
        text_rect.centerx = self.x
        text_rect.centery = self.y
        screen.blit(surf, text_rect)