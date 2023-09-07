from pathlib import Path
import csv
import pandas as pd
import plotly.express as px

path_fire_data = Path('../data/world_fires_1_day.csv')

heads = ['latitude', 'longitude', 'brightness']

# 获取数据的函数(这里直接基于16.2的取数函数来调整，其实可能可以不用这么复杂)
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
                dic_out[item] = []

    # 提取需要的数据
    for row in reader:
        for item in heads:
            is_date = item == 'DATE'
            is_number = item == 'latitude' or item == 'longitude' 
            
            index = dic_head_to_num[item]

            if is_date:    
                try:
                    data = datetime.strptime(row[index], '%Y-%m-%d')
                except ValueError:
                    print(f"Missing data for {data}")
            elif is_number:
                try:
                    data = float(row[index])
                except ValueError:
                    print(f"Missing data for {item}, in {dic_out['DATE'][index]}")
                    data = None
            dic_out[item].append(data)
    
    return dic_out

# 获得想要的数据
dic_fire = get_dates(path_fire_data, heads)

# 把数据转化为pandas的DataFrame对象
datas = pd.DataFrame(
    data=zip(dic_fire['longitude'], dic_fire['latitude'], dic_fire['brightness']),
    columns=['经度', '纬度', '火灾强度']
)

# 绘制图表
fig = px.scatter(
    datas,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    color='火灾强度',
)

# 显示图表
fig.show()