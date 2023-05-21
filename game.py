import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shooting Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player_width, player_height = 50, 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 3  # Decreased player speed
player_movement = 0
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Bullet
bullet_width, bullet_height = 10, 30
bullet_speed = 10
bullet_state = "ready"  # "ready" -> ready to be fired, "fired" -> bullet is currently moving
bullet = pygame.Rect(0, 0, bullet_width, bullet_height)

# Enemies
enemy_width, enemy_height = 50, 50
enemy_speed = 2
enemies = []
num_enemies = 5
for _ in range(num_enemies):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(50, 200)
    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_movement = -1
                player_speed *= 0.9  # Decrease player speed
            if event.key == pygame.K_RIGHT:
                player_movement = 1
                player_speed *= 0.9  # Decrease player speed

            # Fire bullet
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet.x = player.x + player_width // 2 - bullet_width // 2
                bullet.y = player.y
                bullet_state = "fired"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_movement = 0

    # Move the player
    player.x += player_movement * player_speed

    # Keep the player within the screen bounds
    if player.left < 0:
        player.left = 0
    elif player.right > screen_width:
        player.right = screen_width

    # Move the bullet
    if bullet_state == "fired":
        bullet.y -= bullet_speed

    # Collision detection
    if bullet.y <= 0:
        bullet_state = "ready"
        bullet.y = -bullet_height

    for enemy in enemies:
        if bullet.colliderect(enemy):
            enemies.remove(enemy)
            bullet_state = "ready"
            bullet.y = -bullet_height
            score += 10

    # Update the display
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, enemy)

    # Draw the score
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    # Check if all enemies are finished
    if len(enemies) == 0:
        win_text = font.render("You won the game!", True, RED)
        screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)  # Pause for 3 seconds
        running = False

    pygame.display.flip()

# Quit the game
pygame.quit()
