import queue

from pygame.surface import SurfaceType

import Settings as st
import Fonts as f
import pygame
import Customer as c
import Queue as q

pygame.init()
clock = pygame.time.Clock()

screen: SurfaceType = pygame.display.set_mode((st.DISPLAY_WIDTH, st.DISPLAY_HEIGHT))
pygame.display.set_caption("☕ Cozy Coffee Stand")

stand_text: SurfaceType = f.render_font("☕ Raccafé")
rect = stand_text.get_rect()
rect.center = (st.textx, st.texty)

# orders_queue: list[str] = ['Latte', 'Espresso', 'Matcha']
# customers = [c.Customer(st.standx + st.standwidth + (i * c.customer_space_between), st.groundy - c.radius, orders_queue[i])
#              for i in range(3)]
# customer = c.Customer(200, st.groundy - c.radius, "Latte")

def main():

    running = True
    while running:
        for event in pygame.event.get(): # HANDLES INPUT ONLY!!!!!!!!!!
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # stored as a queue in Queue.py so HAVE to be accessed using q
                if len(q.customers) > 0 and q.customers[0].is_clicked(mouse_x, mouse_y):
                    q.serve_customer()
                    q.try_spawn_customer()



        screen.fill(st.bgc)
        screen.blit(stand_text, rect)

        # draw customer as a queue
        for i, customer in enumerate(q.customers):
            customer.draw(screen, show_order=(i==0))


        # draw ground strips
        pygame.draw.rect(screen, st.groundcolor, st.groundrect)

        # draw coffee stand
        pygame.draw.rect(screen, st.standcolor, st.standrect)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()