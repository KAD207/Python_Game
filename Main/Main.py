import Settings as st
import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((st.DISPLAY_WIDTH, st.DISPLAY_HEIGHT))
pygame.display.set_caption("☕ Cozy Coffee Stand")
pygame.display.set_mode((st.DISPLAY_WIDTH, st.DISPLAY_HEIGHT))

def main():

    running = True
    while running:
        for event in pygame.event.get(): # HANDLES INPUT ONLY!!!!!!!!!!
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False


        screen.fill(st.bgc)

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