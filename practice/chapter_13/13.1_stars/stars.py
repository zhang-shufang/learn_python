import sys
import pygame

from setting import Setting
from star import Star

class Stars:
    """生成星星的类"""
    def __init__(self) -> None:
        """初始化"""
        # 基础初始化
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode(
            (self.setting.screen_width, self.setting.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Stars')

        # 元素初始化
        self.stars = pygame.sprite.Group()
        self._generate_star_lines()

    def _generate_star_lines(self):
        """用于产生星星队列"""
        star = Star(self)
        gap_x = star.rect.width
        gap_y = star.rect.height

        current_x  = gap_x
        current_y = gap_y
        while current_y < self.setting.screen_height - 3 * gap_y:
            while current_x < self.setting.screen_width - gap_x:
                self._creat_stars(current_x, current_y)
                current_x += 2 * gap_x 
                print(current_x, current_y)
            current_x = gap_x
            current_y += 2 * gap_y
            

    def _creat_stars(self, x, y):
        new_star = Star(self)
        new_star.rect.x = x
        new_star.rect.y = y
        self.stars.add(new_star)

    def _upgrade_screen(self):
        """绘制屏幕上的各种元素"""
        
        self.screen.fill(self.setting.bg_color)
        self.stars.draw(self.screen)
        
        pygame.display.flip()

    def run_game(self):
        """游戏主循环"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._upgrade_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    stars = Stars()
    stars.run_game()