import pygame
from typing import Self

# Base class for game objects
class SquareShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, heigth: float, width: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.heigth = heigth
        self.width = width


    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def rectangle(self) -> list[pygame.Vector2]:
        a = self.position + pygame.Vector2(self.width / 2, (-1) * self.heigth / 2)
        b = self.position + pygame.Vector2(self.width / 2, self.heigth / 2)
        c = self.position + pygame.Vector2((-1) * self.width / 2, self.heigth / 2)
        d = self.position + pygame.Vector2((-1) * self.width / 2, (-1) * self.heigth / 2)

        return [a, b, c, d]

    def collides_with(self, other: Self) -> bool:
        if self.position.distance_to(other.position) <= self.width + other.width:
            return True
        return False