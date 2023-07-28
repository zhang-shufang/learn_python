from multiprocessing.spawn import import_main_path
import sys
from time import sleep

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

class SideShooting:
    """横向射击的主游戏类"""
    def __init__(self) -> None:
        # 游戏窗口初始化
        self.settings = Settings()
        self.game_stats = GameStats(self)
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
        self.rocket_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.aliens_bullets = pygame.sprite.Group()

        # 游戏状态初始化
        self.game_active = True

    # 外星人相关函数——————
    def _alien_fire_bullet(self):
        """外星人飞船发射子弹，
            有子弹数量限制，且随机发射"""
        for alien in self.aliens:
            if alien.ready_to_fire:
                # if len(self.aliens_bullets) < self.settings.buttets_allow_alien:
                new_bullet = Bullet(self, alien, -1)
                self.aliens_bullets.add(new_bullet)
                alien.ready_to_fire = False

    def _check_aliens_bullets(self):
        """检查外星人射出的子弹情况"""
        self.aliens_bullets.update()

        # 检查子弹与火箭的碰撞情况
        if pygame.sprite.spritecollideany(self.rocket, self.aliens_bullets):
            self._rocket_hit()

        # 界面外子弹消失
        for bullet in self.aliens_bullets.copy():
            if bullet.rect.right < 0:
                self.aliens_bullets.remove(bullet)

    def _creat_alien(self):
        """生成一个外星人"""
        new_alien = Alien(self)
        new_alien.rect.x = self.settings.screen_width - new_alien.x * 3
        self.aliens.add(new_alien)
    
    # 火箭相关函数——————
    def _rocket_hit(self):
        """控制火箭被击落的函数"""
        if self.game_stats.rocket_left > 0:
            self.rocket.reset()
            self.game_stats.rocket_left -= 1
        else:
            self.game_active = False
        sleep(1)
        print(self.game_stats.rocket_left)

    def _rocket_fire_bullet(self):
        """火箭子弹数小于限制时发射子弹"""
        if len(self.rocket_bullets) < self.settings.buttets_allow_rocket:
            new_bullet = Bullet(self, self.rocket, 1)
            self.rocket_bullets.add(new_bullet)

    def _check_rocket_bollets(self):
        """检查火箭的子弹运行情况"""
        self.rocket_bullets.update()

        # 检查子弹的碰撞情况，并记录击落数量
        hit_aliens = pygame.sprite.groupcollide( 
            self.aliens, self.rocket_bullets, True, True)
        if hit_aliens:
            self.game_stats.hit_aliens += 1
            print(self.game_stats.hit_aliens)

        # 删除视野外子弹
        for bullet in self.rocket_bullets.copy():
            if bullet.rect.left > self.screen_rect.right:
                self.rocket_bullets.remove(bullet)

    # 主程序相关函数——————
    def _upgrade_elements(self):
        """游戏界面中各种元素的更新"""
        self.rocket.update()        # 火箭更新

        self._check_rocket_bollets()

        # 外星人更新
        if not self.aliens:
            self._creat_alien()
        for alien in self.aliens:
            alien.update()

        self._alien_fire_bullet()
        self._check_aliens_bullets()

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
            self._rocket_fire_bullet()

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
        for bullet in self.rocket_bullets:
            bullet.draw_bullet()
        for bullet in self.aliens_bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
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
