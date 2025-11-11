import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, LINE_WIDTH)  
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
    
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        pos = self.position
        vel = self.velocity
        rad = self.radius
        self.kill()
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        a1_velocity = vel.rotate(angle)
        a2_velocity = vel.rotate(-angle)
        new_radius = rad - ASTEROID_MIN_RADIUS
        a1 = Asteroid(pos.x, pos.y, new_radius)
        a1.velocity = a1_velocity * 1.2
        a2 = Asteroid(pos.x, pos.y, new_radius)
        a2.velocity = a2_velocity * 1.2
