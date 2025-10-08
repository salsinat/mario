import pygame
from pygame import Surface
from pygame.locals import * # type: ignore

from entities.entity import Entity
from gameloop_interface import GameLoopInterface

class Player(Entity, GameLoopInterface):
    def __init__(self, pos_x:int, pos_y:int):
        image = pygame.image.load("assets/images/mario/stand/0.gif").convert_alpha()
        image.set_colorkey((255, 0, 255))

        super().__init__(pos_x, pos_y, image)

        self.__move_speed = 0
    
    @property
    def move_speed(self) -> float:
        return self.__move_speed
    
    @move_speed.setter
    def move_speed(self, value:float):
        self.__move_speed = value
    
    def update_delta(self, delta:float):
        self.move_speed = delta * 0.15

    def render(self, screen:Surface):
        screen.blit(self.image, (self.x, self.y))

    def handle_events(self):
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            self.x += int(self.move_speed)
        if keys[K_LEFT]:
            self.x -= int(self.move_speed)
        if keys[K_UP]:
            self.y -= int(self.move_speed)
        if keys[K_DOWN]:
            self.y += int(self.move_speed)

