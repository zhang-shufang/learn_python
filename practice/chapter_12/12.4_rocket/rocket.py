import pygame

class Rocket:
    """管理火箭的类"""
    def __init__(self, rocket_game) -> None:
        """初始化火箭并设置其初始位置"""
        # 屏幕属性
        self.screen = rocket_game.screen                    # 关于屏幕的属性
        self.screen_rect = rocket_game.screen.get_rect()    # 关于屏幕的碰撞尺寸的属性
        # print(rocket_game.screen.get_rect())    
        

        # 飞船初始化
        self.image = pygame.image.load("images/rocket.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船属性
        self.speed = float(5)                               # 飞船速度
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """飞船移动"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed

        # 将位置更新
        self.rect.x = self.x
        self.rect.y = self.y