import pygame
from pygame import Rect
from Colisiones import colision_limite
from Parametros import MEDIDA_DE_TILE
from src.game.Movimiento import movimiento_respecto_al_mouse


class Jugador:
    def __init__(self, cuerpo: Rect, velocidad: float):
        self.cuerpo: Rect = cuerpo
        self.velocidad: float = velocidad

        self.controles = {
            "adelante" : pygame.K_w,
            "atras" : pygame.K_s,
            "derecha" : pygame.K_d,
            "izquierda" : pygame.K_a,
        }

    def mover(self, teclas, posicion_mouse: tuple) -> None:
        desplazamiento_total = [0, 0]

        for tecla, valor in self.controles.items():
            if teclas[valor]:
                cambio_en_x, cambio_en_y = movimiento_respecto_al_mouse(
                    self.velocidad,
                        (
                            self.cuerpo.x + MEDIDA_DE_TILE / 2,
                            self.cuerpo.y + MEDIDA_DE_TILE / 2
                         ),
                        posicion_mouse,
                        tecla
                    )
                desplazamiento_total[0] += cambio_en_x
                desplazamiento_total[1] += cambio_en_y

        if colision_limite(self.cuerpo, tuple(desplazamiento_total)):
            return
        else:
            self.cuerpo.move_ip(
                desplazamiento_total[0],
                desplazamiento_total[1]
            )
