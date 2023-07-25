- [12 游戏与pygame](#12-游戏与pygame)
  - [12.1 安装pygame](#121-安装pygame)
  - [12.？ pygame的常用函数](#12-pygame的常用函数)
    - [游戏初始化](#游戏初始化)
    - [游戏控制](#游戏控制)
    - [帧率控制](#帧率控制)
    - [颜色与填充](#颜色与填充)
    - [素材加载与绘制](#素材加载与绘制)


# 12 游戏与pygame

## 12.1 安装pygame
在终端使用以下命令来安装 `pygame` ：
```python
$ python -m pip install --user pygame       # 适用用于python3以下版本
$ python3 -m pip install --user pygame      # 适用于python3的版本
```

## 12.？ pygame的常用函数
### 游戏初始化
- `sys` 模块: 玩家退出时，会使用其中的工具来退出游戏。
- `pygame.init()`: 初始化背景。
- `pygame.display.set_mode(width, high)`: 接受两个表示界面长宽的参数，并返回一个 `surface` 。功能为创建一个显示窗口，游戏中的图形元素都将在其中显示。（在 pygame 中，surface用于显示游戏元素，每个元素（例如外星人或飞船）都是一个surface。

### 游戏控制
控制基础：
游戏的控制的实现是通过 **事件** （event） 来实现的。主要有以下方法：
- `pygame.event.get()`: 返回一个列表，包含它在上一次调用后发生的所有事件。
- `event.type`: 访问事件的类型属性。其值可能是下方“游戏事件类型“的一种。
- `event.key`: 访问事件的
- `sys.exit()`: 此函数调用时可退出游戏。

游戏事件类型：
- `pygame.QUIT`: 游戏退出事件，玩家点击关闭游戏的窗口所获得的事件为此事件。
- `.KEYDOWN`: 每当按键被按下时，会产生一个此事件。

### 帧率控制
理想情况下，游戏在所有的系统中都应该以相同的速度（帧率）运行。这通常会反映在主循环中画面刷新的速率。在 pygame 中，可以通过创建一个时钟（clock）来实现对帧率的控制。
- `pygame.time.Clock()`: 用于创建时钟。通常会赋值作为游戏的属性之一。例如`self.clock = pygame.time.Clock()`。
- `clock.tick(f)`: 时钟的计时（tick）方法，通常放在游戏主循环的最后，接受一个表示游戏帧率的数字参数。例如参数为60，则该函数其会确保每秒 while 循环运行 60 次。

### 颜色与填充
- `.fill(rgb)`: 用于处理 surface 的方法，接受一个表示颜色的实参，能够将颜色填充到对应的 surface 里。

### 素材加载与绘制
- `pygame.image.load('file_path')`: 通过路径加载图片文件，返回一个 surface 。也可接受其他参数，详见 pygame 文档。
- `.blit(source, dest)`: surface 的一个方法，可将资源按照位置（dest）绘制在目标 surface 上。