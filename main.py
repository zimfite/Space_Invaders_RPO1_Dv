import pygame 
import sys 
from hero import Hero 
from enemy import Enemy 
import random 
 
class Bullet(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__() 
        self.image = pygame.Surface((10, 10))  
        self.image.fill((255, 255, 255)) 
        self.rect = self.image.get_rect() 
        self.rect.center = (x, y) 
        self.speed = 5 
 
    def update(self): 
        self.rect.y -= self.speed 
 
def start_game(): 
    pygame.init() 
    screen = pygame.display.set_mode((800, 600)) 
    pygame.display.set_caption("Самая лучшая игра для новогоднего настроения") 
 
    background = pygame.image.load("img/o.jpg") 
 
    hero = Hero(screen) 
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
 
    clock = pygame.time.Clock() 
    spawn_interval = 1500 
    last_spawn_time = 0 
    flag = True 
 
    acceleration = 0.2 
    deceleration = 0.1 
    max_speed = 5 
    speed_x = 0 
    speed_y = 0 
 
    # ENEMY 
    max_enemies = 10 
    ENEMY_WIDTH = 50 
    ENEMY_HEIGHT = 50 
    SCREEN_WIDTH = 800 
 
    lives = 3 
    score = 0 
 
    def spawn_enemy(): 
        num_enemies = random.randint(1, 2)
        for _ in range(num_enemies): 
            x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH) 
            y = random.randint(-ENEMY_HEIGHT, 0) 
            enemy = Enemy(x, y) 
            enemies.add(enemy) 
 
    while flag and lives > 0: 
        screen.blit(background, (0, 0)) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                flag = False 
                sys.exit() 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    bullet = Bullet(hero.rect.centerx, hero.rect.top) 
                    bullets.add(bullet)
 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: 
            speed_x -= acceleration 
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: 
            speed_x += acceleration 
 
        if not keys[pygame.K_a] and not keys[pygame.K_LEFT]: 
            if speed_x < 0: 
                speed_x += deceleration 
        if not keys[pygame.K_d] and not keys[pygame.K_RIGHT]: 
            if speed_x > 0: 
                speed_x -= deceleration 
 
        speed_x = max(-max_speed, min(max_speed, speed_x)) 
        speed_y = max(-max_speed, min(max_speed, speed_y)) 
 
        hero.rect.x += speed_x 
        hero.rect.y += speed_y 
 
        bullets.update() 
        bullets.draw(screen) 
 
        if hero.rect.left < 0: 
            hero.rect.left = 0 
        if hero.rect.right > screen.get_width(): 
            hero.rect.right = screen.get_width() 
        if hero.rect.top < 0: 
            hero.rect.top = 0 
        if hero.rect.bottom > screen.get_height(): 
            hero.rect.bottom = screen.get_height() 
 
        current_time = pygame.time.get_ticks() 
 
        if current_time - last_spawn_time > spawn_interval: 
            spawn_enemy() 
            last_spawn_time = current_time 
 
        enemies.update() 
        enemies.draw(screen) 
 
        collisions = pygame.sprite.groupcollide(bullets, enemies, True, True) 
 
        score += len(collisions) 
 
        for enemy in enemies: 
            if enemy.rect.bottom > screen.get_height(): 
                lives -= 1 
                enemies.remove(enemy) 
 
        heart_image = pygame.image.load("img/heart.png")
        heart_rect = heart_image.get_rect() 
        for i in range(lives): 
            screen.blit(heart_image, (screen.get_width() - 10 - (i + 1) * (heart_rect.width + 5), 10)) 
 
        font = pygame.font.Font(None, 36) 
        score_text = font.render(f"Score: {score}", True, (255, 255, 255)) 
        screen.blit(score_text, (10, 50)) 
 
        hero.output_hero() 
 
        pygame.display.flip() 
        clock.tick(60) 
 
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 72) 
    game_over_text = font.render("Game Over", True, (255, 0, 0)) 
    restart_text = font.render("Press R to restart", True, (255, 255, 255)) 
    screen.blit(game_over_text, (200, 200)) 
    screen.blit(restart_text, (200, 300)) 
    pygame.display.flip() 
 
    while True: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_r: 
                    return 
 
start_game()
