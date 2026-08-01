from pygame.surface import SurfaceType

import Settings as settings
import Fonts as font
import pygame
import Queue as queue
import GameState as gamestate
import Shop as shop
import FloatingText as f

pygame.init()
clock = pygame.time.Clock()

screen: SurfaceType = pygame.display.set_mode((settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
pygame.display.set_caption("☕ Cozy Coffee Stand")

stand_text: SurfaceType = font.render_font("☕ Raccafé", 60)
rect = stand_text.get_rect()
rect.center = (settings.textx, settings.texty)

floating_texts: list = []

def main():

    running = True
    while running:


        # ======================
        # 1. HANDLE INPUT
        # ======================
        for event in pygame.event.get(): # HANDLES INPUT ONLY!!!!!!!!!!
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # shop toggle sidebar
                if shop.shop_button.collidepoint(mouse_x, mouse_y):
                    shop.toggle_sidebar()

                for upgrade in shop.upgrades:
                    if hasattr(upgrade, 'buy_rect') and upgrade.buy_rect.collidepoint(mouse_x, mouse_y):
                        buy_result = upgrade.purchase()
                        if buy_result is True:
                            floating_texts.append(f.FloatingText("Bought!", (50, 180, 20), mouse_x, mouse_y))
                        elif buy_result is False:
                            floating_texts.append(f.FloatingText("Not enough money!", (200, 50, 50), mouse_x, mouse_y))
                    elif upgrade.is_clicked(mouse_x, mouse_y):
                        upgrade.toggle_expanded()

                # stored as a queue in Queue.py so HAVE to be accessed using queue
                if len(queue.customers) > 0 and queue.customers[0].is_clicked(mouse_x, mouse_y):
                    queue.serve_customer()

        # =====================
        # 2. UPDATE GAME STATE
        # =====================
        shop.update()
        queue.try_spawn_customer()

        for ft in floating_texts:
            ft.update()

        floating_texts[:] = [ft for ft in floating_texts if ft.is_alive()]

        # =======================
        # 3. DRAW EVERYTHING
        # =======================

        # DRAW ORDER: BG > CHAR > BGO > CUSTOMER > SHOP
        screen.fill(settings.bgc)                                           # bg
        pygame.draw.rect(screen, settings.groundcolor, settings.groundrect) # ground
        pygame.draw.rect(screen, settings.standcolor, settings.standrect)   # stand

        for i, customer in enumerate(queue.customers):            # customers
            customer.draw(screen, show_order=(i==0))

        shop.draw(screen)                                                   # sidebar
        y_offset = 75
        for upgrade in shop.upgrades:
            upgrade.draw(screen, shop.sidebar_x + 20, y_offset)
            y_offset += 160 if upgrade.expanded else 100
            y_offset += 10
        shop.draw_button(screen)                                            # shop button

        screen.blit(stand_text, rect)                                       # title
        coin_text = font.render_font(f'$ {gamestate.coins}', 50)
        screen.blit(coin_text, (20, 20))                               # coins

        for ft in floating_texts:                                           # floating text
            ft.draw(screen)
        # ========================
        # 4. PUSH TO SCREEN
        # ========================
        pygame.display.update()

        # ========================
        # 5. WAIT FOR NEXT FRAME
        # ========================
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()