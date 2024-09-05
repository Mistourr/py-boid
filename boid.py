import pygame
from pygame import Vector2, Vector3
from drawable import Drawable
from math import cos, sin, atan2, pi
import time

class Boid(Drawable):

    # DO NOT TOUCH

    #config vars
    _size: float = 10
    _color: Vector3 = (255, 255, 255)
    _n_neighbours = 3
    _sep_distance = 35
    _speed = 100

    def __init__(self, x:float, y:float) -> None:
        super().__init__()
        self._pos: Vector2 = Vector2(x, y)
        self._vel: Vector2 = Vector2(1,0)

    def getPos(self) -> Vector2:
        return self._pos

    def setPos(self, x: float, y: float):
        self._pos = Vector2(x, y)

    def getVelocity(self):
        return self._vel
    
    def setVelocity(self, vel: Vector2):
        self._vel = vel

    def move(self, delta: float):
        self._pos = self._pos + self._vel * delta * self._speed
    
    def draw(self, screen):
        _dir = atan2(self._vel.y, self._vel.x)
        triangle = [
            Vector2(cos(_dir) * self._size, sin(_dir) * self._size),
            Vector2(cos(_dir + pi * (3/4)) * self._size, sin(_dir + pi * (3/4)) * self._size),
            Vector2(cos(_dir + pi * (5/4)) * self._size, sin(_dir + pi * (5/4)) * self._size)
        ]
        points = [(p.x + self._pos.x, p.y + self._pos.y) for p in triangle]
        pygame.draw.polygon(screen, self._color, points)

    # ----------------------------------------------------
    # TODO: Add boid logic methods here :
    
    def separation(self, boids: list['Boid']) -> Vector2:
        sep_force = Vector2(0, 0)
        count = 0
        for boid in boids:
            if boid == self:
                continue
            dist = self._pos.distance_to(boid._pos)
            if dist < self._sep_distance:
                sep_force += (self._pos - boid._pos)
                count += 1
        
        if count > 0:
            return (sep_force / count).normalize()
        else:
            return sep_force

    def alignement(self, boids: list['Boid']) -> Vector2:
        mean: Vector2 = Vector2(0,0)
        for boid in boids:
            if boid == self:
                continue
            mean += boid.getVelocity()
        mean /= len(boids)
        return mean.normalize()
    
    def cohesion(self, boids: list['Boid']) -> Vector2:
        mean: Vector2 = Vector2(0,0)
        for boid in boids:
            if boid == self:
                continue
            mean += boid.getPos()
        mean /= len(boids)
        return mean.normalize()
    
    def circling(self, w, h):
        return ( (Vector2(w/2, h/2) + Vector2(cos(time.time()), sin(time.time()))) - self._pos).normalize()