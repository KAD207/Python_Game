from abc import ABC, abstractmethod

import pygame

import GameState as gamestate
import Queue as queue
import Customer as customer
import Fonts as fonts

class Upgrades(ABC):
    def __init__(self, name: str, description: str, cost: int, level: int, max_level: int, color: tuple[int, int, int] = (178, 190, 181)) -> None:
        self.name = name
        self.description = description
        self.cost = cost
        self.level = level
        self.max_level = max_level
        self.color = color

    def can_afford(self) -> bool:
        return gamestate.coins >= self.cost

    def purchase(self) -> bool:
        if self.can_afford() and self.level < self.max_level:
            gamestate.spend_coins(self.cost)
            self.level += 1
            self.apply_effect()
            return True
        else:
            print(f'Cannot purchase {self.name}!\n')
            return False

    def draw(self, screen, x, y):
        card_rect = pygame.Rect(x, y, 360, 100)
        pygame.draw.rect(screen, self.color, card_rect)

        name_surf = fonts.render_font(self.name, 32)
        name_rect = name_surf.get_rect(topleft=(x+10,y+10))
        screen.blit(name_surf, name_rect)

        desc_surf = fonts.render_font(self.description, 21)
        desc_rect = desc_surf.get_rect(topleft=(x+180,y + 15))
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
