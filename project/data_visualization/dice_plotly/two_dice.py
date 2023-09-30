from die import Die
import plotly.express as px

# 创建一个骰子
die_1 = Die()
die_2 = Die(10)

# 投掷几次骰子，并将其除存在列表中
results = []

for roll_time in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# 对结果进行可视化
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice_visual_d6d10.html')