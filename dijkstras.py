import pygame
from graph import Graph
import numpy as np
import math


if __name__ == "__main__":

    screen = pygame.display.set_mode((800, 800))
    running = True

    g = Graph()
    g.add_node(1)  # 0
    g.add_node(2, 0)  # 1
    g.add_node(3, 0, 1)  # 2
    g.add_node(6, 0, 2)  # 3
    g.add_node(5, 3)  # 4
    g.add_node(4, 1, 2, 4)  # 5

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False

        screen.fill((0, 0, 0))

        g.draw(screen)

        pygame.display.flip()
    pygame.quit()
