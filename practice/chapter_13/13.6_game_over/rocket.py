import pygame

class Rocket:
    """管理火箭的类"""
    def __init__(self, rocket_game) -> None:
        """初始化火箭"""
        # 窗口信息初始化
        self.screen = rocket_game.screen
        self.screen_rect = self.screen.get_rect()

        # 加载火箭图片并获取其外接矩形
        self.image = pygame.image.load("images/rocket_small.png")
        self.rect = self.image.get_rect()

        # 飞船坐标及运动初始化
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)     # 坐标
        self.speed = rocket_game.settings.rocket_speed    # 运动速度
        self.moving_up = False          # 向上运动状态
        self.moving_down = False        # 向下运动状态

    def blitme(self):
        """在执行位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.y = self.y

    def reset(self):
        """飞船被击落后进行重置"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y

