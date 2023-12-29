import pygame

pygame.init()

# Установка размера окна
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Задание цвета фона
background_color = (255, 255, 255)

# Задание цвета текста
text_color = (0, 0, 0)

# Задание шрифта
font = pygame.font.SysFont("Arial", 32)

# Создание кнопки
button_rect = pygame.Rect(320 - 100, 240, 200, 50)

# Создание текста
button_text = font.render("Играть", True, text_color)

# Задание координат текста внутри кнопки
text_rect = button_text.get_rect(center=button_rect.center)
go = 0

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                 go = 1
    if go == 1:
        pygame.quit()
        running = False
    else:

        # Очистка экрана
        screen.fill(background_color)

        # Рисование кнопки
        pygame.draw.rect(screen, (0, 0, 255), button_rect)

        # Рисование текста на кнопке
        screen.blit(button_text, text_rect)

        # Обновление экрана
        pygame.display.flip()

# Завершение работы Pygame
pygame.quit()