import requests
import json


# 利用 requests 對 API 來源發送一個請求
response = requests.get("https://raw.githubusercontent.com/kiang/pharmacies/master/json/points.json")


# 將請求回應的內容存成一個字串格式
data = response.text

# 將長得像 json 格式的字串解析成字典或列表
data = json.loads(data)

# 印出解析後的資料
#print(data)

med_count = {}

# 填入欄位名稱
for d in data['features']:
    county = d['properties']['county']
    if county not in med_count:
         med_count[county] = 0
    med_count[county] += 1


print(med_count)
# {'台北市': 123, '新北市': 456 ...}

