
import pygame
from pygame import Rect
from Movimiento import movimiento_relativo
from Colisiones import desplazamiento_y_colision
from Parametros import MEDIDA_DE_TILE


class Entidad:
    def __init__(self, posicion_inicial_x: float, posicion_inicial_y: float, alto, ancho, velocidad: float, url: str):

        self.imagen = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (alto / self.imagen.get_width()),
                self.imagen.get_height() * (ancho / self.imagen.get_height()),
            )
        )

        self.cuerpo: Rect = self.sprite.get_rect()
        self.velocidad: float = velocidad

        self.cuerpo.x = posicion_inicial_x
        self.cuerpo.y = posicion_inicial_y

    def mover(self, objetivo: tuple, fondo: Rect, direccion: int):
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
            self.cuerpo.center,
            objetivo,
            MEDIDA_DE_TILE
        )

        movimiento_x, movimiento_y = desplazamiento_y_colision(self.cuerpo, desplazamiento, fondo, direccion)

        self.cuerpo.move_ip(
            movimiento_x,
            movimiento_y
        )


class Jugador(Entidad):
    controles = {
        "adelante": pygame.K_w
    }

    def mover(self, posicion_mouse: tuple, fondo: Rect, entidades: list[Entidad]) -> None:
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
                self.cuerpo.center,
                posicion_mouse,
                10
            )

        movimiento_x, movimiento_y = desplazamiento_y_colision(self.cuerpo, desplazamiento, fondo, -1)

        for entidad in entidades:
            entidad.cuerpo.move_ip(
                movimiento_x, movimiento_y
            )

        fondo.move_ip(
            movimiento_x,
            movimiento_y
        )
