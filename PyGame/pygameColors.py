import pygame

pygame.init()

#colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (155, 0, 155)
ORANGE = (255, 127, 0)
XENO = (127, 40, 100)
NAVY = (27, 40, 100)

screen = pygame.display.set_mode((800, 600))
background = CYAN
run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if background == GRAY:
                background = WHITE
            else:
                background = GRAY
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
            elif event.key == pygame.K_c:
                background = CYAN
            elif event.key == pygame.K_m:
                background = MAGENTA
            elif event.key == pygame.K_b:
                background = BLUE
            elif event.key == pygame.K_w:
                background = WHITE
            elif event.key == pygame.K_b:
                background = BLACK
            elif event.key == pygame.K_y:
                background = YELLOW
            elif event.key == pygame.K_a:
                background = GRAY
            elif event.key == pygame.K_p:
                background = PURPLE
            elif event.key == pygame.K_o:
                background = ORANGE
            elif event.key == pygame.K_x:
                background = XENO
            elif event.key == pygame.K_n:
                background = NAVY
    screen.fill(background)
    pygame.display.update()

pygame.quit()