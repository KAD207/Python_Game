DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 768
x = DISPLAY_WIDTH / 2 - 100
y = DISPLAY_HEIGHT / 2

bgc = (255, 248, 220)

# ground strips color/rect
groundx = 0
groundy = DISPLAY_HEIGHT * 0.7
groundcolor = (120, 180, 80)
groundrect = (groundx, groundy, DISPLAY_WIDTH, DISPLAY_HEIGHT * 0.45)

# coffee stand
standwidth = 250
standheight = 350
standcolor = (180, 140, 100)
standx = DISPLAY_WIDTH / 2
standy = groundy - standheight
standrect = (standx - standwidth/2, standy, standwidth, standheight)

textx = DISPLAY_WIDTH / 2
texty = DISPLAY_HEIGHT / 2 - standheight

black = (0,0,0)
white = (255,255,255)