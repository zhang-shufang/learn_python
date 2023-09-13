import requests
import plotly.express as px


def run_api(url):
    """该函数用于执行API调用并查看响应结果"""

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    
    return r

# 执行API调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
r = run_api(url)
print(f"Status code: {r.status_code}")  # 显示API是否正常运行

# 处理结果
response_dict = r.json()
print(f"Complete results: {response_dict['incomplete_results']}")   # 确认收到了完整的结果集

# 提取需要的数据
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"    
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
title = "Most-Starred Python Projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.1)

fig.show()
