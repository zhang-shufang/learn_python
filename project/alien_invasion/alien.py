import time
import pygame
from pygame.sprite import Sprite

from settings import Settings

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_game) -> None:
        """类初始化"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings    # 这里从主程序走
        
        # 加载图片和碰撞区
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人位置初始化
        self.x = self.rect.x = self.rect.width
        self.y = self.rect.y = self.rect.height
        self.speed = self.settings.alien_speed

    def check_edges(self):
        """如果舰队触及边缘，则运动反向"""
        screen_rect = self.screen.get_rect()
        # print(self.rect.right, self.rect.left, self.rect.x, self.rect.width)
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """外星人位置更新"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        # self.print_coordinates()

    def print_coordinates(self):
        """用于调试打印坐标"""
        print(self.x, self.y, self.rect.x, self.rect.y)