from re import S
import sys
from time import sleep
from xmlrpc.client import FastParser

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """外星人入侵游戏的主程序类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        # 设置信息导入
        self.settings = Settings()

        # 屏幕初始化
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
          (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')    # ??

        # 统计信息导入
        self.game_stats = GameStats(self)
        self.game_stats.reset_stats()
        self.play_time = 0
        
        # 界面中的可见元素
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._generate_fleet()

        # 游戏开始状态
        self.game_active = False

        # 游戏界面元素
        self.play_button = Button(self, 'Play')
        self.scoreboard = Scoreboard(self)
    
    # 飞船函数组
    def _ship_hit(self):
        """飞船被撞击"""
        # 剩余飞船数量减少
        if self.game_stats.ship_left > 0:
            self.game_stats.ship_left -= 1    
            self.scoreboard.prep_ship()
            
            # 清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
            self._generate_fleet()
            self.ship.center_ship()
        else:
            self.game_active = False
            self.play_time += 1
            if self.play_time == 1:
                self.play_button.prep_msg('Replay')
            pygame.mouse.set_visible(True)
            
        # 暂停一会
        sleep(0.5)
    
    def _upgrade_bullets(self):
        """更新子弹位置，删除不需要的子弹"""
        self.bullets.update()
        self._check_bullet_alien_collisions()
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        # 检查是否有子弹击中了外星人
        # 如果是就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for aliens in collisions.values():
                self.game_stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            # 删除现有的子弹并创建一个新的外星舰队
            self.bullets.empty()
            self._generate_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.game_stats.level += 1
            self.scoreboard.prep_level()
    
    def _fire_bullet(self):
        """创建一个子弹，并让其加入编组bullets"""
        if len(self.bullets) < self.settings.buttets_allow:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # 外星人函数组
    def _check_fleet_edges(self):
        """在有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                # print("change")
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队向下移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _generate_fleet(self):
        """创建外星人舰队"""
        # 创建一个外星人，并填满一行。
        # 两个外星人中间空一个人。
        alien = Alien(self)
        gap_x = alien.rect.width
        gap_y = alien.rect.height

        current_x = gap_x
        current_y = gap_y
        while current_y < self.settings.screen_height - 4 * gap_y:
            while current_x < self.settings.screen_width - 2 * gap_x:
                self._creat_alien(current_x, current_y)
                current_x += 2 * gap_x
                # print(current_x, current_y)
            current_y += 2 * gap_y
            current_x = gap_x
    
    def _creat_alien(self, x, y):
        """基于x位置创建单个外星人"""
        new_alien = Alien(self)
        new_alien.x = new_alien.rect.x = x
        new_alien.y = new_alien.rect.y = y
        self.aliens.add(new_alien)
    
    def _upgrade_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        # print(self.game_stats.ship_left)
        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检测飞船是否到屏幕底部
        self._check_alien_bottom()

    def _check_alien_bottom(self):
        """检查是否有外星人到达底部"""
        for alien in self.aliens:
            if alien.rect.bottom > self.settings.screen_height:
                # 像飞船被撞到一样处理
                self._ship_hit()
                break


    # 游戏操控函数组
    def _check_keydown_events(self, event):
        """按下按键的操作"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True   # 向右移动飞船
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.game_stats.save_high_score()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        """抬起按键的操作"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # 停止向右移动
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """在玩家单击 Play 按钮时开始新游戏"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _check_events(self):
        # 响应案件和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_stats.save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    # 游戏流程函数组
    def _start_game(self):
        """游戏开始"""
        # 重置游戏统计信息
        self.game_stats.reset_stats()
        self.scoreboard.prep_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_ship()

        self.game_active = True
        self.settings.initialize_dynamic_setting()

        # 清空外星人列表和子弹列表
        self.bullets.empty()
        self.aliens.empty()

        # 创建一个新的外星舰队，并将飞船放在屏幕底部的中央
        self._generate_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)

    def _upgrade_screen(self):
        # 更新屏幕上的图像，并进行绘制
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.scoreboard.show_score()

        # 如果游戏处于非活动状态，就绘制 Play 按钮
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()   # 创建一个空屏幕

    def run_game(self):
        """游戏主循环"""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._upgrade_aliens()
                self._upgrade_bullets()
            
            self._upgrade_screen()            
            self.clock.tick(60)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()