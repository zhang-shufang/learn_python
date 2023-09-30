from die import Die
import plotly.express as px

# 创建一个骰子
die = Die()

# 投掷几次骰子，并将其除存在列表中
results = []

for roll_time in range(6000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# 对结果进行可视化
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()