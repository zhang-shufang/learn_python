from random import choice

class RandomWalk:
    """生成一个随机游走数据的类"""
    
    def __init__(self, num_points=5000) -> None:
        """初始化随机游走的属性"""
        self.num_points = num_points

        # 所有随机游走都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """随机游走的函数"""
        
        # 不断游走，直到列表到达指定长度
        while len(self.x_values) < self.num_points:
            
            # 确定前进的方向、距离和步长
            x_direction = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
                
            # 计算下一个点的坐标并储存
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            