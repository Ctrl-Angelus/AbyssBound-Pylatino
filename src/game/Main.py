import pygame
from pygame.rect import Rect

from Entidades import Jugador
from Parametros import *


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    jugador = Jugador(Rect(0, 0, MEDIDA_DE_TILE, MEDIDA_DE_TILE), VELOCIDAD)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas_presionadas = pygame.key.get_pressed()
        jugador.mover(teclas_presionadas)

        escena.fill((0, 0, 0))
        pygame.draw.rect(escena, (0, 0, 255), jugador.cuerpo, 0, 100)
        pygame.display.update()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
