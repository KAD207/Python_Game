import pygame

import Settings as st
import SummaryBoard as sb
import GameState as gs
import Queue as queue

cream = (255, 248, 220)
navy = (20, 24, 82)

# time tracking
day_start_time = 0
current_day = 1
is_night = False
night_start_time = 0

def get_day_progress() -> float:
    # 0.0 to 1.0
    if is_night:
        return 1.0
    elapsed_time = pygame.time.get_ticks() - day_start_time
    return min(elapsed_time / st.DAY_DURATION, 1.0)

def update() -> None:
    # check if day is over -> start next day
    global day_start_time, current_day, is_night, night_start_time
    progress = get_day_progress()

    if progress >= 1.0 and not is_night:
        is_night = True
        night_start_time = pygame.time.get_ticks()
        sb.show()

    if is_night:
        night_elapsed = pygame.time.get_ticks() - night_start_time
        if night_elapsed >= st.NIGHT_DURATION:
            is_night = False
            current_day += 1
            day_start_time = pygame.time.get_ticks()
            sb.hide()
            gs.reset_daily_stats()
            queue.reset_spawn_timer()


def draw_overlay(screen) -> None:
    # calculator color on progress
    progress = get_day_progress()

    # larp each RGB channel separately
    r = cream[0] + (navy[0] - cream[0]) * progress
    g = cream[1] + (navy[1] - cream[1]) * progress
    b = cream[2] + (navy[2] - cream[2]) * progress

    overlay_surf = pygame.Surface((st.DISPLAY_WIDTH, st.DISPLAY_HEIGHT))
    overlay_surf.fill(( int(r), int(g), int(b) ))
    overlay_surf.set_alpha( int(progress * 100) )

    # blit overlay
    screen.blit(overlay_surf, (0, 0))

def draw_clock(screen) -> None:
    # draw circular clock top right
    pass