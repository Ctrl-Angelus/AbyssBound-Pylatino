import math

import pygame
from pygame import Rect


class Entidad:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo = cuerpo
        self.velocidad = velocidad

        self.controles = {
            pygame.K_a: (-self.velocidad, 0),
            pygame.K_d: (self.velocidad, 0),
            pygame.K_w: (0, -self.velocidad),
            pygame.K_s: (0, self.velocidad)
        }


    def mover(self, keys) -> None:
        teclas_presionadas = 0
        for clave, valor in self.controles.items():
            if keys[clave]:
                teclas_presionadas += 1

        if teclas_presionadas >= 2:
            factor = math.sin(math.radians(45))
        else:
            factor = 1

        for clave, valor in self.controles.items():
            if keys[clave]:
                self.cuerpo.move_ip(valor[0] * factor, valor[1] * factor)
