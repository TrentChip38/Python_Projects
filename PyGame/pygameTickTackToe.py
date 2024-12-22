import pygame
from pygame.locals import *

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

screen = pygame.display.set_mode((340, 340))
#pygame.display.flip()
background = CYAN
run = True
playerTurn = 1
def draw(posx,posy, playerTurn):
    if playerTurn == 1:
        print(playerTurn)
        playerTurn = 2
        #draw x
        pygame.draw.line(screen, RED, (posx + 30, posy + 30), (posx - 30, posy - 30), 5)
        pygame.draw.line(screen, RED, (posx + 30, posy - 30), (posx - 30, posy + 30), 5)
    elif playerTurn == 2:
        print(playerTurn)
        playerTurn = 1
        #draw y
        pygame.draw.circle(screen, RED, (posx, posy), 40, 5)
    return playerTurn


screen.fill(background)
pygame.draw.rect(screen, RED, (115,20,10,300))
pygame.draw.rect(screen, RED, (215,20,10,300))
pygame.draw.rect(screen, RED, (20,115,300,10))
pygame.draw.rect(screen, RED, (20,215,300,10))
pygame.display.update()
while run:
    for event in pygame.event.get():
        #print(event)
        mousePos = pygame.mouse.get_pos()
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            #print(mousePos)
            if (mouseX < 215 and mouseX > 115) and (mouseY > 20 and mouseY < 115):
                playerTurn = draw(170, 70, playerTurn)
            elif (mouseX < 320 and mouseX > 215) and (mouseY > 20 and mouseY < 115):
                playerTurn = draw(270, 70, playerTurn)
            elif (mouseX < 115 and mouseX > 20) and (mouseY > 20 and mouseY < 115):
                playerTurn = draw(70, 70, playerTurn)
            
            elif (mouseX < 215 and mouseX > 115) and (mouseY > 115 and mouseY < 215):
                playerTurn = draw(170, 170, playerTurn)
            elif (mouseX < 320 and mouseX > 215) and (mouseY > 115 and mouseY < 215):
                playerTurn = draw(270, 170, playerTurn)
            elif (mouseX < 115 and mouseX > 20) and (mouseY > 115 and mouseY < 215):
                playerTurn = draw(70, 170, playerTurn)

            elif (mouseX < 215 and mouseX > 115) and (mouseY > 215 and mouseY < 315):
                playerTurn = draw(170, 270, playerTurn)
            elif (mouseX < 320 and mouseX > 215) and (mouseY > 215 and mouseY < 315):
                playerTurn = draw(270, 270, playerTurn)
            elif (mouseX < 115 and mouseX > 20) and (mouseY > 215 and mouseY < 315):
                playerTurn = draw(70, 270, playerTurn)
        #if event.type == pygame.KEYDOWN:
            #background = YELLOW
    pygame.display.update()

pygame.quit()