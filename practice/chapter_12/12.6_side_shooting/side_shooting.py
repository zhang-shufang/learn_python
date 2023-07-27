import sys

import pygame

from rocket import Rocket
from bullet import Bullet

class SideShooting:
    """横向射击的主游戏类"""
    def __init__(self) -> None:
        # 游戏窗口初始化
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Side Shooting')

        # 帧率初始化
        self.clock = pygame.time.Clock()

        # 游戏元素初始化
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def run(self):
        """游戏主循环"""
        while True:
            self._check_event()
            self._upgrade_elements()
            self._upgrade_screen()
            self.clock.tick(60)
    
    def _upgrade_screen(self):
        """绘制游戏元素"""
        self.screen.fill((230, 230, 230))
        self.rocket.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()

    def _upgrade_elements(self):
        """游戏界面中各种元素的更新"""
        self.rocket.update()        # 火箭更新

        # 子弹更新
        self.bullets.update()
        print(len(self.bullets))
        # 删除视野外子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
    
    def _check_event(self):
        """监听各种事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """对按下事件进行反应"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """对抬起事件进行反应"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
if __name__ == '__main__':
    # 创建游戏并运行
    side_shooting = SideShooting()
    side_shooting.run()
