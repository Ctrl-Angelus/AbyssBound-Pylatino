import pygame.image

from src.game.Gestion.Contexto import ContextoDelJuego


class Proyectil:
    def __init__(self, contexto: ContextoDelJuego, url, ancho: int, alto: float, movimiento: tuple, posicion_inicial: tuple):

        imagen = pygame.image.load(url).convert_alpha()
        escalado = [
            imagen.get_height() * (alto / imagen.get_height()),
            imagen.get_width() * (ancho / imagen.get_width())
        ]
        self.sprite = pygame.transform.scale(imagen, escalado)

        self.cuerpo = self.sprite.get_rect().inflate(-10, -10)

        self.cuerpo.x = posicion_inicial[0]
        self.cuerpo.y = posicion_inicial[1]

        self.contexto = contexto

        self.movimiento = movimiento
        self.puntos_de_daño = 10

        self.viva = True

    def mover(self):
        self.cuerpo.move_ip(
            self.movimiento[0],
            self.movimiento[1]
        )
        tile_actual = self.contexto.escenario.tile_map.obtener_tile_actual(self.cuerpo)
        if tile_actual is None:
            self.eliminar()

        tiles = self.contexto.escenario.tile_map.obtener_tiles_cercanos(self.cuerpo)

        for tile in tiles:
            if tile is None:
                continue
            if tile.colision:
                collide = self.cuerpo.colliderect(tile.cuerpo)
                if collide:
                    self.eliminar()

        for entidad in self.contexto.entidades:
            if entidad is self.contexto.jugador:
                continue

            collide = self.cuerpo.colliderect(entidad.cuerpo)

            if collide:
                if entidad.entidad_viva:
                    entidad.iniciar_empuje(self.movimiento[0], self.movimiento[1])
                    entidad.realizar_daño(self.puntos_de_daño)

    def mostrar(self):
        if self.viva:
            self.contexto.escena.blit(self.sprite, self.obtener_posicion_visual())
        else:
            self.contexto.proyectiles.remove(self)

    def eliminar(self):
        self.viva = False

    def obtener_posicion_visual(self) -> tuple:
        return self.cuerpo.x - self.contexto.offset[0], self.cuerpo.y - self.contexto.offset[1]