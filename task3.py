import pygame
import sys
import random
import math

WIDTH, HEIGHT = 800, 600           
DRONE_SIZE = 20                    
SEPARATION_DISTANCE = 50           
MAX_SPEED = 3                      
NUM_DRONES = 20                    

class Drone:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, DRONE_SIZE, DRONE_SIZE)
        self.speed_x = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.speed_y = random.uniform(-MAX_SPEED, MAX_SPEED)

    def update(self, drones):
        move_x, move_y = 0, 0

        for other in drones:
            if other == self:
                continue 
            distance = math.hypot(other.rect.centerx - self.rect.centerx,
                                  other.rect.centery - self.rect.centery)
           
            if distance < SEPARATION_DISTANCE and distance != 0:
                move_x += self.rect.centerx - other.rect.centerx
                move_y += self.rect.centery - other.rect.centery

        self.speed_x += move_x * 0.05
        self.speed_y += move_y * 0.05

        speed = math.hypot(self.speed_x, self.speed_y)
        if speed > MAX_SPEED:
            scale = MAX_SPEED / speed
            self.speed_x *= scale
            self.speed_y *= scale

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (225, 0, 0), self.rect)

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Swarm Project — Task 3")

    clock = pygame.time.Clock()

    drones = [Drone(random.randint(0, WIDTH - DRONE_SIZE),
                    random.randint(0, HEIGHT - DRONE_SIZE)) for _ in range(NUM_DRONES)]

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for drone in drones:
            drone.update(drones)

        screen.fill((255, 255, 255))

        for drone in drones:
            drone.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
