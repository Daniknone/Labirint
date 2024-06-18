from os import path
import pygame
import sys
import random

h = 0
h = ""
h = []
h = False
h = 0.232


WIDTH = 1024 -64
HEIGHT = 1024 -64
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player_runL = True
player_runR = True
player_runU = True
player_runD = True
running = True
block_position = [0,0]
qiutx = 0
qiuty = 0
img_dir = path.join(path.dirname(__file__), 'New Piskel (8).png','New Piskel (6).png')

blocks = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.image = player_img
        self.rect = self.image.get_rect()
        # self.rect.center = (272,0)




    def update(self):

        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and player_runL == True:
            self.speedx = -4
        if keystate[pygame.K_RIGHT] and player_runR == True:
            self.speedx = 4
        if keystate[pygame.K_UP] and player_runU == True:
            self.speedy = -4
        if keystate[pygame.K_DOWN] and player_runD == True:
            self.speedy = 4

        player1 = Player()
        player1.image = pygame.Surface((32,32))
        player1.rect.x = self.rect.x + self.speedx
        player1.rect.y = self.rect.y + self.speedy


        hitLocal = pygame.sprite.spritecollide(player1, blocks, False)
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
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

class Qiut(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 0
        self.speedy = 0

# Создаем игру и окно
pygame.init()
background = pygame.image.load("New Piskel (8).png")
background = pygame.image.load("New Piskel (6).png")
background_rect = background.get_rect()
player_img = pygame.image.load("New Piskel (8).png")
Block_img  = pygame.image.load("New Piskel (6).png")
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()




PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
level = [
        "  ------E---------------------",
        "-------      ----          ---",
        "-------- ---- ---  ---- ------",
        "-------- ----Q---- ---- ---- -",
        "-------- ---        --       -",
        "----         -----------------",
        "---- ------  -----------------",
        "---- ------            -------",
        "--          -------- ---------",
        "-- ------             --------",
        "-       -------- ---- --------",
        "-------                  -----",
        "--    ------------     -------",
        "-----     -----      -------- ",
        "---------   --------      ----",
        "---------- --------   --------",
        "----------              ------",
        "---------- -------------------",
        "-            -----------------",
        "-     ---             --------",
        "-- --------------  -----------",
        "-- --------------            -",
        "-          -------------------",
        "- ------- --------        ----",
        "-  ------      ---- ----- ----",
        "-- ----------       ---   ----",
        "-  ----       ------------  --",
        "-  ---  ----            ---- -",
        "-- ----           -----      -",
        "------------------------------",]



xp = -16
yp = -16
x = 0
y = 0  # координаты
for row in level:  # вся строка
        yp += 32
        for col in row:  # каждый символ
            if xp == 944:
                xp = -16
            xp += 32

            if col == "-":
                pf = Block(x,y)
                all_sprites.add(pf)
                blocks.add(pf)

            if col == "E":
                ef = Enter(x, y)
                all_sprites.add(ef)
                player.rect.x = x
                player.rect.y = y
            if col == "Q":
                ef = Qiut(x, y)
                qiutx = x
                qiuty = y
                all_sprites.add(ef)


            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT    #то же самое и с высотой
        x = 0


all_sprites.add(player)


# Цикл игры
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    if player.rect.x == qiutx and player.rect.y == qiuty:
        running = False

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()






