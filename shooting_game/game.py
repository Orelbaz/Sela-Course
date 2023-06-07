import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Best shooting game ever")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player
player_width, player_height = 50, 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
player_movement = 0
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Bullet
bullet_width, bullet_height = 10, 30
bullet_speed = 8
bullet_state = "ready"
bullet = pygame.Rect(0, 0, bullet_width, bullet_height)

# Enemies
enemy_width, enemy_height = 50, 50
enemy_speed = 2
enemy_bullet_width, enemy_bullet_height = 10, 30
enemy_bullet_speed = 8
enemy_bullet_delay = 500  # Decreased delay for more frequent enemy bullets
enemies = []
enemy_bullets = []
num_enemies = 5
max_level = 6
level = 1
enemy_speed_multiplier = 1
enemy_bullet_delay_multiplier = 1
for _ in range(num_enemies):
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = random.randint(50, 200)
    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
enemy_last_shot = pygame.time.get_ticks()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Power-up
class PowerUp:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

power_up_width, power_up_height = 30, 30
power_up_speed = 2
power_up = None

# Game loop
running = True
game_over = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_movement = -1
            if event.key == pygame.K_RIGHT:
                player_movement = 1

            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet.x = player.x + player_width // 2 - bullet_width // 2
                bullet.y = player.y
                bullet_state = "fired"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_movement == -1:
                player_movement = 0
            if event.key == pygame.K_RIGHT and player_movement == 1:
                player_movement = 0

    player.x += player_movement * player_speed

    if player.left < 0:
        player.left = 0
    elif player.right > screen_width:
        player.right = screen_width

    if bullet_state == "fired":
        bullet.y -= bullet_speed

    if bullet.y <= 0:
        bullet_state = "ready"
        bullet.y = -bullet_height

    for enemy in enemies:
        if bullet.colliderect(enemy):
            enemies.remove(enemy)
            bullet_state = "ready"
            bullet.y = -bullet_height
            score += 10

        if enemy.y >= screen_height:
            enemies.remove(enemy)

        if pygame.time.get_ticks() - enemy_last_shot >= enemy_bullet_delay:
            enemy_bullet = pygame.Rect(
                enemy.x + enemy_width // 2 - enemy_bullet_width // 2,
                enemy.y + enemy_height,
                enemy_bullet_width,
                enemy_bullet_height,
            )
            enemy_bullets.append(enemy_bullet)
            enemy_last_shot = pygame.time.get_ticks()

            if enemy_bullet.colliderect(player):
                game_over = True

    if power_up is None:
        if random.random() < 0.01:
            power_up = PowerUp(
                random.randint(0, screen_width - power_up_width),
                random.randint(50, 200),
                power_up_width,
                power_up_height,
                power_up_speed,
            )

    if power_up is not None:
        power_up.rect.y += power_up.speed
        if power_up.rect.colliderect(player):
            player_speed += 2
            power_up = None

        if power_up.rect.y >= screen_height:
            power_up = None

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, BLACK, enemy)
    for enemy_bullet in enemy_bullets:
        pygame.draw.rect(screen, BLACK, enemy_bullet)

    if power_up is not None:
        pygame.draw.rect(screen, GREEN, power_up.rect)

    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("You lost the game!", True, RED)
        screen.blit(
            game_over_text,
            (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2),
        )
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    elif len(enemies) == 0:
        level += 1
        if level <= max_level:
            player.x = screen_width // 2 - player_width // 2
            bullet_state = "ready"
            enemy_bullets.clear()
            enemies.clear()
            for _ in range(num_enemies + level * 2):
                enemy_x = random.randint(0, screen_width - enemy_width)
                enemy_y = random.randint(50, 200)
                enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
            enemy_speed_multiplier += 0.5
            enemy_bullet_delay_multiplier += 0.5
            enemy_speed = int(enemy_speed_multiplier * level)
            enemy_bullet_speed *= 2  # Double the enemy bullet speed
            enemy_bullet_delay = max(100, int(enemy_bullet_delay_multiplier * level * 500))
            num_enemies *= 2  # Double the number of enemies

            level_text = font.render("Level " + str(level), True, RED)
            screen.blit(
                level_text,
                (screen_width // 2 - level_text.get_width() // 2, screen_height // 2 - level_text.get_height() // 2),
            )
            pygame.display.flip()
            pygame.time.wait(2000)
        else:
            win_text = font.render("You won the game!", True, RED)
            screen.blit(
                win_text,
                (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2),
            )
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
