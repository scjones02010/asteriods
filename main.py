import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *

def main():
    pygame.init()
    clock= pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (asteroid_field, updatable)
    asteroid_field = AsteroidField()   
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


    running= True
    dt=0

    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
             
    
    while running:
        tick = clock.tick(60)
        dt= tick/1000
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        
        for sprite in updatable:
            sprite.update(dt)
        
        screen.fill((0,0,0))
        
        for sprite in drawable:
            sprite.draw(screen)
        
        for asteriod in asteroids:
            if asteriod.collision_detection(player):
                print('Game Over')
                return

        pygame.display.flip()

    return

if __name__=='__main__':
    main()