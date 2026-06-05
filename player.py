import pygame
from squareshape import SquareShape
from shots import PlayerShot
from constants import PLAYER_HEIGTH, PLAYER_WIDTH, LINE_WIDTH, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS

class Player(SquareShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_HEIGTH, PLAYER_WIDTH)
        self.shot_timer = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        a = self.position + pygame.Vector2(0, (-1) * self.heigth / 2)
        b = self.position + pygame.Vector2(self.width / 2, self.heigth / 2)
        c = self.position + pygame.Vector2((-1) * self.width / 2, self.heigth / 2)
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "yellow", self.triangle(), LINE_WIDTH)

    def move(self, dt: float) -> None:
        self.position += pygame.Vector2(1, 0) * PLAYER_SPEED * dt

    def update(self, dt: float) -> None:
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.move((-1) * dt)

        if keys[pygame.K_SPACE]:
            if self.shot_timer <= 0:
                self.shoot()
                self.shot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

    def shoot(self) -> None:
        shot = PlayerShot(self.position[0], self.position[1] - (self.heigth / 2))
        shot.velocity = pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED * (-1)
