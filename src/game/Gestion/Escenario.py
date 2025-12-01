from src.game.Sprites.Sprite import Sprite
from src.game.Sprites.SpriteSheet import SpriteSheet
from src.game.Gestion.Parametros import DIMENSIONES_DEL_LIENZO


class Escenario:
    def __init__(self, contexto):
        self.contexto = contexto
        self.fondo = Sprite("src/recursos/fondo.png", None, None)

        self.fondo.cuerpo.x = -(self.fondo.width - DIMENSIONES_DEL_LIENZO[0]) / 2
        self.fondo.cuerpo.y = -(self.fondo.height - DIMENSIONES_DEL_LIENZO[1]) / 2

        self.fondo_estatico = SpriteSheet("src/recursos/fondo-estatico.png")
        self.fondo_estatico.generar_frames(4, 1, (60, 60), 1)
        self.fondo_estatico.iniciar_animacion()


    def mostrar(self):
        sprite = self.fondo_estatico.obtener_sprite_actual()
        self.contexto.escena.blit(
            sprite.imagen,
            sprite.cuerpo)

        self.fondo_estatico.animacion(0)
        self.contexto.escena.blit(self.fondo.imagen, self.fondo.cuerpo)
