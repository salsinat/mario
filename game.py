import pygame
from pygame.locals import * # type: ignore
from pygame.time import Clock

from entities.player import Player

FPS = 60

class Game:
    def __init__(self):
        self.__running = False
        self.__clock = Clock()
        self.__delta = 0
        self.__screen = pygame.display.set_mode((400, 300))

        self.__player = Player(5, 5)
        pygame.display.set_caption("MARIO BROS")

    @property
    def running(self) -> bool:
        return self.__running

    def run(self):
        self.__running = True
    
    def __handle_events(self):
        key_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT or key_pressed[K_ESCAPE]:
                self.__running = False
        
        self.__player.handle_events()

    def __update(self):
        self.__player.update_delta(self.__delta)
        self.__delta = self.__clock.tick(FPS)

    def __draw(self):
        self.__screen.fill(Color(0, 0, 0))
        self.__player.render(self.__screen)
        pygame.display.flip()

    def loop(self):
        self.__handle_events()
        self.__update()
        self.__draw()