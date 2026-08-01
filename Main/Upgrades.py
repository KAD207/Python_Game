from abc import ABC, abstractmethod

import pygame

import GameState as gamestate
import Queue as queue
import Customer as customer
import Fonts as fonts

class Upgrades(ABC):
    def __init__(self, name: str, description: str, cost: int, level: int, max_level: int,
                 color: tuple[int, int, int] = (178, 190, 181)) -> None:
        self.name = name
        self.description = description
        self.cost = cost
        self.level = level
        self.max_level = max_level
        self.color = color
        self.expanded = False
        self.last_failed_attempt = 0

    def can_afford(self) -> bool:
        return gamestate.coins >= self.cost

    def purchase(self) -> bool | None:
        current_time = pygame.time.get_ticks()
        if not self.can_afford():
            if current_time - self.last_failed_attempt < 1000:
                return None # silently blocked = no floating text
            self.last_failed_attempt = current_time

        if self.can_afford() and self.level < self.max_level:
            gamestate.spend_coins(self.cost)
            self.level += 1
            self.apply_effect()
            return True
        else:
            return False

    def is_clicked(self, mouse_x, mouse_y):
        if hasattr(self, 'card_rect'):
            return self.card_rect.collidepoint(mouse_x, mouse_y)
        return False

    def toggle_expanded(self):
        self.expanded = not self.expanded

    def draw(self, screen, x, y):
        card_height = 160 if self.expanded else 100
        self.card_rect = pygame.Rect(x, y, 360, card_height)
        pygame.draw.rect(screen, self.color, self.card_rect)

        # always show name
        name_surf = fonts.render_font(self.name, 32)
        name_rect = name_surf.get_rect(topleft=(x+10,y+10))
        screen.blit(name_surf, name_rect)

        # always show cost (bottom left) and level (bottom right)
        cost_surf = fonts.render_font(f'$ {self.cost}', 22)
        cost_rect = cost_surf.get_rect(bottomleft=(x + 10, y + card_height - 10))
        screen.blit(cost_surf, cost_rect)

        level_surf = fonts.render_font(f'Lv {self.level}/{self.max_level}', 22)
        level_rect = level_surf.get_rect(bottomright=(x + 350, y + card_height - 10))
        screen.blit(level_surf, level_rect)

        # always shop buy button
        self.buy_rect = pygame.Rect(x + 265, y + 10, 80, 35)
        pygame.draw.rect(screen, (150, 200, 150), self.buy_rect)
        buy_surf = fonts.render_font("BUY", 24)
        buy_rect = buy_surf.get_rect(center=self.buy_rect.center)
        screen.blit(buy_surf, buy_rect)

        if self.expanded:
            desc_surf = fonts.render_font(self.description, 21, italic=True)
            desc_rect = desc_surf.get_rect(topleft=(x + 10,y + 45))
            screen.blit(desc_surf, desc_rect)

    @abstractmethod
    def apply_effect(self):
        pass


class LargerQueueUpgrade(Upgrades):
    def apply_effect(self):
        queue.MAX_QUEUE_SIZE += 1
        customer.customer_space_between -= 6
        print(f'LargerQueueUpgrade fired!\n')

class FasterSpawnUpgrade(Upgrades):
    def apply_effect(self):
        queue.spawn_time_inclusive -= 100
        queue.spawn_time_exclusive -= 100
        print(f'FasterSpawnUpgrade fired!\n')

class CosmeticsUpgrade(Upgrades):
    def apply_effect(self):
        print(f'CosmeticsUpgrade fired!\n')
