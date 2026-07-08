# Customer
# ├── position (x, y)
# ├── order (a string like "Latte")
# └── methods:
#     ├── draw(screen)  — draws the circle + order text
from math import sqrt
import pygame
import Fonts as f

color = (255, 180, 120)
radius = 20
customer_space_between = 100

class Customer:
    def __init__(self, x, y, order) -> None:
        self.x = x
        self.y = y
        self.order = order

    def draw(self, screen, show_order: bool = False) -> None:
        pygame.draw.circle(screen, color, (self.x, self.y), radius)

        text_surf = f.render_font(self.order)
        text_rect = text_surf.get_rect()

        text_rect.centerx = self.x  # horizontally centered on customer
        text_rect.bottom = self.y - radius  # sits just above the head

        # if index == 0 then show_order
        if show_order:
            screen.blit(text_surf, text_rect)

    def get_mouse_distance(self, mouse_x, mouse_y) -> float:
        return sqrt((mouse_x - self.x) ** 2 + (mouse_y - self.y) ** 2)

    def is_clicked(self, mouse_x, mouse_y) -> bool:
        dist = self.get_mouse_distance(mouse_x, mouse_y)
        return dist <= radius

    def update_pos(self, new_x):
        self.x = new_x

    def update_queue(self):
        pass