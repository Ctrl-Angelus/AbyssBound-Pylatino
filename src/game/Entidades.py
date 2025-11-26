import math

import pygame
from pygame import Rect
from Colisiones import colision_limite

class Jugador:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo: Rect = cuerpo
        self.velocidad: float = velocidad

        self.controles = {
            pygame.K_w: (0, -self.velocidad),
            pygame.K_a: (-self.velocidad, 0),
            pygame.K_s: (0, self.velocidad),
            pygame.K_d: (self.velocidad, 0)
        }

    def mover(self, teclas) -> None:
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
                if colision_limite(self.cuerpo, movimiento):
                    continue
                else:
                    self.cuerpo.move_ip(
                        movimiento[0] * factor,
                        movimiento[1] * factor
                    )