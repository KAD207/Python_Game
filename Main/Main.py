from pygame.surface import SurfaceType

import Settings as settings
import Fonts as font
import pygame
import Queue as queue
import GameState as gamestate
import Shop as shop

pygame.init()
clock = pygame.time.Clock()

screen: SurfaceType = pygame.display.set_mode((settings.DISPLAY_WIDTH, settings.DISPLAY_HEIGHT))
pygame.display.set_caption("☕ Cozy Coffee Stand")

stand_text: SurfaceType = font.render_font("☕ Raccafé", 60)
rect = stand_text.get_rect()
rect.center = (settings.textx, settings.texty)

def main():

    running = True
    while running:
        # Collect & handle input (event loop)
        for event in pygame.event.get(): # HANDLES INPUT ONLY!!!!!!!!!!
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # shop toggle sidebar
                if shop.shop_button.collidepoint(mouse_x, mouse_y):
                    shop.toggle_sidebar()

                # stored as a queue in Queue.py so HAVE to be accessed using queue
                if len(queue.customers) > 0 and queue.customers[0].is_clicked(mouse_x, mouse_y):
                    queue.serve_customer()
        # FUTURE: to pause when shop is open, add a `paused` flag:
        # if not paused:
        #     q.try_spawn_customer()
        #     # update game state here
        # drawing still runs every frame regardless

        # spawn customer randomly 2s-6s
        queue.try_spawn_customer()

        # DRAW ORDER: BG > CHAR > BGO > CUSTOMER > SHOP
        screen.fill(settings.bgc)
        pygame.draw.rect(screen, settings.groundcolor, settings.groundrect)
        pygame.draw.rect(screen, settings.standcolor, settings.standrect)

        # customers
        for i, customer in enumerate(queue.customers):
            customer.draw(screen, show_order=(i==0))

        # updates
        shop.update()
        shop.draw(screen)
        for i, upgrade in enumerate(shop.upgrades):
            upgrade.draw(screen, shop.sidebar_x + 20,  75 + i * 120)
        shop.draw_button(screen)

        # stand rectangle text (always on top)
        screen.blit(stand_text, rect)
        coin_text = font.render_font(f'$ {gamestate.coins}', 50)
        screen.blit(coin_text, (20, 20))  # top left for now

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()