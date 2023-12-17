import pygame

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
        self.player.rect = self.player.image.get_rect()
        self.render = pygame.sprite.Group()
        self.render.add(self.player)
        self.player.rect.x = x
        self.player.rect.y = y
        self.health_points = 3
        self.count = 0
        self.flag = 0
        self.side = 0
        self.sides = ['Left', 'Right']

    def rendering(self, screen, frame):
        if self.flag == 2:
            if frame == 2:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}1.png')
                self.player.rect.y = 620
            elif frame == 4:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}2.png')
            elif frame == 6:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}3.png')
            elif frame == 8:
                self.player.image = pygame.image.load(
                    f'images/Player/Player{self.sides[self.side]}Sword/PlayerAttack{self.sides[self.side]}4.png')
                self.flag = not self.flag
                self.player.rect.y = 700
        self.render.draw(screen)

    def walk_left(self, frame):
        if frame == 7:
            self.player.image = pygame.image.load(f'images/Player/Playerleft/playerleft1.png')
        elif frame == 14:
            self.player.image = pygame.image.load(f'images/Player/PlayerLeft/playerleft2.png')
        elif frame == 21:
            self.player.image = pygame.image.load(f'images/Player/PlayerLeft/playerleft3.png')
        elif frame == 28:
            self.player.image = pygame.image.load(f'images/Player/PlayerLeft/playerleft4.png')
        self.player.rect.x -= 4
        self.side = 0

    def walk_right(self, frame):
        if frame == 7:
            self.player.image = pygame.image.load(f'images/Player/PlayerRight/playerRight1.png')
        elif frame == 14:
            self.player.image = pygame.image.load(f'images/Player/PlayerRight/playerRight2.png')
        elif frame == 21:
            self.player.image = pygame.image.load(f'images/Player/PlayerRight/playerRight3.png')
        elif frame == 28:
            self.player.image = pygame.image.load(f'images/Player/PlayerRight/playerRight4.png')
        self.player.rect.x += 4
        self.side = 1

    def check(self, frame):
        if frame == 28:
            frame = 0

        return frame

    def attack(self):
        self.flag = 2


size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
main_character = Player(60, 700)
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
    main_character.rendering(screen, frame)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        main_character.walk_right(frame)
    if keys[pygame.K_a]:
        main_character.walk_left(frame)
    frame = main_character.check(frame)
    clock.tick(fps)
    pygame.display.flip()
