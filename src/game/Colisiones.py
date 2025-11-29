from pygame import Rect


def desplazamiento_y_colision(objeto_estatico: Rect, desplazamiento: tuple, objeto_dinamico: Rect, direccion: int) -> tuple:

    simulacion: Rect = objeto_dinamico.move(
        desplazamiento[0] * direccion,
        desplazamiento[1] * direccion
    )

    # Se verifica si la versión simulada del fondo choca o sobrepasa las coordenadas del personaje
    colision_izquierda: bool = simulacion.left >= objeto_estatico.left
    colision_derecha: bool = simulacion.right <= objeto_estatico.right

    colision_arriba: bool = simulacion.top >= objeto_estatico.top
    colision_abajo: bool = simulacion.bottom <= objeto_estatico.bottom

    # El movimiento por defecto lo da el desplazamiento original, se modifica en caso de ser necesario
    movimiento_x: float = desplazamiento[0] * direccion
    movimiento_y: float = desplazamiento[1] * direccion

    # En caso de haber colisiones, se modifica el movimiento lo justo para que el personaje alcance el borde sin pasarlo
    if colision_izquierda:
        movimiento_x = objeto_estatico.left - objeto_dinamico.left

    elif colision_derecha:
        movimiento_x = objeto_estatico.right - objeto_dinamico.right

    if colision_arriba:
        movimiento_y = objeto_estatico.top - objeto_dinamico.top

    elif colision_abajo:
        movimiento_y = objeto_estatico.bottom - objeto_dinamico.bottom

    return movimiento_x, movimiento_y