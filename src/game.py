import sys

import pygame as pg
from pygame.locals import *

from .layer import LayerStack
from .entity import Player
from .terrain import Terrain

class Game(object):
    def __init__(self, width=1280, height=720, scale=1) -> None:
        pg.init()

        self.window = pg.display.set_mode((width, height), 0, 32)
        pg.display.set_caption('Masita')
        self.display = pg.Surface((self.window.get_width() / scale, self.window.get_height() / scale))

        self.layer_stack = LayerStack()
        self.layer_stack.push_layer(Player())

        self.terrain = Terrain()

        self.running = True
        self.clock = pg.time.Clock()

    def on_event(self) -> None:
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False

            for layer in self.layer_stack.get()[::-1]:
                layer.__on_event__(event)

    def on_update(self) -> None:
        for layer in self.layer_stack.get():
            layer.__on_update__()
        
        self.clock.tick(60)

    def on_render(self) -> None:
        self.display.fill((121, 121, 121))

        for layer in self.layer_stack.get():
            layer.__on_render__(self.display)

        self.window.blit(pg.transform.scale(self.display, (self.window.get_width(), self.window.get_height())), (0, 0))
        pg.display.update()

        pg.display.set_caption(f'Masita - {int(self.clock.get_fps())} fps')

    def close(self) -> None:
        self.layer_stack.clean()
        del self.display
        del self.window

        pg.quit()
        sys.exit()
