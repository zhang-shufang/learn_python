from tokenize import String
import pygame.font

class Button:
    """游戏按钮的类"""
    def __init__(self, game, msg, align = 'center', position = (0,0)) -> None:
        """初始化"""
        # 窗口初始化
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # 按钮的字体设置
        self.font = pygame.font.SysFont(None, 48)
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        

        # 按钮的基本属性
        self.msg = msg
        self.msg_image = None
        self.msg_image_rect = None
        self.width = None
        self.height = None
        self.rect = None

        self.align = align
        self.position = position

        # 按钮设置函数，可按要求进行自适应
        self.set_button(self.msg)

    def set_button(self, msg):
        """设置按钮的文本，并自适应大小"""
        # 渲染文本并获取区域数据
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

        # 设置按钮尺寸
        self.width = self.msg_image_rect.width + 24
        self.height = self.msg_image_rect.height + 24

        # 创建按钮的 rect 对象，在屏幕对应位置对其
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        setattr(self.rect, self.align, self.position)     #设置对象属性值
        
        # 文字与按钮居中对齐
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        # self.msg_image_rect.center = self.rect.center
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

