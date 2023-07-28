import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """管理星星的类"""
    def __init__(self, stars) -> None:
        """类初始化"""
        super().__init__()
        self.screen = stars.screen

        # 加载图片和碰撞区
        self.image = pygame.image.load("images/star.png")
        self.rect = self.image.get_rect()

        # 星星位置属性
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

