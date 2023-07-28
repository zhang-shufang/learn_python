from __future__ import barry_as_FLUFL
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
        self.rd_current_x = self.raindrop.rect.x    # 由于x需要在函数外保存数值，因此放在这里
        self.rd_current_y = - self.raindrop.rect.y  # 放在这是为了和x统一
        self.rd_limit = 0                           # 单行雨滴最多11个

    def _upgrade_rain(self):
        """更新下雨的函数"""
        # 按条件持续生产雨滴
        self._creat_rain_row()

        # 更新雨滴的行动
        self.raindrops.update()
        
        # 删除屏幕外的雨滴
        for raindrop in self.raindrops:
            # print(raindrop.check_edge)
            print(self.raindrops)
            if raindrop.check_out():
                self.raindrops.remove(raindrop)

    def _creat_rain_row(self):
        """在屏幕上方视野外产生一行雨滴"""
        """当还未到边界且一行数量小于11时一直递增横坐标产生雨滴，
            到达边界后横坐标归零。
            若雨滴进入界面后，可减少数量限制以生成新的雨滴。"""
        gap_x = self.raindrop.rect.x
        boder_x = self.settings.screen_width - gap_x

        while self.rd_current_x < boder_x and self.rd_limit < 11:
            self._creat_raindrop(self.rd_current_x, self.rd_current_y)
            self.rd_limit += 1
            self.rd_current_x += gap_x * 2
            # print(is_in_boder, is_not_limited)
            # print(self.rd_limit, self.rd_current_x, current_y)
        
        if self.rd_current_x >= boder_x:
            self.rd_current_x = gap_x

        for raindrop in self.raindrops:
            if raindrop.check_in():
                self.rd_limit -= 1
                break

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
            self._upgrade_screen()
            self._check_events()
            
# 实例化并运行游戏
if __name__ == "__main__":
    raindrops = RainDrops()
    raindrops.run_game()