import pygame
from pygame import Rect, Surface
from src.game.Gestion.Parametros import MEDIDA_DE_TILE_ESCALADO
from src.game.Gestion.Contexto import ContextoDelJuego


class EntidadBase:
    def __init__(self, posicion_inicial: tuple, velocidad: float, url: str, contexto: ContextoDelJuego):

        alto = MEDIDA_DE_TILE_ESCALADO
        ancho = MEDIDA_DE_TILE_ESCALADO

        self.url: str = url
        self.imagen: Surface = pygame.image.load(url).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.imagen,
            (
                self.imagen.get_width() * (alto / self.imagen.get_width()),
                self.imagen.get_height() * (ancho / self.imagen.get_height()),
            )
        )
        self.cuerpo: Rect = self.sprite.get_rect().inflate(-10, -10)
        self.velocidad: float = velocidad

        self.cuerpo.move_ip(posicion_inicial)
        self.contexto = contexto

    def obtener_posicion(self) -> tuple:
        return self.cuerpo.centerx - self.contexto.offset[0], self.cuerpo.centery - self.contexto.offset[1]

    def mover(self, movimiento_x, movimiento_y) -> None:
        self.cuerpo.move_ip(movimiento_x, movimiento_y)