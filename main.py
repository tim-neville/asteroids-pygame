import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import *
from asteroidfield import AsteroidField
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x,y)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        if (pygame.key.get_pressed())[pygame.K_q]:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        screen.fill("black")
        
        updatable.update(dt)

        for asteroid in asteroids:
            if (asteroid.check_is_collision(player)):
                print("Game over!")
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            for shot in shots:
                if (asteroid.check_is_collision(shot)):
                    asteroid.split()
                    shot.kill()


        for unit in drawable:
            unit.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000 #convert  milliseconds to seconds


if __name__ == "__main__":
    main()
