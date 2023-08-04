import sys

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from target import Target
from button import Button
from game_stats import GameStats

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
        self.targets = pygame.sprite.Group()

        # 界面初始化
        self.game_stats = GameStats(self)
        self.game_stats_msg = (
                'Hit: ' + str(self.game_stats.hit) + 
                '  Time:' + str(self.game_stats.taking_time))
        self.play_button = Button(self, 'Play')
        self.stats_button = Button(self, self.game_stats_msg, 'midtop')

        # 游戏状态初始化
        self.game_active = False

    def _creat_target(self):
        """生成一个靶子"""
        new_target = Target(self)
        new_target.rect.x = self.settings.screen_width - new_target.x * 3
        self.targets.add(new_target)

    def _fire_bullet(self):
        """子弹数小于限制时发射子弹"""
        if len(self.bullets) < self.settings.buttets_allow:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _game_accomplish(self):
        """游戏通关"""
        self.game_active = False
        self.play_button.set_button('Replay')
        pygame.mouse.set_visible(True)

    def _check_hit_target(self):
        """检测是否集中靶子"""
        
        # 碰撞检测
        if pygame.sprite.groupcollide(
            self.targets, self.bullets, True, True):
            self.game_stats.hit += 1
            self.game_stats_msg = (
            'Hit: ' + str(self.game_stats.hit) + 
            '  Time:' + str(self.game_stats.taking_time))
            self.stats_button.set_button(self.game_stats_msg)
        
        if self.game_stats.hit >= 3:
            self._game_accomplish()
            

    def _upgrade_elements(self):
        """游戏界面中各种元素的更新"""
        self.rocket.update()        # 火箭更新

        # 靶子更新
        if not self.targets:
            self._creat_target()
        for target in self.targets:
            target.update()

        # 子弹更新
        self.bullets.update()

        self._check_hit_target()

        # print(len(self.bullets))
        # 删除视野外子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        # print(self.targets)

    def _game_start(self):
        """游戏开始的各种动作"""
        # 重置统计信息
        self.game_active = True
        self.game_stats.reset()

        # 清空子弹列表
        self.bullets.empty()

        pygame.mouse.set_visible(False)

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

    def _check_play_button(self, mouse_pos):
        """检查是否按下开始按钮"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            self._game_start()
            
    def _check_event(self):
        """监听各种事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _upgrade_screen(self):
        """绘制游戏元素"""
        self.screen.fill((230, 230, 230))
        self.rocket.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        for target in self.targets:
            target.draw_target()
        if not self.game_active:
            self.play_button.draw_button()
        else:
            self.stats_button.draw_button()
        pygame.display.flip()

    def run(self):
        """游戏主循环"""
        while True:
            self._check_event()
            if self.game_active:
                self._upgrade_elements()
            self._upgrade_screen()
            self.clock.tick(60)
        
if __name__ == '__main__':
    # 创建游戏并运行
    side_shooting = SideShooting()
    side_shooting.run()
