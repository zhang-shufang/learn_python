from unittest import result
import matplotlib.pyplot as plt
from die import Die

# 新建两个骰子
die1 = Die()
die2 = Die()

# 对投掷结果进行采样并储存
num_sampling = 1_000
results = [die1.roll() + die2.roll() for time in range(num_sampling)]

# count the results 
min_result = 2
max_result = die1.num_sides + die2.num_sides
poss_num = range(min_result, max_result)
frequencies = [results.count(value) for value in poss_num]

# print(frequencies)

# draw picture
fig, ax = plt.subplots()

ax.bar(poss_num, frequencies)

ax.set_title('Two Dice')
ax.set_ylabel('Frequencies')
ax.set_xlabel('Poss Numbers')

ax.set_xticks(poss_num)     # 用于设定横坐标的刻度

plt.show()