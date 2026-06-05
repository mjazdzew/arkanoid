import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_HEIGTH
from player import Player
from shots import PlayerShot, EnemyShot
from enemy import Enemy
from enemygenerator import EnemyGenerator

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    enemy_shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    PlayerShot.containers = (player_shots, updatable, drawable)
    Enemy.containers = (enemies, updatable, drawable)
    EnemyGenerator.containers = (updatable)
    EnemyShot.containers = (enemy_shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - (PLAYER_HEIGTH / 2))
    enemy_generator = EnemyGenerator()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
