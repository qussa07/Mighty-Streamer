import pygame
from enemy_mob import Mob

clock = pygame.time.Clock()
fps = 60
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Mighty Streamer')
background = pygame.image.load('images/bg.jpg')


class Player:
    def __init__(self, x, y):
        skin = pygame.image.load('images/Player/PlayerLeft/playerleft1.png')
        self.player = pygame.sprite.Sprite()
        self.player.image = skin
        self.player.rect = self.player.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.render = pygame.sprite.Group()
        self.render.add(self.player)
        self.health_points = 3
        self.count = 0
        self.flag = 1
        self.side = 0
        self.sides = ['Left', 'Right']
        self.playerleft1 = pygame.image.load(f'images/Player/PlayerLeft/playerleft1.png').convert_alpha()
        self.playerleft2 = pygame.image.load(f'images/Player/PlayerLeft/playerleft2.png').convert_alpha()
        self.playerleft3 = pygame.image.load(f'images/Player/PlayerLeft/playerleft3.png').convert_alpha()
        self.playerleft4 = pygame.image.load(f'images/Player/PlayerLeft/playerleft4.png').convert_alpha()
        self.playerRight1 = pygame.image.load(f'images/Player/PlayerRight/playerRight1.png').convert_alpha()
        self.playerRight2 = pygame.image.load(f'images/Player/PlayerRight/playerRight2.png').convert_alpha()
        self.playerRight3 = pygame.image.load(f'images/Player/PlayerRight/playerRight3.png').convert_alpha()
        self.playerRight4 = pygame.image.load(f'images/Player/PlayerRight/playerRight4.png').convert_alpha()

    def rendering(self, screen, frame):
        if self.flag == 2:
            if frame == 2:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}1.png').convert_alpha()
                self.player.rect.y = 620
            elif frame == 4:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}2.png').convert_alpha()
            elif frame == 6:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}3.png').convert_alpha()
            elif frame == 8:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}4.png').convert_alpha()
                self.flag = 1
                self.player.rect.y = 700
        elif self.flag == 1:
            if self.side == 1:
                self.player.image = self.playerRight1
                self.flag = 0
            else:
                self.player.image = self.playerleft1
                self.flag = 0
        if self.side:
            self.player.rect = self.player.image.get_rect(center=(self.x, self.y))
        else:
            self.player.rect = self.player.image.get_rect(center=(self.x, self.y))
        self.render.draw(screen)

    def walk_left(self, frame):
        if frame == 7:
            self.player.image = self.playerleft1
        elif frame == 14:
            self.player.image = self.playerleft2
        elif frame == 21:
            self.player.image = self.playerleft3
        elif frame == 28:
            self.player.image = self.playerleft4
        self.x -= 4
        self.side = 0

    def walk_right(self, frame):
        if frame == 7:
            self.player.image = self.playerRight1
        elif frame == 14:
            self.player.image = self.playerRight2
        elif frame == 21:
            self.player.image = self.playerRight3
        elif frame == 28:
            self.player.image = self.playerRight4
        self.x += 4
        self.side = 1

    def check(self, frame):
        if frame == 28:
            frame = 0

        return frame

    def attack(self):
        self.flag = 2

    def jump(self):
        pass


size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
main_character = Player(60, 780)
mob = Mob(500, 580)
frame = 0
running = True
while running:
    frame += 1

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP and (event.key == pygame.K_d or event.key == pygame.K_a):
            if keys[pygame.K_d]:
                main_character.walk_right(7)
            if keys[pygame.K_a]:
                main_character.walk_left(7)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                main_character.attack()
        elif event.type == pygame.K_SPACE:
            main_character.jump()
    main_character.rendering(screen, frame)
    mob.rendering(screen, frame)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        main_character.walk_right(frame)
    if keys[pygame.K_a]:
        main_character.walk_left(frame)
    frame = main_character.check(frame)
    frame1 = mob.check(frame)
    clock.tick(fps)
    pygame.display.flip()
