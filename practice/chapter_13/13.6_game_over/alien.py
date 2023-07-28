import pygame
from pygame.sprite import Sprite
from random import randint
import time

from settings import Settings

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, game) -> None:
        """类初始化"""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.settings = game.settings    # 这里从主程序走
        
        # 加载图片和碰撞区
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人运动初始，每隔一段时间，变换一次方向
        self.x = self.rect.x = self.rect.width
        self.y = self.rect.y = self.rect.height
        self.speed = self.settings.alien_speed
        self.direction = 1
        self.time_0 = time.time()
        self.time_trigger = 0

        # 外星人射击初始化
        self.number_of_bullets = 0
        self.ready_to_fire = True
        self.timer = 0
        self.loading_time = 2

    def _reloading(self):
        """装弹函数，一段时间后可以发射"""
        if not self.ready_to_fire:
            loading_time = time.time() - self.timer
            # print(loading_time)
            if loading_time > self.loading_time:
                self.ready_to_fire = True
                self.timer = time.time()

    def _change_direct(self):
        """改变飞船移动方向"""
        self.direction *= -1

    def check_edges(self):
        """如果舰队触及边缘，则运动反向"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top:
            touch_edges = True
        else:
            touch_edges = False
        return touch_edges
    
    def update(self):
        """外星人位置更新"""
        # 每隔一段随机时间改变方向
        # 或是到达边缘后改变方向
        interval = time.time() - self.time_0
        if not self.time_trigger:
            self.time_trigger = randint(1, 4)
        # print(interval, self.time_trigger)
        
        if interval > self.time_trigger:
            self.time_0 = time.time()
            self.time_trigger = 0
            number = randint(0, 99)
            if number // 2:
                self._change_direct()
        elif self.check_edges():
            self._change_direct()

        self.y += self.settings.alien_speed * self.direction
        self.rect.y = self.y
        # self.print_coordinates()

        self._reloading()

    def print_coordinates(self):
        """用于调试打印坐标"""
        print(self.x, self.y, self.rect.x, self.rect.y)