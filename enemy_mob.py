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
        self.mframe = 0
        skin = pygame.image.load('images/MobSprite/MobLeft/MobLethalLeft1.png')
        self.mob = pygame.sprite.Sprite()
        self.mob.image = skin
        self.mob.rect = self.mob.image.get_rect(center=(x, y))
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
        if mframe < 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight1.png')
        elif 7 <= mframe < 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight2.png')
        elif 14 <= mframe < 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight3.png')
        elif 21 <= mframe < 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobAttackRight/MobAttackRight4.png')

    def rendering(self, screen, frame):
        if self.mob.rect.x > player.player.rect.x:
            self.mob_left(self.mframe)
        elif self.mob.rect.x < player.player.rect.x:
            self.mob_right(self.mframe)

        self.render.draw(screen)

    def mob_left(self, mframe):
        if mframe < 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft1.png')
        elif 7 <= mframe < 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft2.png')
        elif 14 <= mframe < 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft3.png')
        elif 21 <= mframe < 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft4.png')
        self.mob.rect.x -= 1

    def mob_right(self, mframe):
        if mframe == 7:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight1.png')
        elif mframe == 14:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight2.png')
        elif mframe == 21:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight3.png')
        elif mframe == 28:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight3.png')
        self.mob.rect.x += 1

    def check(self, mframe):
        if mframe > 28:
            mframe = 0

        return mframe

    # def follow_player(self, player):
    #
    #
    #     if self.mob.rect.x > player.player.rect.x:
    #         self.mob_left(self.mframe)
    #     elif self.mob.rect.x < player.player.rect.x:
    #         self.mob_right(self.mframe)


if __name__ == '__main__':
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

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
