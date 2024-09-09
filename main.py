from time import sleep

import pygame
import levels
import time

WIDTH = 1024 - 64
HEIGHT = 1024 - 64
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
LITE_BLUE = (100,100,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128,128,128)

speed = 8


running = True
level_number = 0

quit_by_levelx = []
quit_by_levely = []

blocks_by_level = []
cannon_by_level = [[]]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bullet_image = pygame.image.load("bullet.png")

for i in levels.all_levels:
    blocks_by_level.append(pygame.sprite.Group())

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image = player_img
        self.rect = self.image.get_rect()

    def update(self):

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -speed
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = speed
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedy = -speed
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedy = speed

        player1 = Player()
        player1.image = pygame.Surface((32,32))
        player1.rect.x = self.rect.x + self.speedx
        player1.rect.y = self.rect.y + self.speedy


        hitLocal = pygame.sprite.spritecollide(player1, blocks_by_level[level_number], False)
        if hitLocal:
            return

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen1):
        screen1.blit(self.image, self.rect)

class Cannon(pygame.sprite.Sprite):
    bullet = Bullet(0, 0)
    angle = 0

    def __init__(self,x,y,angle1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image = cannon_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0
        self.image = pygame.transform.rotate(self.image,angle1)
        self.angle = angle1

    def draw(self, screen1):
        self.bullet = Bullet(self.rect.x, self.rect.y)
        self.bullet.image = pygame.transform.rotate(self.bullet.image,self.angle)
        self.bullet.draw(screen)

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image = Block_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

class Enter(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image = Enter_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

class Qiut(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image = Qiut_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0


# Создаем игру и окно
pygame.init()
print("init")


Enter_img = pygame.image.load("l0_sprite_1.png")
Qiut_img = pygame.image.load("l0_sprite_2.png")
player_img = pygame.image.load("New Piskel (8).png")
Block_img = pygame.image.load("New Piskel (6).png")
cannon_image = pygame.image.load("cannon.png")

pygame.mixer.init()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites_by_level = []
for i in levels.all_levels:
    all_sprites_by_level.append(pygame.sprite.Group())
    cannon_by_level.append([])

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


for i in range(len(all_sprites_by_level)):
    player = Player()
    xp = -16
    yp = -16
    x = 0
    y = 0  # координаты
    for row in levels.all_levels[i]:  # вся строка
            yp += 32
            for col in row:  # каждый символ
                if xp == 944:
                    xp = -16
                xp += 32

                if col == "-":
                    pf = Block(x,y)
                    all_sprites_by_level[i].add(pf)
                    blocks_by_level[i].add(pf)

                if col == "E":
                    ef = Enter(x, y)
                    all_sprites_by_level[i].add(ef)
                    player.rect.x = x
                    player.rect.y = y
                if col == "Q":
                    ef = Qiut(x, y)
                    quit_by_levelx.append(x)
                    quit_by_levely.append(y)
                    all_sprites_by_level[i].add(ef)
                if col == "↓":
                    cn = Cannon(x,y,180)
                    all_sprites_by_level[i].add(cn)
                    blocks_by_level[i].add(cn)
                    cannon_by_level[i].append(cn)
                if col == "↑":
                    cn = Cannon(x,y,0)
                    all_sprites_by_level[i].add(cn)
                    blocks_by_level[i].add(cn)
                    cannon_by_level[i].append(cn)
                if col == "←":
                    cn = Cannon(x,y,90)
                    all_sprites_by_level[i].add(cn)
                    blocks_by_level[i].add(cn)
                    cannon_by_level[i].append(cn)
                if col == "→":
                    cn = Cannon(x,y,-90)
                    all_sprites_by_level[i].add(cn)
                    blocks_by_level[i].add(cn)
                    cannon_by_level[i].append(cn)

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT     # то же самое и с высотой
            x = 0


    all_sprites_by_level[i].add(player)

# Цикл игры
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites_by_level[level_number].update()

    player_idx = len(all_sprites_by_level[level_number].sprites()) - 1
    if (all_sprites_by_level[level_number].sprites()[player_idx].rect.x == quit_by_levelx[level_number] and
            all_sprites_by_level[level_number].sprites()[player_idx].rect.y == quit_by_levely[level_number]):
        # all_sprites_by_level[level_number].remove()

        if level_number == len(levels.all_levels) - 1:
            running = False
        # level_number = level_number + 1
        level_number += 1

        #running = False  # Переход на новый уровень
        # all_sprites.empty()

    # Рендеринг
    screen.fill(GRAY)
    all_sprites_by_level[level_number].draw(screen)

    for cn in cannon_by_level[level_number]:
        cn.draw(screen)
    # После отрисовки всего, переворачиваем экран

    # bullet = Bullet(23, 23)
    # bullet.draw(screen)
    pygame.display.flip()

pygame.quit()






