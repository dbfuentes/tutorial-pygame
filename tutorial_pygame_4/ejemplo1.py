#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Escrito por Daniel Fuentes B.
# Licencia: X11/MIT license http://www.opensource.org/licenses/mit-license.php
# http://pythonmania.wordpress.com/2010/07/14/tutorial-pygame-4-figuras-y-texto

# ---------------------------
# Importación de los módulos
# ---------------------------

import pygame
from pygame.locals import *
import sys

# -----------
# Constantes
# -----------

WIDTH = 640
HEIGHT = 480

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------


# ------------------------------
# Función principal del juego
# ------------------------------


def main():
    pygame.init()
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("tutorial pygame parte 4")

    # el bucle principal del juego
    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()

        # Re dibujar los elementos en pantalla
        screen.fill((30, 145, 255))
        pygame.draw.line(screen, (255, 255, 255), (0, 25), (640, 25), 2)
        # actualizamos la pantalla
        pygame.display.flip()


if __name__ == "__main__":
    main()
