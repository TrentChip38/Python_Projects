import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Maze Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player settings
player_size = 20
player_pos = [50, 50]
player_speed = 5

# Goal settings
goal_size = 30

# Coin settings
coin_size = 15
coin_count = 5  # Number of coins per level
coins = []

# Enemy settings
enemy_size = 20
enemies = []

# Levels and Walls
levels = [
    [
        (0, 100, 200, 20), (200, 100, 20, 150), (0, 250, 220, 20), (180, 300, 20, 100),
        (100, 400, 200, 20), (300, 200, 20, 200), (400, 0, 20, 250), (300, 400, 200, 20),
        (500, 250, 20, 100), (550, 150, 200, 20), (700, 150, 20, 350), (550, 450, 170, 20),
    ],
    [
        (0, 50, 400, 20), (200, 100, 20, 200), (400, 50, 20, 400), (600, 0, 20, 300),
        (300, 400, 200, 20), (700, 200, 20, 250), (100, 500, 300, 20), (500, 450, 200, 20),
    ],
]
current_level = 0

# Timer and Score
timer = 60  # 60 seconds per level
score = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load custom graphics (Optional - Replace with actual image files)
player_image = pygame.Surface((player_size, player_size))
player_image.fill(BLUE)
goal_image = pygame.Surface((goal_size, goal_size))
goal_image.fill(GREEN)
coin_image = pygame.Surface((coin_size, coin_size))
coin_image.fill(YELLOW)
enemy_image = pygame.Surface((enemy_size, enemy_size))
enemy_image.fill(RED)

# Function to reset level
def reset_level():
    global player_pos, coins, enemies, timer
    player_pos = [50, 50]
    coins = [
        [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
        for _ in range(coin_count)
    ]
    enemies = [
        [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice([-2, 2]), random.choice([-2, 2])]
        for _ in range(current_level + 1)
    ]
    timer = 60

# Function to draw everything
def draw_game():
    # Clear the screen
    screen.fill(WHITE)

    # Draw walls
    for wall in levels[current_level]:
        pygame.draw.rect(screen, BLACK, wall)

    # Draw player
    screen.blit(player_image, player_pos)

    # Draw goal
    goal_pos = [750, 550]
    screen.blit(goal_image, goal_pos)

    # Draw coins
    for coin in coins:
        screen.blit(coin_image, coin)

    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy_image, enemy[:2])

    # Draw score and timer
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    timer_text = font.render(f"Time: {int(timer)}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (10, 50))

# Function to check collisions
def check_collision(rect, obstacles):
    for obstacle in obstacles:
        if rect.colliderect(obstacle):
            return True
    return False

# Reset the first level
reset_level()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    new_pos = player_pos[:]
    if keys[pygame.K_LEFT]:
        new_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        new_pos[0] += player_speed
    if keys[pygame.K_UP]:
        new_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        new_pos[1] += player_speed

    # Collision detection
    player_rect = pygame.Rect(new_pos[0], new_pos[1], player_size, player_size)
    wall_rects = [pygame.Rect(wall) for wall in levels[current_level]]
    if not check_collision(player_rect, wall_rects):
        player_pos = new_pos

    # Check goal collision
    goal_rect = pygame.Rect(750, 550, goal_size, goal_size)
    if player_rect.colliderect(goal_rect):
        score += 100
        current_level += 1
        if current_level >= len(levels):
            print("You Win!")
            running = False
        else:
            reset_level()

    # Check coin collection
    coins = [coin for coin in coins if not player_rect.colliderect(pygame.Rect(coin[0], coin[1], coin_size, coin_size))]
    score += (coin_count - len(coins)) * 10

    # Move enemies
    for enemy in enemies:
        enemy[0] += enemy[2]
        enemy[1] += enemy[3]
        if enemy[0] <= 0 or enemy[0] >= WIDTH - enemy_size:
            enemy[2] *= -1
        if enemy[1] <= 0 or enemy[1] >= HEIGHT - enemy_size:
            enemy[3] *= -1

    # Check enemy collision
    if any(player_rect.colliderect(pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)) for enemy in enemies):
        print("Game Over!")
        running = False

    # Update timer
    timer -= clock.get_time() / 1000
    if timer <= 0:
        print("Time's up! Game Over!")
        running = False

    # Draw the game
    draw_game()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
