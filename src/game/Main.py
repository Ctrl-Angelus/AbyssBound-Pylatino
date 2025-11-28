import pygame
from pygame.rect import Rect

from Entidades import Jugador
from Parametros import *


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    posicion_inicial = (DIMENSIONES_DEL_LIENZO[0] / 2) - (MEDIDA_DE_TILE / 2)

    jugador = Jugador(Rect(posicion_inicial, posicion_inicial, MEDIDA_DE_TILE, MEDIDA_DE_TILE), VELOCIDAD)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas_presionadas = pygame.key.get_pressed()
        posicion_mouse = pygame.mouse.get_pos()

        jugador.mover(teclas_presionadas, posicion_mouse)

        escena.fill((0, 0, 0))
        pygame.draw.rect(escena, (0, 0, 255), jugador.cuerpo, 0, 100)
        pygame.display.flip()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
