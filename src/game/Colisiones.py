
from pygame import Rect
from Parametros import MEDIDA_DE_TILE, DIMENSIONES_DEL_LIENZO

def colision_limite(objeto: Rect, movimiento: tuple) -> bool:
    posicion_inicial_x = objeto.x
    posicion_inicial_y = objeto.y

    posicion_final_x = posicion_inicial_x + movimiento[0]
    posicion_final_y = posicion_inicial_y + movimiento[1]

    limite_x = DIMENSIONES_DEL_LIENZO[0] - MEDIDA_DE_TILE
    limite_y = DIMENSIONES_DEL_LIENZO[1] - MEDIDA_DE_TILE

    colision_inicial_x = posicion_final_x < 0
    colision_final_x = posicion_final_x > limite_x

    colision_inicial_y = posicion_final_y < 0
    colision_final_y = posicion_final_y > limite_y

    colision_x = colision_inicial_x or colision_final_x
    colision_y = colision_inicial_y or colision_final_y

    if colision_inicial_x:
        objeto.move_ip(0 - posicion_inicial_x, 0)
    elif colision_final_x:
        objeto.move_ip(limite_x - posicion_inicial_x, 0)

    if colision_inicial_y:
        objeto.move_ip(0, 0 - posicion_inicial_y)
    elif colision_final_y:
        objeto.move_ip(0, limite_y - posicion_inicial_y)

    return colision_x or colision_y