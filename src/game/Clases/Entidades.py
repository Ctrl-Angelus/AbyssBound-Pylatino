import pygame
from pygame import Rect, Surface

from src.game.Movimiento.Movimiento import movimiento_relativo, mover_fondo
from src.game.Colisiones.Colisiones_borde import colision_borde_jugador
from src.game.Colisiones.Colisiones_borde import colision_borde_enemigos
from src.game.Colisiones.Colisiones_entidades import colisiones_con_entidades
from src.game.Parametros import MEDIDA_DE_TILE


class Entidad:
    def __init__(self, posicion_inicial: tuple, alto, ancho, velocidad: float, url: str):

        self.url: str = url
        self.imagen: Surface = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (alto / self.imagen.get_width()),
                self.imagen.get_height() * (ancho / self.imagen.get_height()),
            )
        )

        self.cuerpo: Rect = self.sprite.get_rect()
        self.velocidad: float = velocidad

        self.cuerpo.move_ip(posicion_inicial)

class Enemigo(Entidad):

    def __init__(self, posicion_inicial: tuple, alto, ancho, velocidad: float, url: str, objetivo: tuple):
        super().__init__(posicion_inicial, alto, ancho, velocidad, url)

        self.objetivo: tuple = objetivo

    def mover(self, fondo: Rect, direccion: int, entidades: list, jugador):
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
            self.cuerpo.center,
            self.objetivo
        )

        movimiento_x, movimiento_y = colision_borde_enemigos(self.cuerpo, desplazamiento, fondo, direccion)

        colisiones_con_entidades(self, movimiento_x, movimiento_y, entidades, jugador)

class Jugador(Entidad):
    controles = {
        "adelante": pygame.K_w,
        "atrás" : pygame.K_s,
        "click": pygame.MOUSEBUTTONDOWN
    }

    def mover(self, posicion_mouse: tuple, fondo: Rect, direccion: int, entidades: list[Enemigo]) -> None:
        desplazamiento: tuple = movimiento_relativo(
            self.velocidad,
                self.cuerpo.center,
                posicion_mouse
            )

        movimiento_x, movimiento_y = colision_borde_jugador(self.cuerpo, desplazamiento, fondo, direccion)

        correccion_x = 0
        correccion_y = 0

        mover_fondo(fondo, entidades, movimiento_x, 0)

        for entidad in entidades:
            colision = self.cuerpo.colliderect(entidad.cuerpo)

            if colision:
                if movimiento_x > 0:
                    correccion_x = self.cuerpo.left - entidad.cuerpo.right

                elif movimiento_x < 0:
                    correccion_x = self.cuerpo.right - entidad.cuerpo.left

                mover_fondo(fondo, entidades, correccion_x, 0)

        mover_fondo(fondo, entidades, 0, movimiento_y)

        for entidad in entidades:
            colision = self.cuerpo.colliderect(entidad.cuerpo)

            if colision:
                if movimiento_y > 0:
                    correccion_y = self.cuerpo.top - entidad.cuerpo.bottom

                elif movimiento_y < 0:
                    correccion_y = self.cuerpo.bottom - entidad.cuerpo.top

                mover_fondo(fondo, entidades, 0, correccion_y)


