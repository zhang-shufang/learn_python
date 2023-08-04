class GameStats:
    """分数信息"""
    def __init__(self, game) -> None:
        """初始化"""
        self.hit = 0
        self.taking_time = 0
    
    def reset(self):
        """重置分数"""
        self.hit = 0
        self.taking_time = 0

    
