#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import subprocess
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Consola de videojuegos")
icon = pygame.image.load('icono.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((800, 600),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

#cambiar el fondo del juega
background = pygame.image.load('fondomenu.png')
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        #poner fondo constantemente
        screen.blit(background, (0,0))
        draw_text('Consola de videojuegos!! Diviertete con estos tres minijuegos', font, (255, 64, 17), screen, 200, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(350, 100, 100, 50)
        #pygame.Rect(margen izquierda, margen top, largo, alto)
        #draw_text('Juego 1', font, (255, 255, 255), screen, 60, 90)
        button_2 = pygame.Rect(350, 200, 100, 50)

        button_3 = pygame.Rect(350, 300, 100, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game() #mandamos a llamar al metodo del juego.
        if button_2.collidepoint((mx, my)):
            if click:
                game2()
        if button_3.collidepoint((mx, my)):
            if click:
                game3()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Memorama', font, (255, 255, 255), screen, 360, 120)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Hacker-fight', font, (255, 255, 255), screen, 360, 220)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Zudoku', font, (255, 255, 255), screen, 360, 320)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    """running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)"""
    subprocess.getoutput('python memorypuzzle.py')
 
def game2():
    subprocess.getoutput('python hacker.py')

def game3():
    subprocess.getoutput('python GUI.py')




#se manda a ejecutar menu principal 
main_menu()
