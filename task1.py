import pygame
import sys

# --- Constants ---
WIDTH, HEIGHT = 800, 600
FPS = 60

# --- Player Class ---
class Player:
    def __init__(self, x, y, speed=5):
        self.rect = pygame.Rect(x, y, 50, 50)  # player as a rectangle
        self.speed = speed

    def update(self, keys):
        # Movement handling
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Boundary checking
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)  # green player


# --- Main Game Loop ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Task 1 — Moving Player")
    clock = pygame.time.Clock()

    player = Player(WIDTH//2, HEIGHT//2)

    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        # Drawing
        screen.fill((30, 30, 30))  # dark background
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
