import sys

import pygame

from rocket import Rocket

class RocketGame:
    """火箭游戏的主程序类"""
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))  # 设定屏幕尺寸

        self.clock = pygame.time.Clock()                    # 创建时钟

        pygame.display.set_caption('Rocket Game')                # ？？

        self.rocket = Rocket(self)

    def run_game(self):
        """游戏主循环"""
        while True:
            self._check_events()
                        
            self.rocket.update()
            self.screen.fill((230, 230, 230))               # 屏幕颜色
            self.rocket.blitme()
            pygame.display.flip()                           # 创建屏幕
        
            self.clock.tick(60)                             # 确保帧率

    def _check_events(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:    
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """监听按下事件，并作出相应的动作"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
    
    def _check_keyup_events(self, event):
        """监听抬起事件，并作出相应的动作"""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False

if __name__ == '__main__':
    # 创建游戏实例并运行
    rocket_game = RocketGame()
    rocket_game.run_game()
