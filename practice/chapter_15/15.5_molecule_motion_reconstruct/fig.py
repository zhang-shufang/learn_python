import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from random_walk import RandomWalk

# 创建一个RandomWalk实例
rw = RandomWalk(5000)
rw.fill_walk()

# 创建一个colormap类型的渐变色
colors = ['blue', 'red']    # 需要渐变的颜色
cmap = mcolors.LinearSegmentedColormap.from_list('cmap', colors)

# 将所有点都绘制出来
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

point_number = range(rw.num_points)     # 确定步数用以画折线
color_map = cmap(np.linspace(0, 1, len(point_number)))  # 将colormap类转化为在0～1之间的可进行输入的颜色数组

# 按步绘制折线，注意输入的x和y需要是一组一组的，最小需要两个点来确定一个线段。
for i in point_number:
    # print(i)
    ax.plot(rw.x_values[i:i+2], rw.y_values[i:i+2], color=color_map[i], linewidth=1)

# 突出起点和终点
ax.scatter(0, 0, c='blue', edgecolors='black', s=100, zorder=float('inf'))
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='black', s=100, zorder=float('inf'))

# 隐藏坐标轴
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
ax.set_aspect('equal')
plt.show()