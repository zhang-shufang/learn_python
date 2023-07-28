import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, rocket_game, initial_position, direction) -> None:
        # 界面初始化
        self.screen = rocket_game.screen

        # 子弹图像初始化
        super().__init__()
        self.color = rocket_game.settings.bullet_color
        self.bullet_width = rocket_game.settings.bullet_width
        self.bullet_height = rocket_game.settings.bullet_height
        self.rect= pygame.Rect(0, 0, self.bullet_width, self.bullet_height)

        # 子弹运动初始化
        self.rect.center = initial_position.rect.center
        self.direction = direction
        self.x = self.rect.x
        self.speed = rocket_game.settings.bullet_speed

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def update(self):
        """子弹向右移动"""
        self.x += self.speed * self.direction
        self.rect.x = self.x

    
