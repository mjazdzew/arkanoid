import random
from collections.abc import Callable

import pygame
from enemy import Enemy
from constants import *

Edge = tuple[pygame.Vector2, Callable[[float], pygame.Vector2]]

class EnemyGenerator(pygame.sprite.Sprite):
    containers: pygame.sprite.Group

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 1.0

    def spawn(self, position: pygame.Vector2, velocity: pygame.Vector2) -> None:
        enemy = Enemy(position.x, position.y)
        enemy.velocity = velocity

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > ENEMY_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0

            # spawn a new enemy at a random position at the top
            positon_x = random.randint(2 + (PLAYER_WIDTH // 2), SCREEN_WIDTH - (2 + (PLAYER_WIDTH // 2)))
            position = pygame.Vector2(positon_x, PLAYER_HEIGTH / 2)
            speed = random.randint(ENEMY_SPEED_AVERAGE - 50, ENEMY_SPEED_AVERAGE + 50)
            velocity = pygame.Vector2(0, speed)
            self.spawn(position, velocity)