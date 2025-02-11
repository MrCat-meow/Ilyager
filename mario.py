import pygame
from settings import WIDTH, HEIGHT, FPS, TITLE, SKY_BLUE
from mario import Mario
from level import Level, level_data

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Создание уровня
level = Level(level_data)

# Создание Mario
mario = Mario(level.player_start_x, level.player_start_y)
all_sprites = pygame.sprite.Group()
all_sprites.add(mario)

# Игровой цикл
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update(level.platforms)  # Передаем платформы для обработки коллизий
    level.update()

    # Рендеринг
    screen.fill(SKY_BLUE)  # Заполняем экран голубым цветом

    # Рисуем уровень
    level.draw(screen)

    # Рисуем спрайты
    all_sprites.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
