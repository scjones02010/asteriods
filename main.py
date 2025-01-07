import pygame
from constants import *

def main():
    pygame.init()
    clock= pygame.time.Clock()
    dt=0
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
    running= True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        clock.tick(60)
        dt= (dt - clock.tick())/1000  
        screen.fill((0,0,0))
        pygame.display.flip()



    return

if __name__=='__main__':
    main()