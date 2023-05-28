from typing import Any
import pygame as py
from settings import *

class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        #setup
        self.image = py.Surface((WINDOW_WIDTH // 10, WINDOW_HEIGHT// 20))
        self.image.fill('red')

        #position
        self.rect = self.image.get_rect(midbottom = (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT - 20))
        self.direction = py.math.Vector2()
        self.pos = py.math.Vector2(self.rect.topleft)
        self.speed = 300

    def input(self):
        keys = py.key.get_pressed()
        if keys[py.K_RIGHT]:
            self.direction.x = 1
        elif keys[py.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self, dt):
        self.input()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)

