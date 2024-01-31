import pygame

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Mighty Streamer')
background = pygame.image.load('images/bg.png')
pygame.font.init()


font = pygame.font.Font(None, 90)

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
running = True
go = True

while running:

    screen.fill('gray')
    over = font.render('YOU WIN!', True, 'purple')
    screen.blit(over, ((1920 // 2) - 170, 1080 // 2 - 80))

    restart = font.render('Нажмите на любую клавишу для закрытия', True, 'purple')
    screen.blit(restart, (160, 1080 // 2))

    kill = font.render(f'кол-во убийств - {1}', True, 'purple')
    screen.blit(kill, (1920 - 900, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pygame.quit()

    pygame.display.flip()
