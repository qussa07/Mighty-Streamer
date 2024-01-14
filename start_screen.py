import pygame

pygame.init()


class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont(None, 24)
        text_img = font.render(self.text, True, self.text_color)
        text_rect = text_img.get_rect(center=self.rect.center)
        screen.blit(text_img, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


def update(buttons, screen):
    for i in buttons:
        i.draw(screen)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
button0 = Button(-50,-55, 0, 0, '1 Уровень', 'WHITE', 'BLACK')
button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 55, 100, 50, '1 Уровень', 'WHITE', 'BLACK')
button1 = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, 100, 50, '2 Уровень', 'WHITE', 'BLACK')
button2 = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 55, 100, 50, '3 Уровень', 'WHITE', 'BLACK')

# Создаем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
go = 0
buttons = [button0, button, button1, button2]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in buttons:
                if i.rect.collidepoint(event.pos):
                    go = buttons.index(i)
                    print(go)
    if go:
        pygame.quit()
        running = False
    else:
        update([button, button1, button2], screen)
        pygame.display.flip()

pygame.quit()
