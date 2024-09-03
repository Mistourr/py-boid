import pygame
from drawable import Drawable
from math import cos, sin, atan2, pi

class Boid(Drawable):

    # DO NOT TOUCH

    #config vars
    size: float = 10
    color: tuple[int, int, int] = (255, 255, 255)

    def __init__(self) -> None:
        super().__init__()
        self._pos: tuple[float, float] = (500, 500)
        self._dir: float = 0

    def setPos(self, x: float, y: float):
        self._dir = atan2(y-self._pos[1], x-self._pos[0])
        self._pos = (x, y)
    
    def draw(self, screen):        
        triangle = [
            (cos(self._dir) * self.size, sin(self._dir) * self.size),
            (cos(self._dir + pi * (3/4)) * self.size, sin(self._dir + pi * (3/4)) * self.size),
            (cos(self._dir + pi * (5/4)) * self.size, sin(self._dir + pi * (5/4)) * self.size)
        ]
        points = [(p[0] + self._pos[0], p[1] + self._pos[1]) for p in triangle]
        pygame.draw.polygon(screen, self.color, points)

    # ----------------------------------------------------
    # TODO: Add boid logic methods here :
    