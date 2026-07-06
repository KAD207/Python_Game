from pygame.surface import SurfaceType

import Settings as st
import Fonts as f
import pygame
import Customer as c

pygame.init()
clock = pygame.time.Clock()

screen: SurfaceType = pygame.display.set_mode((st.DISPLAY_WIDTH, st.DISPLAY_HEIGHT))
pygame.display.set_caption("☕ Cozy Coffee Stand")

stand_text: SurfaceType = f.render_font("☕ Raccafé")
rect = stand_text.get_rect()
rect.center = (st.textx, st.texty)

customer = c.Customer(200, 400, "Latte")

def main():

    running = True
    while running:
        for event in pygame.event.get(): # HANDLES INPUT ONLY!!!!!!!!!!
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False


        screen.fill(st.bgc)
        screen.blit(stand_text, rect)

        customer.draw(screen)

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