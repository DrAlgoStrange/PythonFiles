import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player setup
player_width, player_height = 50, 10
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 50
player_speed = 7

# Block setup
block_width, block_height = 50, 50
block_x = random.randint(0, WIDTH - block_width)
block_y = -block_height
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move block
    block_y += block_speed
    if block_y > HEIGHT:
        block_y = -block_height
        block_x = random.randint(0, WIDTH - block_width)
        score += 1
        block_speed += 0.2  # increase difficulty over time

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
    if player_rect.colliderect(block_rect):
        draw_text("Game Over!", WIDTH // 2 - 80, HEIGHT // 2, RED)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
        continue

    # Draw player and block
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, block_rect)
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
