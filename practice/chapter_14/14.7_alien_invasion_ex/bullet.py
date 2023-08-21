import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹的类"""
    def __init__(self, ai_game, camp = '', p_start = (0,1), p_target = (0,0)) -> None:
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)

        # 储存用浮点数表示的子弹位置
        self.camp = camp

        print(f"{p_start}   {p_target}")

        # 船就让子弹的底部在起点，外星人就让子弹顶部在起点
        if self.camp == 'ship':
            self.rect.midbottom = p_start
        elif self.camp == 'alien':
            self.rect.midtop = p_start

        # print(self.rect.midbottom)
        # print(ai_game.ship.rect.midtop)

        # 通过起点和目标点获得向量，并获得方向向量
        vector = (p_target[0] - p_start[0],
                    p_target[1] - p_start[1])
        self.direction = self._get_direcetion(vector)
        # print(f"vector:{vector}")
        # print(f"direction:{self.direction}")

    def update(self):
        """向上移动子弹"""
        # 更新子弹的准确位置
        self.rect.x += self.direction[0] * self.settings.bullet_speed
        self.rect.y += self.direction[1] * self.settings.bullet_speed

    def _get_direcetion(self, vector):
        """接受一个向量，输出一个方向向量"""
        v_length = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
        x_0 = vector[0] / v_length
        y_0 = vector[1] / v_length
        return (x_0, y_0)

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)