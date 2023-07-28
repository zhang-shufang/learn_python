class Settings:
    """横向射击的设置类"""
    def __init__(self) -> None:
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 飞船的设置
        self.rocket_speed = 10

        # 子弹的设置
        self.bullet_speed = 10.0
        self.bullet_width = 10
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.buttets_allow = 3

        # 外星人的设置
        self.alien_speed = 5.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # 1表示向右，-1向左