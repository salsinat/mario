#!/usr/bin/env python

#-------------------------------------- IMPORTATION --------------------------------------#
from sys import exit # déclaration d'importation du module sys
import pygame # déclaration d'importation du module pygame
from pygame.locals import *

pygame.init() # initialisation du module pygame. Il est obligatoire d'appeler cette fonction une seule fois après l'avoir importé

#-------------------------------------- INITIALISATION FENÊTRE DE JEU ET DES VARIABLES --------------------------------------#

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("MARIO BROS")
running = True;
COLOR_BLACK = Color(0, 0, 0)
COLOR_RED = Color(255, 0, 0)
clock = pygame.time.Clock()
FPS = 60

#-------------------------------------- CREATION DU PERSONNAGE --------------------------------------#
square = Rect(5, 5, 50, 50)

#-------------------------------------- MAJ DE L'ETAT DE JEU --------------------------------------#
delta = 0

while running:
    # On "repeint" l'écran en noir afin de ne pas laisser l'ancien carré
    screen.fill(COLOR_BLACK)

    mov_speed = 5 * delta / 1000 * FPS

    """ Gestion des évènements """
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key_pressed[K_ESCAPE]:
            running = False
        
    # Gestion de l'appluie des flêches directionnelles du clavier pour bouger notre carré
    if key_pressed[K_UP]:
        square.y -= mov_speed
    elif key_pressed[K_DOWN]:
        square.y += mov_speed
    if key_pressed[K_LEFT]:
        square.x -= mov_speed
    elif key_pressed[K_RIGHT]:
        square.x += mov_speed
    
    """ Logique du jeu """
    pygame.draw.rect(screen, COLOR_RED, square)

    """ Rendu de l'écran """ 
    pygame.display.flip()

    delta = clock.tick(30)

pygame.quit()
exit()