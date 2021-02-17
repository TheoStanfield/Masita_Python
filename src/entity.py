import pygame as pg
from pygame.locals import *

from .layer import Layer

class Player(Layer):
    def __init__(self, sprite:str='./assets/player.png', x:int=0, y:int=0, speed:float=2) -> None:
        self.image = pg.image.load(sprite)
        pg.Surface.set_colorkey(self.image, (255, 255, 255))

        self.obj = self.rect(x, y, self.image.get_width(), self.image.get_height())
        self.speed = speed
        self.movement = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }

    def __on_event__(self, event:pg.event.Event) -> bool:
        handled = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.movement['right'] = True
                handled = True

            if event.key == K_LEFT:
                self.movement['left'] = True
                handled = True

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                self.movement['right'] = False
                handled = True

            if event.key == K_LEFT:
                self.movement['left'] = False
                handled = True

        return handled

    def __on_update__(self) -> None:
        self.move()

    def __on_render__(self, display:pg.Surface) -> None:
        display.blit(self.image, (self.obj.x, self.obj.y))

    def rect(self, x:int, y:int, width:int, height:int) -> pg.Rect:
        return pg.Rect(x, y, width, height)

    def move(self) -> None:
        if self.movement['right']:
            self.obj.x += self.speed

        if self.movement['left']:
            self.obj.x -= self.speed
