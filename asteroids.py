import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius<ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle=random.uniform(20,50)
            positive_velocity= self.velocity.rotate(random_angle)*1.2
            negative_velocity = self.velocity.rotate(-random_angle)*1.2
            new_radius = self.radius- ASTEROID_MIN_RADIUS
            new_asteriod_1= Asteroid(self.position.x, self.position.y, new_radius)
            new_asteriod_1.velocity=positive_velocity
            new_asteriod_2= Asteroid(self.position.x, self.position.y, new_radius)
            new_asteriod_2.velocity=negative_velocity



            radius -= ASTEROID_MIN_RADIUS
    
     