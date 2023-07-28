class Settings:
    """雨滴的设置文件"""
    def __init__(self) -> None:
        """初始化"""
        # 屏幕参数
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 雨滴设置
        self.raindrop_speed = 2