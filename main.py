import pygame

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Mighty Streamer')
background = pygame.image.load('images/bg_final.jpg')
pygame.font.init()

font = pygame.font.Font(None, 25)

size = width, height = 544, 320
screen = pygame.display.set_mode(size)
running = True
end = True

while running:
    if end:
        screen.fill('gray')
        over = font.render('GAME OVER', True, 'purple')
        screen.blit(over, (70, 100))

        restart = font.render('Нажмите на любую клавишу для продолжения', True, 'purple')
        screen.blit(restart, (70, 140))
    else:
        screen.fill('black')
        screen.blit(background, (0, 0))

        time_text = font.render('Время проведенное в игре: 0', True, 'purple')
        screen.blit(time_text, (0, 25))

        kill_text = font.render('Убито врагов: 0', True, 'purple')
        screen.blit(kill_text, (0, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            end = False

    pygame.display.flip()
