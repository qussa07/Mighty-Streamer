import pygame

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Mighty Streamer')
background = pygame.image.load('images/bg.png')
pygame.font.init()


font = pygame.font.Font(None, 90)

size = width, height = 1600, 900
screen = pygame.display.set_mode(size)
running = True
go = True

while running:

    screen.fill('gray')
    over = font.render('WIN', True, 'purple')
    screen.blit(over, ((1600 // 2) - 100, 900 // 2))

    restart = font.render('Нажмите на любую клавишу для продолжения', True, 'purple')
    screen.blit(restart, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            end = False

    pygame.display.flip()
