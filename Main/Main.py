from pygame.surface import SurfaceType

import Settings as st
import Fonts as f
import pygame
import Customer as c
import Queue as q
import GameState as gs
import Shop as sh

pygame.init()
clock = pygame.time.Clock()

screen: SurfaceType = pygame.display.set_mode((st.DISPLAY_WIDTH, st.DISPLAY_HEIGHT))
pygame.display.set_caption("☕ Cozy Coffee Stand")

stand_text: SurfaceType = f.render_font("☕ Raccafé", 60)
rect = stand_text.get_rect()
rect.center = (st.textx, st.texty)

def main():

    running = True
    while running:
        # Collect & handle input (event loop)
        for event in pygame.event.get(): # HANDLES INPUT ONLY!!!!!!!!!!
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                sh.toggle_sidebar()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # stored as a queue in Queue.py so HAVE to be accessed using q
                if len(q.customers) > 0 and q.customers[0].is_clicked(mouse_x, mouse_y):
                    q.serve_customer()

        # Update game state (nothing here yet)
        sh.update()

        # Draw everything (screen.fill for now)
        # Push to screen (display.update)
        # Wait for next frame (clock.tick)

        # FUTURE: to pause when shop is open, add a `paused` flag:
        # if not paused:
        #     q.try_spawn_customer()
        #     # update game state here
        # drawing still runs every frame regardless

        # spawn customer randomly 2s-6s
        q.try_spawn_customer()

        # background
        screen.fill(st.bgc)

        # draw ground strips
        pygame.draw.rect(screen, st.groundcolor, st.groundrect)

        # draw coffee stand
        pygame.draw.rect(screen, st.standcolor, st.standrect)

        # draw customer as a queue
        for i, customer in enumerate(q.customers):
            customer.draw(screen, show_order=(i==0))

        # draw shop
        sh.draw(screen)

        # stand rectangle text (always on top)
        screen.blit(stand_text, rect)
        coin_text = f.render_font(f'$ {gs.coins}', 28)
        screen.blit(coin_text, (20, 20))  # top left for now

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()