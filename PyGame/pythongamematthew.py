import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge and Collect")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 128, 255)
GREEN = (0, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 6

# Falling object settings
enemy_size = 40
enemy_list = []
enemy_speed = 3

# Coin settings
coin_size = 30
coin_list = []
coin_spawn_time = 1500  # Spawn a coin every 1500ms

# Score and Lives
score = 0
lives = 5

# Fonts
font = pygame.font.SysFont(None, 36)

# Sounds
pygame.mixer.init()
coin_sound = pygame.mixer.Sound("coin.wav")  # Add a coin sound
hit_sound = pygame.mixer.Sound("hit.wav")    # Add a hit sound

# Create a plain black background surface
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(BLACK)  # Fill the surface with black color

# Spawn enemy
def spawn_enemy():
    x_pos = random.randint(0, WIDTH - enemy_size)
    enemy_list.append([x_pos, 0])

# Spawn coin
def spawn_coin():
    x_pos = random.randint(0, WIDTH - coin_size)
    y_pos = random.randint(0, HEIGHT // 2)
    coin_list.append([x_pos, y_pos])

# Move enemies
def move_enemies():
    global lives
    for enemy in enemy_list[:]:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy_list.remove(enemy)
            lives -= 1

# Move coins
def move_coins():
    for coin in coin_list[:]:
        coin[1] += 2  # Coins fall slowly
        if coin[1] > HEIGHT:
            coin_list.remove(coin)

# Detect collision
def detect_collision(player, obj, size):
    px, py = player[0], player[1]
    ox, oy = obj[0], obj[1]
    return (ox < px < ox + size or ox < px + player_size < ox + size) and \
           (oy < py < oy + size or oy < py + player_size < oy + size)

# Main game loop
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 800)  # Spawn an enemy every 800ms

coin_timer = pygame.USEREVENT + 2
pygame.time.set_timer(coin_timer, coin_spawn_time)

running = True
while running:
    # Fill the screen with the plain black background
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == enemy_timer:
            spawn_enemy()
        if event.type == coin_timer:
            spawn_coin()
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    
    # Move enemies and check for collisions
    move_enemies()
    for enemy in enemy_list[:]:
        if detect_collision(player_pos, enemy, enemy_size):
            enemy_list.remove(enemy)
            lives -= 1
            hit_sound.play()
    
    # Move coins and check for collisions
    move_coins()
    for coin in coin_list[:]:
        if detect_collision(player_pos, coin, coin_size):
            coin_list.remove(coin)
            score += 10
            coin_sound.play()
    
    # Draw player
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    
    # Draw enemies
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))
    
    # Draw coins
    for coin in coin_list:
        pygame.draw.circle(screen, YELLOW, (coin[0] + coin_size // 2, coin[1] + coin_size // 2), coin_size // 2)
    
    # Draw score and lives
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))
    
    # Game Over
    if lives <= 0:
        game_over_text = font.render("Game Over! Press ESC to Exit", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
        pygame.display.flip()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
                break
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
