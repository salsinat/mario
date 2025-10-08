from abc import ABC

from pygame import Surface
from pygame.sprite import Sprite

class Entity(Sprite, ABC):
    def __init__(self, pos_x:int, pos_y:int, image:Surface):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.__x = pos_x
        self.__y = pos_y

    @property
    def x(self) -> int:
        return self.__x
    
    @x.setter
    def x(self, value:int):
        self.__x = value
        self.rect.x = value
    
    @property
    def y(self) -> int:
        return self.__y 
    
    @y.setter
    def y(self, value:int):
        self.__y = value
        self.rect.y = value