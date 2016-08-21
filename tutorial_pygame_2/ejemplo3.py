#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# https://www.pythonmania.net/es/2010/03/25/tutorial-pygame-2-ventana-e-imagenes/

# ---------------------------
# Importacion de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Funcion principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 2")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("fondo.jpg").convert()
    tux = pygame.image.load("tux.png").convert_alpha()

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(fondo, (0, 0))
    screen.blit(tux, (550, 200))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
