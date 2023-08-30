import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=1)

# 设置题图并给坐标轴加上标签
ax.set_title("Cube Number", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

# 设置坐标轴的取值范围
ax.ticklabel_format(style="sci")

plt.show()