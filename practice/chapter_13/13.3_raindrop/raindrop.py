import pygame

from pygame.sprite import Sprite

class RainDrop(Sprite):
    """管理雨滴的类"""
    def __init__(self, game) -> None:
        """初始化"""
        super().__init__()

        # 游戏初始化
        self.screen = game.screen
        self.settings = game.settings

        # 图片和碰撞区域加载
        self.image = pygame.image.load("images/raindrop.png")
        self.rect = self.image.get_rect()

        # 运动相关初始化
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speed = self.settings.raindrop_speed

        # 生成雨滴相关
        self.has_checked_in = False

    def check_in(self):
        """判断雨滴是否出现在屏幕中"""
        if self.rect.top > 0 and (not self.has_checked_in):
            # print('check_in')
            # print(self.rect.top, self.rect.y)
            self.has_checked_in = True
            return True

    def check_out(self):
        """判断雨滴是否到达底边"""
        if self.rect.top > self.settings.screen_height:
            return True

    def update(self):
        """雨滴刷新，主要是运动"""
        self.rect.y += self.speed