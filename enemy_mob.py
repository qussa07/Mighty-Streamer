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
        skin = pygame.image.load('images/MobSprite/MobLeft/MobLethalLeft1.png')
        self.mob = pygame.sprite.Sprite()
        self.mob.image = skin
        self.mob.rect = self.mob.image.get_rect(center=(x, y))
        self.render = pygame.sprite.Group()
        self.render.add(self.mob)
        self.mob.rect.x = x
        self.mob.rect.y = y
        self.hp = 3

    def rendering(self, player):
        if self.mob.rect.x > player.x:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobLeft/MobLethalLeft1.png')

        elif self.mob.rect.x < player.x:
            self.mob.image = pygame.image.load(f'images/MobSprite/MobRight/MobLethalRight1.png')

        mob.render.draw(screen)


if __name__ == '__main__':
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    running = True
    mob.render.draw(screen)
    while running:
        screen.blit(background, (0, 0))

        mob.render.draw(screen)

        clock.tick(fps)
        pygame.display.flip()
