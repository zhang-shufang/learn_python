import sys
import pygame

from settings import Settings
from raindrop import RainDrop

class RainDrops:
    """雨滴的游戏主类"""
    def __init__(self) -> None:
        """游戏初始化"""
        # 设置参数导入
        self.settings = Settings()
        
        # 屏幕初始化
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("RainDrop")

        # 雨滴初始化
        self.raindrops = pygame.sprite.Group()
        self.raindrop = RainDrop(self)
        self._creat_rain()

    def _upgrade_rain(self):
        """更新下雨的函数"""
        self.raindrops.update()
        for raindrop in self.raindrops:
            # print(raindrop.check_edge)
            if raindrop.check_out():
                self.raindrops.remove(raindrop)

    def _creat_rain(self):
        """产生雨滴队列"""
        gap_x = self.raindrop.rect.x
        gap_y = self.raindrop.rect.y
        current_x = gap_x
        current_y = gap_y
        while current_y < self.settings.screen_height - gap_y:
            while current_x < self.settings.screen_width - gap_x:
                self._creat_raindrop(current_x, current_y)
                current_x += gap_x * 2
            current_x = gap_x
            current_y += gap_y * 2

    def _creat_raindrop(self, x, y):
        """产生单个雨滴"""
        new_raindrop = RainDrop(self)
        new_raindrop.rect.x = x
        new_raindrop.rect.y = y
        self.raindrops.add(new_raindrop)

    def _upgrade_screen(self):
        """加载并绘制屏幕信息"""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        """主要用于关闭界面"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
    def run_game(self):
        """游戏主循环"""
        while True:
            self._upgrade_rain()
            print(self.raindrops)
            self._upgrade_screen()
            self._check_events()
            
# 实例化并运行游戏
if __name__ == "__main__":
    raindrops = RainDrops()
    raindrops.run_game()