import pygame 
import sys 
from hero import Hero 
from enemy import Enemy 
import random 
 
class Bullet(pygame.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__() 
        self.image = pygame.image.load("img/m.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (x, y) 
        self.speed = 5 
 
    def update(self): 
        self.rect.y -= self.speed 
 
def start_game(): 
    pygame.init() 
    screen = pygame.display.set_mode((600, 600)) 
    pygame.display.set_caption("Самая лучшая игра для новогоднего настроения") 
 
    background = pygame.image.load("img/o.jpg") 
 
    hero = Hero(screen) 
    bullets = pygame.sprite.Group()  # Create a group for bullets 
    enemies = pygame.sprite.Group()  # Create a group for enemies 
 
    clock = pygame.time.Clock() 
    spawn_interval = 1000  # Интервал в миллисекундах между спавном врагов 
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
 
    lives = 3  # Initialize the number of lives 
    score = 0  # Initialize the score variable 
 
    def spawn_enemy(): 
        num_enemies = random.randint(1, 5)  # Случайное количество врагов от 1 до 5 
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
                    bullets.add(bullet)  # Add the bullet to the bullets group 
 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a] or keys[pygame.K_a]: 
            speed_x -= acceleration 
        if keys[pygame.K_d] or keys[pygame.K_d]: 
            speed_x += acceleration 
 
        # Применяем замедление при отпускании клавиш 
        if not keys[pygame.K_a] and not keys[pygame.K_a]: 
            if speed_x < 0: 
                speed_x += deceleration 
        if not keys[pygame.K_d] and not keys[pygame.K_d]: 
            if speed_x > 0: 
                speed_x -= deceleration 
 
        # Ограничиваем скорость 
        speed_x = max(-max_speed, min(max_speed, speed_x)) 
        speed_y = max(-max_speed, min(max_speed, speed_y)) 
 
        hero.rect.x += speed_x 
        hero.rect.y += speed_y 
 
        # Обновляем и отображаем пули 
        bullets.update() 
        bullets.draw(screen) 
 
        # Проверяем границы экрана 
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
 
        # Обновляем и отображаем врагов 
        enemies.update() 
        enemies.draw(screen) 
 
        # Проверяем столкновение пуль с врагами 
        collisions = pygame.sprite.groupcollide(bullets, enemies, True, True) 
 
        # Увеличиваем счет при уничтожении врага 
        score += len(collisions) 
 
        # Проверяем, если враг достиг нижней границы экрана, убавляем жизнь 
        for enemy in enemies: 
            if enemy.rect.bottom > screen.get_height(): 
                lives -= 1 
                enemies.remove(enemy) 
 
        # Отображаем индикатор жизней 
        heart_image = pygame.image.load("img/heart.png")