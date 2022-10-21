import pygame
import random

pygame.init()

FONT = pygame.font.SysFont(None, 24)

WHITE = (255, 255, 255)


class Graph:
    class Node:
        def __init__(
            self,
            val: any = None,
            x: int = 0,
            y: int = 0,
            color: tuple[int, int, int] = (0, 0, 0),
            *connected
        ):
            self.val = val
            self.x = x
            self.y = y
            self.color = color
            self.radius = 25
            self.connected: list[Graph.Node] = []
            for node in connected:
                assert type(node) is Graph.Node
                self.connected.append(node)
                node.connected.append(self)
            font = FONT.render(str(self.val), True, WHITE)
            if font.get_width() > self.radius * 4:
                font = pygame.transform.scale(
                    font, (self.radius * 4, font.get_height())
                )
            self.text = pygame.surface.Surface((font.get_width(), font.get_height()))
            self.text.fill((0, 0, 0))
            self.text.blit(font, (0, 0))

        def print_connections(self):
            print(self.val, "is connected to ", end="")
            for c in self.connected:
                print(c.val, end=" ")
            print()

        def draw_self(self, screen):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
            screen.blit(
                self.text,
                (
                    self.x - (self.text.get_width() / 2),
                    self.y - (self.text.get_height() / 2),
                ),
            )

        def draw_lines(self, screen):
            for c in self.connected:
                pygame.draw.line(screen, WHITE, (self.x, self.y), (c.x, c.y))

    def __init__(self, *nodes) -> None:
        self.nodes: list[Graph.Node] = []
        for n in nodes:
            self.nodes.append(n)

    def r_pos(self):
        return random.randrange(50, 751, 100)

    def r_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def r_node(self):
        return self.r_pos(), self.r_pos(), self.r_color()

    def add_node(self, val=None, *linked_indexes):
        nodes = []
        for i in linked_indexes:
            nodes.append(self.nodes[i])
        self.nodes.append(Graph.Node(val, *self.r_node(), *nodes))

    def print_connections(self):
        for n in self.nodes:
            n.print_connections()

    def draw_nodes(self, screen):
        for n in self.nodes:
            n.draw_self(screen)

    def draw_lines(self, screen):
        for n in self.nodes:
            n.draw_lines(screen)

    def draw(self, screen):
        self.draw_lines(screen)
        self.draw_nodes(screen)
