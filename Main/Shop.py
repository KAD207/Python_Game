import pygame

import Settings as st
import Fonts as font
import Upgrades as upgrade

sidebar_width: int = 400
sidebar_x: int = -sidebar_width
sidebar_open: bool = False
sidebar_color: tuple[int, int, int] = (229, 228, 226)

# left, top, width, height
shop_button_width: int = 100
shop_button_height: int = 100
shop_button_color: tuple[int, int, int] = (54, 69, 79)
shop_button: pygame.Rect = pygame.Rect(40, st.DISPLAY_HEIGHT - shop_button_height * 1.25, shop_button_width,
                                       shop_button_height)

upgrades = [
    upgrade.LargerQueueUpgrade("Larger Queue", "-Fit more customers", 50, 0, 5),
    upgrade.FasterSpawnUpgrade("Faster Spawns", "-Customers arrive faster", 75, 0, 10),
    upgrade.CosmeticsUpgrade("Cosmetics", "-Cosmetically cosmetical", 10, 0, 100)
    ]

def toggle_sidebar():
    global sidebar_open
    sidebar_open = not sidebar_open

def update():
    global sidebar_x
    target_x = 0 if sidebar_open else -sidebar_width
    sidebar_x += (target_x - sidebar_x) * 0.15

def draw_button(screen):
    pygame.draw.rect(screen, shop_button_color, shop_button)
    text_surf = font.render_font("SHOP", 45)
    text_rect = text_surf.get_rect()
    text_rect.center = shop_button.center
    screen.blit(text_surf, text_rect)

def draw(screen):
    pygame.draw.rect(screen, sidebar_color, (sidebar_x, 0, sidebar_width, st.DISPLAY_HEIGHT))

