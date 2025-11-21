import pygame
from pygame.rect import Rect
import sys

from Entidades import Entidad

screen_size = [800, 800]


def main():
    pygame.init()
    pygame.display.set_caption("Proyecto Pylatino")

    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()

    jugador = Entidad(Rect(10, 10, 50, 50), 5.0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        jugador.mover(keys)

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 255), jugador.cuerpo, 0, 100)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
