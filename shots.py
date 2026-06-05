import pygame
from squareshape import SquareShape
from constants import LINE_WIDTH, SHOT_WIDTH

class PlayerShot(SquareShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_WIDTH * 2, SHOT_WIDTH)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "red", self.rectangle(), LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

class EnemyShot(SquareShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_WIDTH * 2, SHOT_WIDTH)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "green", self.rectangle(), LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt