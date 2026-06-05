import pygame
from squareshape import SquareShape
from shots import EnemyShot
from constants import PLAYER_HEIGTH, PLAYER_WIDTH, LINE_WIDTH, ENEMY_SHOT_SPEED_BONUS, ENEMY_SHOOT_COOLDOWN_SECONDS

class Enemy(SquareShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_HEIGTH, PLAYER_WIDTH)
        self.shot_timer = 0.7

    def triangle(self) -> list[pygame.Vector2]:
        a = self.position + pygame.Vector2(0, self.heigth / 2)
        b = self.position + pygame.Vector2(self.width / 2, (-1) * self.heigth / 2)
        c = self.position + pygame.Vector2((-1) * self.width / 2, (-1) * self.heigth / 2)
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "purple", self.triangle(), LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.shot_timer -= dt
        self.position += self.velocity * dt
        if self.shot_timer <= 0:
            self.shoot()
            self.shot_timer = ENEMY_SHOOT_COOLDOWN_SECONDS

    def shoot(self) -> None:
        shot = EnemyShot(self.position[0], self.position[1] + (self.heigth / 2))
        shot.velocity = self.velocity + pygame.Vector2(0, ENEMY_SHOT_SPEED_BONUS)
