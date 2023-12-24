import pygame
import time
import random

clock = pygame.time.Clock()
fps = 60
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Mighty Streamer')
background = pygame.image.load('images/bg.jpg')


class Mob:
    def __init__(self, x, y):
        self.base_height = y
        self.mframe = 0
        skin = pygame.image.load('images/MobSprite/MobLeft/MobLethalLeft1.png')
        self.mob = pygame.sprite.Sprite()
        self.mob.image = skin
        self.mob.rect = self.mob.image.get_rect()
        self.render = pygame.sprite.Group()
        self.render.add(self.mob)
        self.mob.rect.x = x
        self.mob.rect.y = y
        self.hp = 3

    def attack_left(self, sc):
        if mframe == 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackLeft/MobAttackLeft1.png')

        elif mframe == 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackLeft/MobAttackLeft2.png')
        elif mframe == 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackLeft/MobAttackLeft3.png')
        elif mframe == 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackLeft/MobAttackLeft4.png')

    def attack_right(self, sc):
        if mframe == 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight1.png')
        elif mframe == 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight2.png')
        elif mframe == 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight3.png')
        elif mframe == 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight4.png')

    def rendering(self, screen):
        self.render.draw(screen)

    def mob_left(self, mframe):
        if mframe == 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft1.png')
        elif mframe == 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft2.png')
        elif mframe == 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft3.png')
        elif mframe == 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft4.png')
        self.mob.rect.x -= 2

    def mob_right(self, mframe):
        if mframe == 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight1.png')
        elif mframe == 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight2.png')
        elif mframe == 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight3.png')
        elif mframe == 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight3.png')
        self.mob.rect.x += 2

    def check(self, mframe):
        if mframe == 28:
            mframe = 0

        return mframe

    def follow_player(self, player):
        player_rect = player.get_rect()
        mob_rect = self.mob.rect

        # Проверяем столкновение
        if mob_rect.colliderect(player_rect):
            if self.mob.rect.x > player.player.rect.x:
                self.attack_left(screen)
            else:
                self.attack_right(screen)
            return

        # Оставляем ваш текущий код для перемещения моба
        if self.mframe < 28:
            self.mframe += 1
        else:
            self.mframe = 0

        if self.mob.rect.x > player.player.rect.x:
            self.mob_left(self.mframe)
        elif self.mob.rect.x < player.player.rect.x:
            self.mob_right(self.mframe)


size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)

mob = Mob(1000, 700)

mframe = 0
running = True
while running:
    mframe += 1
    screen.blit(background, (0, 0))

    mob.rendering(screen)

    mob.follow_player(main_character)

    mframe = mob.check(mframe)

    clock.tick(fps)
    pygame.display.flip()
