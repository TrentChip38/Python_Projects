import pygame
import sys

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

# Player settings
player_size = 20
player_pos = [50, 50]
player_speed = 5

# Goal settings
goal_pos = [750, 550]
goal_size = 30

# Walls (x, y, width, height) - Complex Maze Layout
walls = [
    (0, 100, 200, 20), (200, 100, 20, 150), (0, 250, 220, 20), (180, 300, 20, 100),
    (100, 400, 200, 20), (300, 200, 20, 200), (400, 0, 20, 250), (300, 400, 200, 20),
    (500, 250, 20, 100), (550, 150, 200, 20), (700, 150, 20, 350), (550, 450, 170, 20),
    (400, 500, 200, 20), (400, 500, 20, 100), (250, 550, 200, 20), (250, 500, 20, 50),
    (50, 500, 200, 20), (50, 450, 20, 100), (0, 300, 20, 300),
]

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to draw the maze
def draw_maze():
    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

# Function to detect collisions
def check_collision(rect, obstacles):
    for obstacle in obstacles:
        if rect.colliderect(obstacle):
            return True
    return False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
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

    # Create rectangles for collision detection
    player_rect = pygame.Rect(new_pos[0], new_pos[1], player_size, player_size)
    wall_rects = [pygame.Rect(wall) for wall in walls]
    goal_rect = pygame.Rect(goal_pos[0], goal_pos[1], goal_size, goal_size)

    # Check collisions with walls
    if not check_collision(player_rect, wall_rects):
        player_pos = new_pos

    # Check if player reaches the goal
    if player_rect.colliderect(goal_rect):
        print("You Win!")
        running = False

    # Drawing
    screen.fill(WHITE)  # Clear screen
    draw_maze()
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))  # Player
    pygame.draw.rect(screen, GREEN, (*goal_pos, goal_size, goal_size))  # Goal

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
