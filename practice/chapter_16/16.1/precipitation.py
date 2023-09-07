from pathlib import Path
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime

path = Path("../data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()       # 将数据文件按照行来读取，并按行存为列表

reader = csv.reader(lines)      # 创建读取对象，其类型为一个迭代器(似乎更可能是链表)

header_row = next(reader)       # 读取表头

# 确定表头索引及其对应的内容
# for index, value in enumerate(header_row):
#     print(index, value)

# 提取所需要的数据：降水量
dates, precipitaions = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
    precipitaion = float(row[5])            # !!!!!!!!!!!!!!因为没有转换数据类型，会导致图像的y轴一直刻度不对！！！！
    
    dates.append(current_date)
    precipitaions.append(precipitaion)

# 根据数据绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precipitaions, color='blue')

# 设置绘图样式
title = "Daily Precipitation, 2021\nSitka"
ax.set_title(title, fontsize=20)

ax.set_xlabel('', fontsize=6)
ax.xaxis.set_major_locator(mdates.MonthLocator())   # 按月为刻度来设置x轴
fig.autofmt_xdate()

ax.set_ylabel('Precipitation', fontsize=16)

ax.tick_params(labelsize=8)

plt.show()