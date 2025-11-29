import pygame
import random

from Entidades import Jugador, Entidad
from Parametros import *
from Imagen import Imagen


def main():
    pygame.init()

    pygame.display.set_caption(TITULO)

    escena = pygame.display.set_mode(DIMENSIONES_DEL_LIENZO)
    tiempo = pygame.time.Clock()

    fondo = Imagen(
        "src/recursos/fondo.png",
        60, 30
    )

    fondo_estatico = Imagen("src/recursos/fondo-estatico.png", TILES, TILES)

    fondo.cuerpo.x = -(fondo.width - DIMENSIONES_DEL_LIENZO[0]) / 2
    fondo.cuerpo.y = -(fondo.height - DIMENSIONES_DEL_LIENZO[1]) / 2

    posicion_inicial_x = escena.get_rect().center[0] - MEDIDA_DE_TILE / 2
    posicion_inicial_y = escena.get_rect().center[1] - MEDIDA_DE_TILE / 2

    jugador = Jugador(
        posicion_inicial_x, posicion_inicial_y, MEDIDA_DE_TILE, MEDIDA_DE_TILE,
        VELOCIDAD, "src/recursos/jugador.png"
    )

    enemigos = []

    for i in range(50):
        x = random.randint(fondo.cuerpo.left, int(fondo.cuerpo.right - MEDIDA_DE_TILE))
        y = random.randint(fondo.cuerpo.top, int(fondo.cuerpo.bottom - MEDIDA_DE_TILE))
        enemigos.append(
            Entidad(
                x, y, MEDIDA_DE_TILE, MEDIDA_DE_TILE,
                VELOCIDAD / 2, "src/recursos/enemigo.png")
        )

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        teclas_presionadas = pygame.key.get_pressed()
        if teclas_presionadas[jugador.controles.get("adelante")]:
            posicion_mouse = pygame.mouse.get_pos()

            jugador.mover(posicion_mouse, fondo.cuerpo, enemigos)

        escena.blit(fondo_estatico.imagen, fondo_estatico.cuerpo)
        escena.blit(fondo.imagen, fondo.cuerpo)

        for enemigo in enemigos:
            enemigo.mover(jugador.cuerpo.center, fondo.cuerpo, 1)
            escena.blit(enemigo.sprite, enemigo.cuerpo)

        escena.blit(jugador.sprite, jugador.cuerpo)

        pygame.display.flip()
        tiempo.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
