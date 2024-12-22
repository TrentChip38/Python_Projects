import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 15
BALL_SPEED_X, BALL_SPEED_Y = 4, 4

# Initialize paddles and ball
player1_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Scores
player1_score = 0
player2_score = 0

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 36)

# Function to draw everything
def draw():
    screen.fill(BLACK)
    
    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    
    # Draw middle line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    # Draw scores
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4, 20))
    screen.blit(player2_text, (WIDTH - WIDTH // 4, 20))
    
    pygame.display.flip()

# Game loop
running = True
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_dx *= -1

    # Ball out of bounds
    if ball.left <= 0:
        player2_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
    if ball.right >= WIDTH:
        player1_score += 1
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_dx, ball_dy = -BALL_SPEED_X, BALL_SPEED_Y

    # Draw everything
    draw()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
