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
'''
med_count = {}

# 填入欄位名稱
for d in data['features']:
    county = d['properties']['county']
    if county not in med_count:
         med_count[county] = 0
    med_count[county] += 1


print(med_count) # {'台北市': 123, '新北市': 456 ...}
'''

# 建立一個空的字典來存放口罩數量
mask_count = {}

# 填入欄位名稱
for d in data['features']:
    county = d['properties']['county']
    mask_count[county] = d['properties']['mask_adult']
# 如果字典中沒有這個縣市，就初始化為 0
    if county not in mask_count:
        mask_count[county] = 0
    # 將口罩數量加到對應的縣市
    mask_count[county] += d['properties']['mask_adult']


# 將結果從大到小排列
mask_count = dict(sorted(mask_count.items(), key=lambda item: item[1], reverse=True))

print(mask_count)# {'台北市': 12345, '新北市': 45678 ...}
