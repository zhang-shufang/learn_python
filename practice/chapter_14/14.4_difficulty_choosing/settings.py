class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""
    def __init__(self) -> None:
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 飞船的设置
        
        self.ship_limit = 1

        # 子弹的设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.buttets_allow = 3

        # 加速倍率
        self.speedup_scale = 3

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """动态设置初始化"""
        # 子弹速度
        self.bullet_speed = 10.0

        # 飞船速度
        self.ship_speed = 5

        # 外星人运动
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        self.fleet_direction = 1    # 1表示向右，-1向左

    def increase_speed(self):
        """加快速度"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale