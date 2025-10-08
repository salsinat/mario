import pygame
import sys

from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()  

    game.run()

    while game.running:
        game.loop()

    pygame.quit()
    sys.exit()