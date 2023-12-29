import pygame

pygame.init()
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
background_color = (255, 255, 255)
text_color = (0, 0, 0)
font = pygame.font.SysFont("Arial", 32)
button_rect = pygame.Rect(320 - 100, 240, 200, 50)
button_text = font.render("Играть", True, text_color)
text_rect = button_text.get_rect(center=button_rect.center)
go = 0

running = True
while running:
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
        screen.fill(background_color)
        pygame.draw.rect(screen, (0, 0, 255), button_rect)
        screen.blit(button_text, text_rect)
        pygame.display.flip()

pygame.quit()
