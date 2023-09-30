import imp
import requests
import json

# 执行API调用并存储响应
url = "https://hacker_news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url, verify=False)
print(f"Status code: {r.status_code}")

# 探索数据的结构
response_dict= r.json()
response_string= json.dumps(response_dict, indent=4)
print(response_string)
