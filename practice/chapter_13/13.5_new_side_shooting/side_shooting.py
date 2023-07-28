import sys
from typing import Tuple

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien

class SideShooting:
    """横向射击的主游戏类"""
    def __init__(self) -> None:
        # 游戏窗口初始化
        self.settings = Settings()
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Side Shooting')

        # 帧率初始化
        self.clock = pygame.time.Clock()

        # 游戏元素初始化
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def _creat_alien(self):
        """生成一个外星人"""
        new_alien = Alien(self)
        new_alien.rect.x = self.settings.screen_width - new_alien.x * 3
        self.aliens.add(new_alien)

    def _fire_bullet(self):
        """子弹数小于限制时发射子弹"""
        if len(self.bullets) < self.settings.buttets_allow:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _upgrade_elements(self):
        """游戏界面中各种元素的更新"""
        self.rocket.update()        # 火箭更新

        # 外星人更新
        if not self.aliens:
            self._creat_alien()
        for alien in self.aliens:
            alien.update()

        # 子弹更新
        self.bullets.update()

        # 碰撞检测
        pygame.sprite.groupcollide(
            self.aliens, self.bullets, True, True)

        # print(len(self.bullets))
        # 删除视野外子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        # print(self.aliens)

    def _check_keyup_events(self, event):
        """对抬起事件进行反应"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _check_keydown_events(self, event):
        """对按下事件进行反应"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_event(self):
        """监听各种事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _upgrade_screen(self):
        """绘制游戏元素"""
        self.screen.fill((230, 230, 230))
        self.rocket.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """游戏主循环"""
        while True:
            self._check_event()
            self._upgrade_elements()
            self._upgrade_screen()
            self.clock.tick(60)
        
if __name__ == '__main__':
    # 创建游戏并运行
    side_shooting = SideShooting()
    side_shooting.run()
