import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge and Collect")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# Sounds
pygame.mixer.init()
coin_sound = pygame.mixer.Sound("coin.wav")  # Add a coin sound file
hit_sound = pygame.mixer.Sound("hit.wav")    # Add a hit sound file

# Car settings
car_width = 50
car_height = 80
car_speed = 5

# Levels and difficulty
levels = 6
current_level = 1
coin_goal = 5
coins_collected = 0

# Obstacle settings
obstacle_width = 50
obstacle_height = 80
obstacle_speed = 4
obstacles = []

# Coin settings
coin_radius = 15
coins = []

# Create the car
car = pygame.Rect(WIDTH // 2 - car_width // 2, HEIGHT - car_height - 10, car_width, car_height)

# Function to spawn obstacles
def spawn_obstacles(num):
    for _ in range(num):
        x = random.randint(0, WIDTH - obstacle_width)
        y = random.randint(-300, -50)
        obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

# Function to spawn coins
def spawn_coins(num):
    for _ in range(num):
        x = random.randint(0, WIDTH - coin_radius * 2)
        y = random.randint(-300, -50)
        coins.append(pygame.Rect(x, y, coin_radius * 2, coin_radius * 2))

# Function to move and remove obstacles
def move_obstacles():
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)

# Function to move coins
def move_coins():
    for coin in coins[:]:
        coin.y += obstacle_speed
        if coin.y > HEIGHT:
            coins.remove(coin)

# Function to check collision
def detect_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Function to display level and instructions
def display_text(text, x, y, color=WHITE):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

# Main game loop
running = True
while running:
    screen.fill(GRAY)  # Background color
    
    # Display level and coins collected
    display_text(f"Level: {current_level}", 10, 10)
    display_text(f"Coins: {coins_collected}/{coin_goal}", 10, 50)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car.x > 0:
        car.x -= car_speed
    if keys[pygame.K_RIGHT] and car.x < WIDTH - car_width:
        car.x += car_speed
    if keys[pygame.K_UP] and car.y > 0:
        car.y -= car_speed
    if keys[pygame.K_DOWN] and car.y < HEIGHT - car_height:
        car.y += car_speed

    # Move obstacles and check for collisions
    move_obstacles()
    for obstacle in obstacles[:]:
        if detect_collision(car, obstacle):
            hit_sound.play()
            running = False  # Game over
    
    # Move coins and check for collection
    move_coins()
    for coin in coins[:]:
        if detect_collision(car, coin):
            coin_sound.play()
            coins.remove(coin)
            coins_collected += 1

    # Draw car
    pygame.draw.rect(screen, BLUE, car)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin.x + coin_radius, coin.y + coin_radius), coin_radius)

    # Check level completion
    if coins_collected >= coin_goal:
        current_level += 1
        if current_level > levels:
            display_text("You Win! Press ESC to Exit", WIDTH // 2 - 150, HEIGHT // 2)
            pygame.display.flip()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                    break
        else:
            coins_collected = 0
            coin_goal += 3  # Increase coin goal
            obstacle_speed += 1  # Increase speed
            car_speed += 0.5  # Increase car speed
            obstacles.clear()
            coins.clear()
            spawn_obstacles(current_level + 2)
            spawn_coins(current_level + 3)

    # Spawn new obstacles and coins
    if len(obstacles) < current_level + 2:
        spawn_obstacles(1)
    if len(coins) < current_level + 3:
        spawn_coins(1)

    # Update screen
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
