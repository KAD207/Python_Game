# Customer
# ├── position (x, y)
# ├── order (a string like "Latte")
# └── methods:
#     ├── draw(screen)  — draws the circle + order text

import pygame

color = (255, 180, 120)
radius = 20

class Customer:
    def __init__(self, x, y, order):
        self.x = x
        self.y = y
        self.order = order

    def draw(self, screen):
        pygame.draw.circle(screen, color, (self.x, self.y), radius)