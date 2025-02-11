import pygame
from sprites import Platform


class Level:
    def __init__(self, level_data):
        self.platforms = pygame.sprite.Group()
        self.player_start_x = 0
        self.player_start_y = 0

        for row_index, row in enumerate(level_data):
            for col_index, cell in enumerate(row):
                x = col_index * 50  # Пример размера блока
                y = row_index * 50
                if cell == 'X':  # 'X' представляет платформу
                    platform = Platform(x, y, 50, 50)
                    self.platforms.add(platform)
                elif cell == 'S':  # 'S' представляет стартовую позицию игрока
                    self.player_start_x = x
                    self.player_start_y = y

    def update(self):
        self.platforms.update()  # Если у платформ есть какая-либо логика обновления

    def draw(self, screen):
        for platform in self.platforms:
            screen.blit(platform.image, platform.rect)


# Пример данных уровня (простая карта)
level_data = [
    "XXXXXXXXXXXXXXXX",
    "X              X",
    "X   S          X",
    "X         XXX  X",
    "X              X",
    "XXXXXXXXXXXXXXXX",
]
