"""
End-of-day summary board file
"""

import pygame
import DayNightCycle as dnc
import Fonts as fonts
import GameState as gs
import Settings as st

# PANEL DIMENSIONS
PANEL_WIDTH = 500
PANEL_HEIGHT = 300
PANEL_COLOR = (229, 228, 226)

target_y = st.DISPLAY_HEIGHT / 2 - PANEL_HEIGHT / 2
panel_y = -PANEL_HEIGHT
panel_velocity = 0.0
visible = False

most_popular = max(gs.orders_today, key=gs.orders_today.get) if gs.orders_today else "None..."

def show() -> None:
    # called when night starts
    global visible, panel_y, panel_velocity
    visible = True
    panel_y = -PANEL_HEIGHT
    panel_velocity = 0.0

def hide() -> None:
    # called when next day starts
    global visible
    visible = False

def update() -> None:
    # spring physics toward target_y
    global panel_y, panel_velocity
    panel_velocity += (target_y - panel_y) * 0.1
    panel_velocity *= 0.65
    panel_y += panel_velocity

def draw(screen) -> None:
    # draw panel, day number, coins earned today
    if not visible:
        return
    panel_x = st.DISPLAY_WIDTH / 2 - PANEL_WIDTH / 2
    panel_rect = pygame.Rect(panel_x, panel_y, PANEL_WIDTH, PANEL_HEIGHT)
    pygame.draw.rect(screen, PANEL_COLOR, panel_rect, border_radius=12)

    title_surf = fonts.render_font("Day Summary", 50)
    title_rect = title_surf.get_rect(midtop=(panel_rect.centerx, panel_rect.top + 20))
    screen.blit(title_surf, title_rect)

    line_x = panel_rect.left + 30
    line_y = panel_rect.top + 80

    items = [
        f'Drinks served: {gs.drinks_served_today}',
        f'Gross earnings: ${gs.coins_earned_today}',
        f'Upgrades spent: ${gs.upgrades_spent_today}',
        f'Net earnings: ${gs.coins_earned_today - gs.upgrades_spent_today}',
    ]

    for item in items:
        surf = fonts.render_font(item, 28)
        screen.blit(surf, (line_x, line_y))
        line_y += 40