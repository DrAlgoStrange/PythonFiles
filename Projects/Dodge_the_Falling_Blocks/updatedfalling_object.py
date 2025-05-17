import pygame
import random
import sys
import os

# Initialize
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚧 Dodge the Chaos!")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 60
player_speed = 7

# Load images
def load_and_scale(path, size):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)

player_img = load_and_scale("assets/player.png", (50, 50))
object_images = [
    load_and_scale("assets/brick.png", (40, 40)),
    load_and_scale("assets/car.png", (40, 40)),
    load_and_scale("assets/bomb.png", (40, 40)),
    load_and_scale("assets/piano.png", (40, 40)),
    load_and_scale("assets/plane.png", (40, 40))
]

# Block types (used for speed/difficulty)
block_types = [
    {"speed": 4},
    {"speed": 5},
    {"speed": 6}
]

# High score
high_score_file = "highscore.txt"
score = 0
high_score = 0
if os.path.exists(high_score_file):
    try:
        with open(high_score_file, "r") as f:
            high_score = int(f.read())
    except:
        high_score = 0

# Object holders
falling_objects = []
crazy_objects = []

def spawn_object():
    block = random.choice(block_types)
    return {
        "x": random.randint(0, WIDTH - 40),
        "y": -40,
        "speed": block["speed"],
        "image": random.choice(object_images),
        "w": 40,
        "h": 40
    }

def spawn_crazy_object():
    return {
        "x": random.randint(0, WIDTH - 40),
        "y": -40,
        "dx": random.choice([-3, -2, -1, 1, 2, 3]),
        "dy": random.randint(3, 6),
        "image": random.choice(object_images),
        "w": 40,
        "h": 40
    }

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Difficulty rules
    if score < 25:
        while len(falling_objects) < 5:
            falling_objects.append(spawn_object())
    elif score < 60:
        while len(falling_objects) < 10:
            falling_objects.append(spawn_object())
    else:
        falling_objects.clear()
        while len(crazy_objects) < 10:
            crazy_objects.append(spawn_crazy_object())

    # Update & draw falling objects
    for obj in falling_objects:
        obj["y"] += obj["speed"]
        if obj["y"] > HEIGHT:
            obj.update(spawn_object())
            score += 1
        screen.blit(obj["image"], (obj["x"], obj["y"]))

    # Update & draw crazy objects
    for obj in crazy_objects[:]:
        obj["x"] += obj["dx"]
        obj["y"] += obj["dy"]
        if obj["x"] <= 0 or obj["x"] + obj["w"] >= WIDTH:
            obj["dx"] *= -1
        if obj["y"] > HEIGHT:
            crazy_objects.remove(obj)
            score += 2
        screen.blit(obj["image"], (obj["x"], obj["y"]))

    # Player
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    screen.blit(player_img, (player_x, player_y))

    # Collision detection
    for obj in falling_objects + crazy_objects:
        obj_rect = pygame.Rect(obj["x"], obj["y"], obj["w"], obj["h"])
        if player_rect.colliderect(obj_rect):
            draw_text("💥 Game Over!", WIDTH//2 - 100, HEIGHT//2, RED)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

    # Score display
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"High Score: {high_score}", 10, 40)

    pygame.display.flip()

# Save high score
if score > high_score:
    with open(high_score_file, "w") as f:
        f.write(str(score))

pygame.quit()
sys.exit()
 