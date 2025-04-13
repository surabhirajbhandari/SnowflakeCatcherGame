# File Name: main.py
# Purpose: Snowflake Catcher Game with Winter Wonderland Theme
# Surabhi Rajbhandari : sr3523

import pygame
import sys
import random
from drawable import Rectangle, Snowflake, Snowman, Basket

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GROUND_COLOR = (255, 250, 250)  # Snowy White
SKY_COLOR = (135, 206, 250)   # Sky Blue

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snowflake Catcher")

# Clock to control frame rate
clock = pygame.time.Clock()

# Fonts and score
font = pygame.font.SysFont(None, 36)
score = 0

# Snowflake spawn control
snow_timer = 0
spawn_interval = 300  # in milliseconds

# Game objects
snowflakes = []
drawables = []

# Add snowman and basket
snowman = Snowman(100, HEIGHT // 2 + 50)
basket = Basket(WIDTH // 2, HEIGHT - 60)

# Function to draw environment
def draw_environment():
    screen.fill(SKY_COLOR)
    
    # Draw snow ground
    pygame.draw.rect(screen, (255, 250, 250), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))  # snowy ground
    pygame.draw.ellipse(screen, (255, 255, 255), (-100, HEIGHT//2 + 80, WIDTH + 200, 200))  # soft snowbank

    # Optional: scatter snow dots
    for _ in range(40):
        x = random.randint(0, WIDTH)
        y = random.randint(HEIGHT // 2 + 60, HEIGHT - 5)
        r = random.randint(2, 4)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), r)

# Function to display score
def draw_score():
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
while running:
    dt = clock.tick(60)
    snow_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket.move_left()
    if keys[pygame.K_RIGHT]:
        basket.move_right(WIDTH)

    # Spawn new snowflakes
    if snow_timer >= spawn_interval:
        snowflakes.append(Snowflake.spawn())
        snow_timer = 0

    # Update snowflakes
    for flake in snowflakes:
        flake.move()

    # Collision detection
    basket_rect = basket.get_rect()
    caught = []
    missed = []

    for flake in snowflakes:
        x, y = flake.getLoc()
        if basket_rect.collidepoint(x, y):
            caught.append(flake)
        elif y > HEIGHT:
            missed.append(flake)

    for flake in caught:
        snowflakes.remove(flake)
        score += 1

    for flake in missed:
        snowflakes.remove(flake)

    # Draw everything
    draw_environment()
    snowman.draw(screen)
    for flake in snowflakes:
        flake.draw(screen)
    basket.draw(screen)
    draw_score()

    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
