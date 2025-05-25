# Entity.py
import pygame
from Vector2 import Vector2

class Entity(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        try:
            self.image = pygame.image.load(filename).convert_alpha()
            self.position = Vector2(0, 0)
            print(f"Загружено изображение: {filename}")
        except Exception as e:
            print(f"Ошибка загрузки изображения: {str(e)}")
            self.image = pygame.Surface((32, 32))
            self.image.fill((255, 0, 0))  # Красный квадрат при ошибке

    def blit(self, screen):
        if screen and self.image:
            screen.blit(self.image, self.position.to_tuple())
            print(self.position.to_tuple())