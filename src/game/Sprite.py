import pygame
from pygame import Rect, Surface
from Parametros import *


class Sprite:
    def __init__(self, ruta: str, tiles_x: int, tiles_y: int):
        self.ruta: str = ruta

        imagen: Surface = pygame.image.load(self.ruta).convert()


        self.escalado = (
                TAMAÑO_TILE_ORIGINAL * (MEDIDA_DE_TILE / TAMAÑO_TILE_ORIGINAL) * tiles_x,
                TAMAÑO_TILE_ORIGINAL * (MEDIDA_DE_TILE / TAMAÑO_TILE_ORIGINAL) * tiles_y
        )

        self.imagen: Surface = pygame.transform.scale(imagen, (
            self.escalado[0],
            self.escalado[1]
        ))

        self.width = self.imagen.get_width()
        self.height = self.imagen.get_height()

        self.cuerpo: Rect = self.imagen.get_rect()