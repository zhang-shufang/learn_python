from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path_dv = '../data/death_valley_2021_simple.csv'
path_sk = '../data/sitka_weather_2021_simple.csv'

heads = ['NAME', 'DATE', 'TMAX', 'TMIN']

# 获取数据的函数
def get_dates(path_str, heads):
    """输入文件路径，以及需要提取的数据的表头
    返回一个字典，键为表头，值为符合该表头的数据集"""
    # 读取数据
    path = Path(path_str)
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)

    dic_head_to_num = {}    # 储存表头及对应的索引
    dic_out = {}            # 储存需要输出的数据

    # 获取表头及对应的索引，并初始化输出的字典
    header = next(reader)
    for index in range(len(header)):
        for item in heads:
            if header[index] == item:
                dic_head_to_num[item] = index
                if item == "NAME":              # 站点名称不需要用列表（其实可以统一为列表，但是为了数据类型严谨，在此这样做）
                    value = ''
                else:
                    value = []
                dic_out[item] = value

    # 提取需要的数据
    got_station_name = False
    for row in reader:
        for item in heads:
            is_name = item == 'NAME' 
            is_date = item == 'DATE'
            is_int = item == 'TMAX' or item == 'TMIN'
            
            index = dic_head_to_num[item]

            if is_name:
                if not got_station_name:
                    dic_out[item] = row[index]
                    got_station_name = True
            else:
                if is_date:    
                    try:
                        data = datetime.strptime(row[index], '%Y-%m-%d')
                    except ValueError:
                        print(f"Missing data for {data}")
                elif is_int:
                    try:
                        data = int(row[index])
                    except ValueError:
                        print(f"Missing data for {item}, in {dic_out['DATE'][index]}")
                        data = None
                dic_out[item].append(data)
    
    return dic_out

# 提取两个文件中需要的数据
datas_dv = get_dates(path_dv, heads)
datas_sk = get_dates(path_sk, heads)

# 通过前后均值来补充缺失的数据
tmax = datas_dv['TMAX']

for index, value in enumerate(tmax):
    if value == None:
        data = (tmax[index-1] + tmax[index+1])/2
        tmax[index] = data

datas_dv['TMAX'] = tmax

# 根据高温数据绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
name_dv = datas_dv['NAME']
line1, = ax.plot(datas_dv['DATE'], datas_dv['TMAX'], linewidth=1, label=name_dv, color='red', alpha=0.3)    # 注意需要有逗号才能发挥作用
ax.plot(datas_dv['DATE'], datas_dv['TMIN'], linewidth=1, color='red', alpha=0.3)
ax.fill_between(datas_dv['DATE'], datas_dv['TMAX'], datas_dv['TMIN'], facecolor='red', alpha=0.1)

name_sk = datas_sk['NAME']
line2, = ax.plot(datas_sk['DATE'], datas_sk['TMAX'], linewidth=1, label=name_sk, color='blue', alpha=0.3)
ax.plot(datas_sk['DATE'], datas_sk['TMIN'], linewidth=1, color='blue', alpha=0.3)
ax.fill_between(datas_sk['DATE'], datas_sk['TMAX'], datas_sk['TMIN'], facecolor='blue', alpha=0.1)

# 设置图例
ax.legend([line1, line2], [name_dv, name_sk])

# 设置绘图的标题
title = "Daily High and Low Tempreatures Comparsion in 2021\nDeath Valley VS Sitka"
ax.set_title(title, fontsize=20)

# 设置横纵坐标标题及刻度
ax.set_xlabel('', fontsize=6)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()