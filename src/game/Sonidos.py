import pygame
from random import randint


def sonido_golpe():
    version_audio = randint(1, 3)
    canal_efectos = pygame.mixer.Channel(3)
    golpe = pygame.mixer.Sound(f"src/recursos/audio/efectos/golpe-{version_audio}.mp3")
    golpe.set_volume(0.2)

    canal_efectos.play(golpe)

def sonido_muerte():
    canal_efectos = pygame.mixer.Channel(3)
    muerte = pygame.mixer.Sound("src/recursos/audio/efectos/golpe-letal.mp3")

    muerte.set_volume(0.4)

    canal_efectos.play(muerte)

def sonido_proyectil():
    canal_efectos = pygame.mixer.Channel(1)
    choque = pygame.mixer.Sound("src/recursos/audio/proyectil.mp3")

    choque.set_volume(0.2)

    canal_efectos.play(choque)

def sonido_dash():
    canal_efectos = pygame.mixer.Channel(2)
    dash = pygame.mixer.Sound("src/recursos/audio/dash.mp3")

    dash.set_volume(0.1)

    canal_efectos.play(dash)