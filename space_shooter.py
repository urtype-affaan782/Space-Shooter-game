import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# Load assets (updated to use .jpg extensions)
player_img = pygame.image.load("player.jpg")
enemy_img = pygame.image.load("enemy.jpg")
bullet_img = pygame.image.load("bullet.jpg")
background_img = pygame.image.load("background.jpg")


# Scale images
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (50, 50))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Game variables
player_speed = 7
bullet_speed = -10
enemy_speed = 3
score = 0
game_over = False

# Font
font = pygame.font.Font(None, 36)

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += player_speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -50)

    def update(self):
        self.rect.y += enemy_speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-150, -50)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += bullet_speed
        if self.rect.bottom < 0:
            self.kill()

# Sprite groups
player = Player()
player_group = pygame.sprite.GroupSingle(player)
enemies = pygame.sprite.Group([Enemy() for _ in range(5)])
bullets = pygame.sprite.Group()

# Main game loop
def main():
    global score, game_over

    while True:
        screen.blit(background_img, (0, 0))

        if not game_over:
            keys = pygame.key.get_pressed()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    bullets.add(bullet)

            # Update
            player_group.update(keys)
            bullets.update()
            enemies.update()

            # Collision detection
            for bullet in bullets:
                enemy_hit = pygame.sprite.spritecollideany(bullet, enemies)
                if enemy_hit:
                    bullet.kill()
                    enemy_hit.rect.x = random.randint(0, SCREEN_WIDTH - enemy_hit.rect.width)
                    enemy_hit.rect.y = random.randint(-150, -50)
                    score += 10

            if pygame.sprite.spritecollideany(player, enemies):
                game_over = True

            # Draw everything
            player_group.draw(screen)
            bullets.draw(screen)
            enemies.draw(screen)
            draw_text(f"Score: {score}", 10, 10, WHITE)

        else:
            draw_text("GAME OVER", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, RED)
            draw_text("Press R to Restart", SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 + 10, WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    restart_game()

        pygame.display.flip()
        clock.tick(FPS)

# Helper functions
def draw_text(text, x, y, color):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

def restart_game():
    global score, game_over
    score = 0
    game_over = False
    for enemy in enemies:
        enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
        enemy.rect.y = random.randint(-150, -50)
    main()

if __name__ == "__main__":
    main()
