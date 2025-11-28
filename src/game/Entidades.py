import pygame
from pygame import Rect
from Parametros import MEDIDA_DE_TILE
from Movimiento import movimiento_respecto_al_mouse


class Jugador:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo: Rect = cuerpo
        self.velocidad: float = velocidad

        self.controles = {
            "adelante" : pygame.K_w
        }

    def mover(self, posicion_mouse: tuple, fondo: Rect) -> None:
        desplazamiento: tuple = movimiento_respecto_al_mouse(
            self.velocidad,
                (
                    self.cuerpo.x + MEDIDA_DE_TILE / 2,
                    self.cuerpo.y + MEDIDA_DE_TILE / 2
                ),
                posicion_mouse
            )

        fondo.x -= desplazamiento[0]
        fondo.y -= desplazamiento[1]
