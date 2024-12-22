import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (100, 100, 100)

# Player settings
player_size = 20
player_speed = 5

# Goal settings
goal_size = 30

# Coin settings
coin_size = 15
coin_count = 5

# Enemy settings
enemy_size = 20

# Levels and Walls
levels = [
    [
        # Level 1
        (0, 100, 200, 20), (200, 100, 20, 150), (0, 250, 220, 20), (180, 300, 20, 100),
        (100, 400, 200, 20), (300, 200, 20, 200), (400, 0, 20, 250), (300, 400, 200, 20),
        (500, 250, 20, 100), (550, 150, 200, 20), (700, 150, 20, 350), (550, 450, 170, 20),
    ],
    [
        # Level 2
        (50, 100, 400, 20), (200, 100, 20, 200), (400, 50, 20, 400), (600, 0, 20, 300),
        (300, 400, 200, 20), (700, 200, 20, 250), (100, 500, 300, 20), (500, 450, 200, 20),
        (150, 150, 200, 20), (500, 300, 100, 20), (550, 350, 20, 100),
    ],
    [
        # Level 3
        (400, 0, 20, 200), (300, 100, 20, 300), (500, 0, 20, 400), (700, 200, 20, 200),
        (400, 500, 200, 20), (200, 300, 20, 200), (0, 100, 200, 20), (600, 100, 20, 200),
        (300, 500, 20, 100), (150, 400, 200, 20), (400, 400, 20, 100), (600, 300, 100, 20),
    ],
    [
        # Level 4
        (0, 150, 600, 20), (700, 150, 20, 450), (600, 300, 20, 300), (400, 200, 200, 20),
        (300, 400, 200, 20), (100, 300, 200, 20), (0, 500, 300, 20), (0, 400, 20, 100),
        (100, 200, 20, 100), (400, 100, 200, 20), (600, 200, 20, 100),
    ],
    [
        # Level 5
        (0, 100, 600, 20), (0, 200, 200, 20), (300, 100, 20, 300), (500, 100, 20, 400),
        (600, 400, 200, 20), (200, 300, 100, 20), (700, 150, 20, 350), (400, 500, 200, 20),
        (100, 400, 200, 20), (200, 200, 20, 100), (400, 300, 200, 20), (600, 200, 20, 100),
    ],
    [
        # Level 6 (Final Level)
        (50, 100, 800, 20), (100, 100, 20, 400), (700, 50, 20, 500), (400, 0, 20, 250),
        (300, 300, 200, 20), (500, 200, 100, 20), (600, 300, 20, 200), (300, 400, 100, 20),
        (200, 200, 20, 100), (0, 500, 300, 20), (400, 400, 20, 100),
    ],
]

# Timer and Score
timer = 60  # 60 seconds per level
score = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player start positions for each level
start_positions = [
    [50, 50],
    [50, 50],
    [50, 50],
    [50, 50],
    [50, 50],
    [50, 50],
]

# Reset level
current_level = 0
coins = []
enemies = []

def reset_level():
    global player_pos, coins, enemies, timer
    player_pos = start_positions[current_level]
    coins.clear()
    enemies.clear()

# Draw Game
    # Generate coins
    for _ in range(coin_count):
        while True:
            coin = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
            coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size)
            wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
            if not any(coin_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                coins.append(coin)
                break

    # Generate enemies
    for _ in range(current_level + 2):  # Enemies increase with each level
        while True:
            enemy = [
                random.randint(50, WIDTH - 50),
                random.randint(50, HEIGHT - 50),
                random.choice([-2, 2]),
                random.choice([-2, 2]),
            ]
            enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
            wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
            if not any(enemy_rect.colliderect(wall_rect) for wall_rect in wall_rects):
                enemies.append(enemy)
                break

    timer = 60  # Reset timer

# Function to draw everything
def draw_game():
    # Clear screen
    screen.fill(GREY)

    # Draw walls
    for wall in levels[current_level]:
        pygame.draw.rect(screen, BLACK, wall)

    # Draw player
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    pygame.draw.rect(screen, BLUE, player_rect)

    # Draw goal
    goal_pos = [WIDTH - 50, HEIGHT - 50]
    goal_rect = pygame.Rect(goal_pos[0], goal_pos[1], goal_size, goal_size)
    pygame.draw.rect(screen, GREEN, goal_rect)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_size // 2)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

    # Draw timer and score
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f"Time: {int(timer)}", True, BLACK)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(timer_text, (10, 10))
    screen.blit(score_text, (10, 50))

# Initialize the first level
reset_level()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Timer
    timer -= clock.get_time() / 1000
    if timer <= 0:
        print("Time's up! Game Over!")
        running = False

    # Player movement
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx -= player_speed
    if keys[pygame.K_RIGHT]:
        dx += player_speed
    if keys[pygame.K_UP]:
        dy -= player_speed
    if keys[pygame.K_DOWN]:
        dy += player_speed

    # Move player with collision detection
    new_pos = [player_pos[0] + dx, player_pos[1] + dy]
    new_rect = pygame.Rect(new_pos[0], new_pos[1], player_size, player_size)
    wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
    if not any(new_rect.colliderect(wall_rect) for wall_rect in wall_rects):
        player_pos = new_pos

    # Check for reaching the goal
    goal_rect = pygame.Rect(WIDTH - 50, HEIGHT - 50, goal_size, goal_size)
    if new_rect.colliderect(goal_rect):
        score += 100
        current_level += 1
        if current_level >= len(levels):
            print("You win!")
            running = False
        else:
            reset_level()

    # Check for coin collection
    for coin in coins[:]:
        coin_rect = pygame.Rect(coin[0], coin[1], coin_size, coin_size)
        if new_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += 10

    # Move enemies
    for enemy in enemies:
        enemy[0] += enemy[2]
        enemy[1] += enemy[3]
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if enemy[0] <= 0 or enemy[0] >= WIDTH - enemy_size:
            enemy[2] *= -1
        if enemy[1] <= 0 or enemy[1] >= HEIGHT - enemy_size:
            enemy[3] *= -1
        if new_rect.colliderect(enemy_rect):
            print("Game Over! Enemy collision.")
            running = False

    # Draw game
    draw_game()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
