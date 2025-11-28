import pygame
from pygame.rect import Rect

from Entidades import Jugador
from Parametros import *


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    fondo = pygame.image.load("src/recursos/fondo-prueba.png").convert()
    factor = DIMENSIONES_DEL_LIENZO[1] / (fondo.get_height() / 2)
    fondo_escalado = pygame.transform.scale(
        fondo,
        (
            fondo.get_width() * factor,
            fondo.get_height() * factor
        )
    )

    fondo_escalado_rect = fondo_escalado.get_rect()
    fondo_escalado_rect.x = -(fondo_escalado.get_width() - DIMENSIONES_DEL_LIENZO[0]) / 2
    fondo_escalado_rect.y = -(fondo_escalado.get_height() - DIMENSIONES_DEL_LIENZO[1]) / 2

    posicion_inicial = (DIMENSIONES_DEL_LIENZO[0] / 2) - (MEDIDA_DE_TILE / 2)

    jugador = Jugador(Rect(posicion_inicial, posicion_inicial, MEDIDA_DE_TILE, MEDIDA_DE_TILE), VELOCIDAD)

    escena.blit(fondo_escalado, fondo_escalado_rect)

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas_presionadas = pygame.key.get_pressed()

        if teclas_presionadas[jugador.controles.get("adelante")]:
            posicion_mouse = pygame.mouse.get_pos()

            jugador.mover(posicion_mouse, fondo_escalado_rect)

        escena.fill((0,0,0))
        escena.blit(fondo_escalado, fondo_escalado_rect)

        pygame.draw.rect(escena, (0, 0, 255), jugador.cuerpo)
        pygame.display.flip()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
