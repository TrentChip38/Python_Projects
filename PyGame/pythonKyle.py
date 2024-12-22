import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stick Figure Battle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Clock for frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# Stick figure dimensions and settings
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60
PLAYER_SPEED = 7
JUMP_HEIGHT = 20
GRAVITY = 1

# Lives
player1_lives = 3
player2_lives = 3

# Game variables
player1_pos = [200, HEIGHT - PLAYER_HEIGHT]
player2_pos = [600, HEIGHT - PLAYER_HEIGHT]
player1_vel = [0, 0]
player2_vel = [0, 0]
player1_on_ground = False
player2_on_ground = False
player1_jumps = 0
player2_jumps = 0
game_over = False

# Define maps
maps = [
    [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(150, HEIGHT - 200, 500, 20)],  # Map 1
    [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(100, HEIGHT - 150, 200, 20), pygame.Rect(500, HEIGHT - 250, 200, 20)],  # Map 2
    [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(300, HEIGHT - 300, 200, 20)],  # Map 3
    [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(100, HEIGHT - 250, 600, 20), pygame.Rect(350, HEIGHT - 400, 100, 20)],  # Map 4
    [pygame.Rect(0, HEIGHT - 20, WIDTH, 20), pygame.Rect(200, HEIGHT - 300, 400, 20)],  # Map 5
]

# Randomize the map
current_map = random.choice(maps)


def draw_stick_figure(x, y, color):
    """Draw a stick figure at (x, y)."""
    pygame.draw.line(screen, color, (x + PLAYER_WIDTH // 2, y), (x + PLAYER_WIDTH // 2, y + PLAYER_HEIGHT), 4)  # Body
    pygame.draw.circle(screen, color, (x + PLAYER_WIDTH // 2, y - 10), 10)  # Head
    pygame.draw.line(screen, color, (x + PLAYER_WIDTH // 2, y + 20), (x, y + 40), 4)  # Left leg
    pygame.draw.line(screen, color, (x + PLAYER_WIDTH // 2, y + 20), (x + PLAYER_WIDTH, y + 40), 4)  # Right leg
    pygame.draw.line(screen, color, (x + PLAYER_WIDTH // 2, y + 10), (x - 10, y + 20), 4)  # Left arm
    pygame.draw.line(screen, color, (x + PLAYER_WIDTH // 2, y + 10), (x + PLAYER_WIDTH + 10, y + 20), 4)  # Right arm


def detect_collision(player_pos, opponent_pos):
    """Detect if player jumps on the opponent."""
    px, py = player_pos
    ox, oy = opponent_pos
    return (
        px + PLAYER_WIDTH > ox and px < ox + PLAYER_WIDTH  # Horizontal overlap
        and py + PLAYER_HEIGHT > oy  # Player lands on top
        and py + PLAYER_HEIGHT < oy + 10  # Within a small vertical range
    )


def display_text(text, x, y, color):
    """Display text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# Main game loop
while True:
    screen.fill(WHITE)  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement for Player 1 (WASD)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player1_pos[0] += PLAYER_SPEED
    if keys[pygame.K_w] and player1_jumps < 2:  # Double jump
        player1_vel[1] = -JUMP_HEIGHT
        player1_jumps += 1

    # Movement for Player 2 (IJKL)
    if keys[pygame.K_j]:
        player2_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_l]:
        player2_pos[0] += PLAYER_SPEED
    if keys[pygame.K_i] and player2_jumps < 2:  # Double jump
        player2_vel[1] = -JUMP_HEIGHT
        player2_jumps += 1

    # Apply gravity
    player1_vel[1] += GRAVITY
    player2_vel[1] += GRAVITY

    # Update positions
    player1_pos[1] += player1_vel[1]
    player2_pos[1] += player2_vel[1]

    # Check for ground and platform collisions
    player1_on_ground = False
    player2_on_ground = False
    for platform in current_map:
        if player1_pos[1] + PLAYER_HEIGHT > platform.top and player1_pos[1] < platform.top:
            if player1_pos[0] + PLAYER_WIDTH > platform.left and player1_pos[0] < platform.right:
                player1_pos[1] = platform.top - PLAYER_HEIGHT
                player1_vel[1] = 0
                player1_on_ground = True
                player1_jumps = 0
        if player2_pos[1] + PLAYER_HEIGHT > platform.top and player2_pos[1] < platform.top:
            if player2_pos[0] + PLAYER_WIDTH > platform.left and player2_pos[0] < platform.right:
                player2_pos[1] = platform.top - PLAYER_HEIGHT
                player2_vel[1] = 0
                player2_on_ground = True
                player2_jumps = 0

    # Check screen boundaries
    player1_pos[0] = max(0, min(WIDTH - PLAYER_WIDTH, player1_pos[0]))
    player2_pos[0] = max(0, min(WIDTH - PLAYER_WIDTH, player2_pos[0]))

    # Detect collisions between players
    if detect_collision(player1_pos, player2_pos):
        player2_lives -= 1
        player2_pos = [600, HEIGHT - PLAYER_HEIGHT]
        player1_pos = [200, HEIGHT - PLAYER_HEIGHT]
    if detect_collision(player2_pos, player1_pos):
        player1_lives -= 1
        player1_pos = [200, HEIGHT - PLAYER_HEIGHT]
        player2_pos = [600, HEIGHT - PLAYER_HEIGHT]

    # Check for game over
    if player1_lives <= 0 or player2_lives <= 0:
        game_over = True

    # Draw platforms
    for platform in current_map:
        pygame.draw.rect(screen, BLACK, platform)

    # Draw stick figures
    draw_stick_figure(player1_pos[0], player1_pos[1], RED)
    draw_stick_figure(player2_pos[0], player2_pos[1], BLUE)

    # Draw lives
    display_text(f"Player 1 Lives: {player1_lives}", 10, 10, RED)
    display_text(f"Player 2 Lives: {player2_lives}", WIDTH - 200, 10, BLUE)

    # Game over screen
    if game_over:
        winner = "Player 1" if player2_lives <= 0 else "Player 2"
        display_text(f"{winner} Wins!", WIDTH // 2 - 100, HEIGHT // 2 - 20, GREEN)
        display_text("Press ESC to Exit", WIDTH // 2 - 100, HEIGHT // 2 + 20, BLACK)
        pygame.display.flip()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    clock.tick(30)
