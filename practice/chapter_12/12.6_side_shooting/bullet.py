import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, rocket_game) -> None:
        # 界面初始化
        self.screen = rocket_game.screen

        # 子弹图像初始化
        super().__init__()
        self.color = (60, 60, 60)
        self.bullet_width = 15
        self.bullet_height = 3

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect= pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = rocket_game.rocket.rect.midright

        # 子弹运动初始化
        self.x = self.rect.x
        self.speed = 15.0

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self):
        """子弹向右移动"""
        self.x += self.speed
        self.rect.x = self.x

    
