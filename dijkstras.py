import pygame
from graph import Graph
import numpy as np
import math


def graph_gen() -> Graph:
    g = Graph()
    g.add_positional_node(1, 100, 700)  # 0
    g.add_positional_node(2, 300, 750, 0)  # 1
    g.add_positional_node(3, 350, 350, 0, 1)  # 2
    g.add_positional_node(6, 150, 150, 0, 2)  # 3
    g.add_positional_node(5, 600, 100, 3)  # 4
    g.add_positional_node(4, 750, 350, 1, 2, 4)  # 5
    return g


def main() -> None:
    screen = pygame.display.set_mode((800, 800))
    running = True

    g = graph_gen()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if keys[pygame.K_LSHIFT]:
                g = graph_gen()

        screen.fill((0, 0, 0))

        g.draw(screen)

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
