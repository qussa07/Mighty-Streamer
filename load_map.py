import pygame

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

tile_images = {
    'block': pygame.image.load('images/blockDirth.png')
}
tile_width = tile_height = 300

def load_level(filename):
    filename = filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))
    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))

def generate_level(level, screen):
    x, y = 0, 0
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '#':
                screen.blit(tile_images['block'], (tile_width * x, tile_height * y))

    return tiles_group



size = WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    generate_level(load_level('map.txt'), screen)
    pygame.display.flip()
