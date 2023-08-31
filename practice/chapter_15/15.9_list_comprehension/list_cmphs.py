from multiprocessing.sharedctypes import Value
from die import Die
import plotly.express as px

# 创建一个骰子
die_1 = Die()
die_2 = Die()

# 投掷几次骰子，并将其除存在列表中

num_sampling = 1_000

results = [die_1.roll() * die_2.roll() for roll_time in range(num_sampling)]

# for roll_time in range(int(num_sampling)):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)

# print(results)

# 分析结果

max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)

frequencies = [results.count(value) for value in poss_results]

# for value in poss_results:
#     frequency = results.count(value) / num_sampling
#     frequencies.append(frequency)

print(poss_results)
print(frequencies)
# 对结果进行可视化
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
# fig.write_html('dice_visual_d6d10.html')