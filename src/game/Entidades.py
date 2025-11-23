import math

import pygame
from pygame import Rect
from Parametros import TAMAÑO

class Jugador:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo = cuerpo
        self.velocidad = velocidad

        self.controles = {
            pygame.K_a: (-self.velocidad, 0),
            pygame.K_d: (self.velocidad, 0),
            pygame.K_w: (0, -self.velocidad),
            pygame.K_s: (0, self.velocidad)
        }

    def colisiones(self, limites: list, movimiento: tuple) -> bool:
        colision_inicial_en_x: bool = self.cuerpo.x + movimiento[0] < 0
        colision_final_en_x: bool = self.cuerpo.x + TAMAÑO + movimiento[0] > limites[0]

        colision_inicial_en_y: bool = self.cuerpo.y + movimiento[1] < 0
        colision_final_en_y: bool = self.cuerpo.y + TAMAÑO + movimiento[1] > limites[1]

        colision_x: bool = colision_inicial_en_x or colision_final_en_x
        colision_y: bool = colision_inicial_en_y or colision_final_en_y

        return colision_x or colision_y

    def mover(self, teclas, limites: list) -> None:

        teclas_presionadas = 0
        for clave, valor in self.controles.items():
            if teclas[clave]:
                teclas_presionadas += 1

        if teclas_presionadas == 2:
            factor = math.sin(math.radians(45))
        else:
            factor = 1

        for clave, movimiento in self.controles.items():
            if teclas[clave]:

                if self.colisiones(limites, movimiento):
                    continue
                else:
                    self.cuerpo.move_ip(
                        movimiento[0] * factor,
                        movimiento[1] * factor
                    )