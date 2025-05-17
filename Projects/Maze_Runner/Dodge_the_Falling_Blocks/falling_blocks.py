import pygame
import random
import sys
import os

# Initialize
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⚡ Dodge the Falling Chaos")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 200, 100)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player setup
player_width, player_height = 50, 10
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 40
player_speed = 7

# Block types
block_types = [
    {"color": RED, "width": 40, "height": 40, "speed": 5},
    {"color": GREEN, "width": 30, "height": 30, "speed": 6},
    {"color": YELLOW, "width": 50, "height": 50, "speed": 4}
]

# Crazy objects
crazy_objects = []

# Game state
score = 0
high_score_file = "highscore.txt"
high_score = 0
if os.path.exists(high_score_file):
    with open(high_score_file, "r") as f:
        try:
            high_score = int(f.read())
        except:
            high_score = 0

# Falling objects
falling_objects = []

def spawn_object():
    obj_type = random.choice(block_types)
    return {
        "x": random.randint(0, WIDTH - obj_type["width"]),
        "y": -obj_type["height"],
        "w": obj_type["width"],
        "h": obj_type["height"],
        "color": obj_type["color"],
        "speed": obj_type["speed"]
    }

def spawn_crazy_object():
    size = random.randint(20, 40)
    return {
        "x": random.randint(0, WIDTH - size),
        "y": -size,
        "w": size,
        "h": size,
        "color": (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
        "dx": random.choice([-3, -2, -1, 1, 2, 3]),
        "dy": random.randint(3, 6)
    }

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Initial spawn
for _ in range(5):
    falling_objects.append(spawn_object())

# Main game loop
# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Difficulty progression
    if score < 12:
        # Spawn max 5 easy objects
        while len(falling_objects) < 5:
            falling_objects.append(spawn_object())
    elif score < 30:
        # Spawn up to 10 predictable objects
        while len(falling_objects) < 10:
            falling_objects.append(spawn_object())
    else:
        # After 30, switch to only crazy objects
        falling_objects.clear()  # Remove easy objects
        while len(crazy_objects) < 10:
            crazy_objects.append(spawn_crazy_object())

    # Update and draw falling objects
    for obj in falling_objects:
        obj["y"] += obj["speed"]
        if obj["y"] > HEIGHT:
            obj.update(spawn_object())  # respawn
            score += 1
        pygame.draw.rect(screen, obj["color"], (obj["x"], obj["y"], obj["w"], obj["h"]))

    # Update and draw crazy objects
    for obj in crazy_objects[:]:
        obj["x"] += obj["dx"]
        obj["y"] += obj["dy"]

        if obj["x"] <= 0 or obj["x"] + obj["w"] >= WIDTH:
            obj["dx"] *= -1
        if obj["y"] > HEIGHT:
            crazy_objects.remove(obj)
            score += 2

        pygame.draw.rect(screen, obj["color"], (obj["x"], obj["y"], obj["w"], obj["h"]))

    # Player rect and collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, BLUE, player_rect)

    for obj in falling_objects + crazy_objects:
        obj_rect = pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"])
        if player_rect.colliderect(obj_rect):
            draw_text("💀 Game Over!", WIDTH//2 - 100, HEIGHT//2, RED)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

    # Score display
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"High Score: {high_score}", 10, 40)

    pygame.display.flip()


# Update high score
if score > high_score:
    with open(high_score_file, "w") as f:
        f.write(str(score))

pygame.quit()
sys.exit()
