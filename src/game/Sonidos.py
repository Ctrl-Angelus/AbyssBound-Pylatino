import pygame
from random import randint


def sonido_golpe():
    version_audio = randint(1, 3)
    golpe = pygame.mixer.Sound(f"src/recursos/audio/efectos/golpe-{version_audio}.mp3")
    golpe.set_volume(0.2)

    golpe.play()

def sonido_muerte():
    muerte = pygame.mixer.Sound("src/recursos/audio/efectos/golpe-letal.mp3")

    muerte.set_volume(0.4)

    muerte.play()

def sonido_choque_proyectil():
    choque = pygame.mixer.Sound("src/recursos/audio/choque-proyectil.mp3")

    choque.set_volume(0.2)

    choque.play()

def sonido_dash():
    dash = pygame.mixer.Sound("src/recursos/audio/dash.mp3")

    dash.set_volume(0.2)

    dash.play()