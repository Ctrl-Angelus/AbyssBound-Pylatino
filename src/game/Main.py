import pygame

from src.game.Gestion.AdministradorDeEntidades import AdministradorDeEntidades
from src.game.Clases.Jugador import Jugador
from src.game.Gestion.Contexto import ContextoDelJuego
from src.game.Gestion.Controlador import Controlador
from src.game.Gestion.Parametros import FPS, DIMENSIONES_DEL_LIENZO


def main():
    contexto = ContextoDelJuego()

    jugador = Jugador(contexto)

    administrador_de_entidades = AdministradorDeEntidades(contexto, jugador)
    administrador_de_entidades.generar_oleada(20)
    contexto.entidades.append(jugador)

    controlador = Controlador(contexto, jugador)

    while contexto.ejecutando:

        for evento in pygame.event.get():
            controlador.verificar_eventos(evento)

        controlador.verificar_controles()

        contexto.escenario.mostrar()

        for entidad in contexto.entidades:
            if entidad is not jugador:
                entidad.movimiento()
            if contexto.offset[0] <= entidad.cuerpo.right and entidad.cuerpo.left <= DIMENSIONES_DEL_LIENZO[0] + contexto.offset[0] and contexto.offset[1] <= entidad.cuerpo.bottom and entidad.cuerpo.top <= DIMENSIONES_DEL_LIENZO[1] + contexto.offset[1]:
                contexto.escena.blit(entidad.sprite, entidad.obtener_posicion())

        contexto.escena.blit(jugador.sprite, jugador.obtener_posicion())

        pygame.display.flip()
        contexto.reloj.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
