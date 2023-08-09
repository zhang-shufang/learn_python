import pygame
from pygame.sprite import Sprite
from random import randint
import time

from settings import Settings

class Target(Sprite):
    """表示单个靶子的类"""
    def __init__(self, game) -> None:
        """类初始化"""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.settings = game.settings    # 这里从主程序走

        # 设置靶子的颜色和尺寸
        self.color = self.settings.target_color
        self.width = self.settings.target_width
        self.height = self.settings.target_height

        # 在（0，0）处创建一个靶子，并设置正确的位置
        self.rect= pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright

        # 靶子运动初始，每隔一段时间，变换一次方向
        self.x = self.rect.x = self.rect.width
        self.y = self.rect.y = self.rect.height
        self.speed = self.settings.target_speed
        self.direction = 1
        self.time_0 = time.time()
        self.time_trigger = 0

    def _change_direct(self):
        """改变飞船移动方向"""
        self.direction *= -1

    def check_edges(self):
        """如果靶子触及边缘，则运动反向"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top:
            touch_edges = True
        else:
            touch_edges = False
        return touch_edges
    
    def update(self):
        """靶子位置更新"""
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

        self.y += self.speed * self.direction
        self.rect.y = self.y
        # self.print_coordinates()

    def draw_target(self):
        """用于绘制靶子"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def print_coordinates(self):
        """用于调试打印坐标"""
        print(self.x, self.y, self.rect.x, self.rect.y)