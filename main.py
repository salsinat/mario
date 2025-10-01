#!/usr/bin/env python

#-------------------------------------- IMPORTATION --------------------------------------#
from sys import exit # déclaration d'importation du module sys
import pygame # déclaration d'importation du module pygame

pygame.init() # initialisation du module pygame. Il est obligatoire d'appeler cette fonction une seule fois après l'avoir importé

#-------------------------------------- INITIALISATION FENÊTRE DE JEU --------------------------------------#

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("MARIO BROS")
