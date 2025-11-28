import pygame
from pygame import Rect
from Colisiones import colision_limite
from Parametros import MEDIDA_DE_TILE
from Movimiento import movimiento_respecto_al_mouse


class Jugador:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo: Rect = cuerpo
        self.velocidad: float = velocidad

        self.controles = {
            "adelante" : pygame.K_w
        }

    def mover(self, posicion_mouse: tuple) -> None:
        desplazamiento: tuple = movimiento_respecto_al_mouse(
            self.velocidad,
                (
                    self.cuerpo.x + MEDIDA_DE_TILE / 2,
                    self.cuerpo.y + MEDIDA_DE_TILE / 2
                ),
                posicion_mouse
            )

        if colision_limite(self.cuerpo, tuple(desplazamiento)):
            return
        else:
            self.cuerpo.move_ip(
                desplazamiento[0],
                desplazamiento[1]
            )
