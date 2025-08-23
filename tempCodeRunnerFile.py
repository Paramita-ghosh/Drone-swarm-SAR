import pygame
import sys
import random

# --- Constants ---
WIDTH, HEIGHT = 800, 600
FPS = 60

# --- Player Class ---
class Player:
    def __init__(self, x, y, speed=5):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.speed = speed

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep inside window
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


# --- Enemy Class ---
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50), 50, 50)
        self.speed = random.choice([2, 3, 4])

    def update(self):
        # Simple movement (bouncing around)
        self.rect.y += self.speed
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)


# --- Main Game Loop ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Task 2 — Player & Enemy")
    clock = pygame.time.Clock()

    player = Player(WIDTH//2, HEIGHT//2)
    enemy = Enemy()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)
        enemy.update()

        # Collision detection
        if player.rect.colliderect(enemy.rect):
            print("Collision!")
            running = False

        # Drawing
        screen.fill((30, 30, 30))
        player.draw(screen)
        enemy.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
